import MySQLdb
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
		out += '<link rel="stylesheet" type="text/css" href="DataTables-1.10.7/media/css/jquery.dataTables.css">'
		out += '<script src="pages/js/jquery-2.1.3.min.js"></script>\n'
		out += '<script src="DataTables-1.10.7/media/js/jquery.dataTables.js"></script>\n'
		out += '<script src="js/testtable.js"></script>\n'
		out += '<div id="request"></div>\n'
		out += '</head>\n'
		self.response.out.write(out)
		
		# Body Scaffolding
		out = '<body>\n'
		out += '<h1>' + page + ' Page</h1>\n'
		self.response.out.write(out)
		
		# We don't have this function yet.
		tables = sqlimpl.GetEntitiesByAttr("MASTER","PAGE",page)\
		
		if (len(tables) == 3):
			for table in tables[2]:
				out = "<div> Table: " + table + "</div><br>"
				self.response.out.write(out)
				#out = '<table id="' + str(table) + '" class="display" cellspacing="0" width="100%">'
				#self.response.out.write(out)
				
				#listout = sqlimpl.ListAllEntities(table) [UNCOMMENT]
				#entities = listout[0]
				#classes = listout[1]
				
				# Parse out the table.
		
		
		
		# Body Scaffolding
		out = '<button type="button" onclick="request(' + "'GET','/pages/create_table.html',['pageid'],[document.getElementById('pageid').getAttribute('value')])" + '">Create New Table</button>\n'
		out += '<script>\n'
		out += '$(function(){\n'
		out += '$("#request").load("pages/modules/request.html");\n'
		out += '});\n'
		out += '</script>\n'
		out += '</body>\n'
		self.response.out.write(out)
		
		
		

