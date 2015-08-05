﻿import MySQLdb
import urllib
import jinja2
import os
import urllib
import cgi
import csv
import StringIO
import string
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import webapp
from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import ndb

from google.appengine.api import users
import webapp2
import logging
import re

from sqllib import sqllib
from tuplelib import pair

# This Python File uses Tabs for Alignment

class view_table(webapp2.RequestHandler):

	def get(self):

		sqlimpl = sqllib();
	
		page = self.request.get('pageid')
		
		# Header Creation
		out = '<head>\n'
		out += '<title>' + page + ' Page</title>\n'
		out += '<div id="pageid" value="' + page + '"></div>\n'
		out += '<link rel="stylesheet" type="text/css" href="pages/DataTables-1.10.7/media/css/jquery.dataTables.css">'
		out += '<script src="pages/js/jquery-2.1.3.min.js"></script>\n'
		out += '<script src="pages/DataTables-1.10.7/media/js/jquery.js"></script>'
		out += '<script src="pages/DataTables-1.10.7/media/js/jquery.dataTables.js"></script>\n'
		out += '<script src="pages/js/viewtable.js"></script>\n'
		out += '<script src="pages/js/jsac.js"></script>\n'
		out += '<script src="pages/js/edit_mode.js"></script>\n'
		
		out += '<script src="https://addthisevent.com/libs/1.6.0/ate.min.js"></script>\n'
		out += '<script> addthisevent.settings({license    : "00000000000000000000",'
		out += 'mouse      : false, css : true,'
		out += 'google     : {show:true, text:"Google <em>(online)</em>"},'
		out += 'outlookcom : {show:true, text:"Outlook.com <em>(online)</em>"},'
		out += 'appleical  : {show:true, text:"Apple Calendar"},'
		out += 'facebook   : {show:true, text:"Facebook Event"}, });</script>'

		out += '<div id="request"></div>\n'
		out += '</head>\n'
		self.response.out.write(out)
		
		# Body Scaffolding
		out = '<body>\n'
		out += '<h1>' + page + ' Page</h1>\n'
		out += ' <div title="Add to Calendar" class="addthisevent" data-track="_gaq.push([' + "'_trackEvent','AddThisEvent','click','ate-calendar'" + '"])"> '
		out += 'Add to Calendar <span class="start">08/18/2015 09:00 AM</span>'
		out +=	'<span class="end">08/18/2015 11:00 AM</span>'
		out +=	'<span class="timezone">Europe/Istanbul</span>'
		out +=	'<span class="title">Summary of the event</span>'
		out +=	'<span class="description">Description of the event</span>'
		out +=	'<span class="location">Location of the event</span>'
		out +=	'<span class="date_format">MM/DD/YYYY</span> </div>'
		self.response.out.write(out)

		tables = sqlimpl.GetEntitiesByAttr("MASTER","PAGE",page)\
		
		if (len(tables) == 3):
			for table in tables[2]:

				out = '<h3> Table: ' + table + '</h3><br>\n'
				out += '<button id="edit_table" onclick="edit_mode(' + "'#" + str(table) + "',1)" + '">Edit Table</button>'
				out += '<button id="delete_row_' + table +'">Delete Row</button>\n'
				out += '<button id="add_row_' + table +'">Add Row</button>\n'

				self.response.out.write(out)

				# Database Query
				listout = sqlimpl.ListAllEntities(table)
				
				# Scaffold Parsing
				cols = []
				classes = []
				skip = 1;
				for elt in listout:
					if (skip):
						skip = 0
					else:
						cols.append(elt[0])
				
				# Column Selection Code		
				out = '<div id="show_hide"><br/>Show/Hide: \n'
				count = 0
				for col in cols:
					if (col != cols[-1]):
						out += '<a class="' + str(table) + '_toggle-vis" data-column="' + str(count) +'">' + str(col).upper() + '</a> - \n'
					else:
						out += '<a class="' + str(table) + '_toggle-vis" data-column="' + str(count) +'">' + str(col).upper() + '</a></div> \n'
					count += 1
				
				out += '<div id="table-container" width="800px" padding="40px" margins="40px">\n'
				out += '<table id="' + table + '" class="display compact row-border hover" cellspacing="0" width="100%">\n'
				self.response.out.write(out)
						
				# Header Parsing
				out = '<thead>\n'
				out += '<tr>\n'
				for col in cols:
					out += '<th>' + col + '</th>\n'
				out += '</tr>\n'
				out += '<thead>\n'
				self.response.out.write(out)
				
				
				# Body Parsing
				out = '<tbody>\n'
				for n in range(2, len(listout[0])):
					out += '<tr id="' + str(listout[0][n]) + '">\n'
					skip = 1;
					for elt in listout:
						if (skip):
							skip = 0
						else:
							name = str(elt[0]) + str(n-2)
							out += '<td class="jsac_' + elt[1] + '" id="' + name + '">' + str(elt[n]) + '</td>\n'
					out += '</tr>\n'
				
				out += '</tbody>\n'
				self.response.out.write(out)
				
				out = '</table>\n'
				out += '</div>\n'
				self.response.out.write(out)
				
				# Initialize DataTables on Table
				out = '<script>\n'
				out += '$(document).ready(function() {\n'
				out += 'var table = $("#' + str(table) + '").DataTable({"scrollY": "200px", "paging": false});\n'

				#Dynamically Adjust Table Cols
				out += '$("a.' + str(table) + '_toggle-vis").on( "click", function (e) { e.preventDefault();\n'
				out += 'var column = table.column( $(this).attr("data-column") );\n'
				out += 'column.visible( ! column.visible() );} );\n'

				# Row Selection and Deletion
				out += '$("#' + str(table) + ' tbody").on( "click", "tr", function () {\n'
				out += '$(this).toggleClass("selected");\n'
				out += '  } );\n'
				out += '$("#delete_row_' + str(table) + '").click( function () { table.rows(".selected").remove().draw( false );} ); \n'

				# Add Row

				out += '$("#add_row_' + str(table) + '").on( "click", function () {\n'
				out += 'table.row.add( [\n'
				for col in cols:
					if (col != cols[-1]):
						out += '"0",\n'
					else:
						out += '"0"]).draw();\n'
				out += ' } );\n'
				out += ' } );\n'
				out += '</script>\n'
				
				
				self.response.out.write(out)
				
			# Body Scaffolding
			out = '<button type="button" onclick="request(' + "'GET','/pages/create_table.html',['pageid'],[document.getElementById('pageid').getAttribute('value')])" + '">Create New Table</button>\n'
			out += '<script>\n'
			out += '$(function(){\n'
			out += '$("#request").load("pages/modules/request.html");\n'
			out += '});\n'
			out += '</script>\n'
			out += '</body>\n'
			self.response.out.write(out)
		else:
			self.redirect('/notfound')
		
		

		
		
		

