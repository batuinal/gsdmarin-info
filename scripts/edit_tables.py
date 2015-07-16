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
from attrlib import attrlib
from tuplelib import pair

# This Python File uses Tabs for Alignment

class edit_tables(webapp2.RequestHandler):

	def post(self):
		#try:
			
			attr = [] # holds pairs(first = select, second = textbox)
			
			reqtype  = self.request.get('reqtype')
			pageid = self.request.get('pageid')
			tname = self.request.get('table_name')
			
			sqlimpl = sqllib();
			attrimpl = attrlib();
			
			out = "-- Request Type: " + reqtype + ", -- Page ID: " + pageid + ", Table Name: " + tname + " <br>"
			self.response.out.write(out)				
			
			resp = []
			
			if (reqtype == "remove"):
				sqllib.RemoveTable(tname,pageid)
			elif (reqtype == "create"):				
				for n in range(0, 99):
					select = self.request.get('select_' + str(n),"INVALID")
					textbox = self.request.get('textbox_' + str(n),"INVALID")
					if (select != "INVALID"):
						attr.append(pair(select, textbox))

				resp.append(sqlimpl.CreateTable(tname,pageid))
				for a in attr:
					resp.append(sqlimpl.AddAttribute(tname, pageid, a.second, attrimpl.getAttr(a.first), a.first))

						
				# [Debug]
				self.response.out.write("-- Attributes: <br>")
				for i in range(len(attr)):
					out = "(" + attr[i].first + "," + attr[i].second + ") <br>"
					self.response.out.write(out)
					
				self.response.out.write("-- Server Responses: <br>")
				for r in resp:
					out = str(r) + "<br>"
					self.response.out.write(out)
				# [/Debug]
				
			else:
				out = "-- Error: Unknown request type (" + reqtype + ")."
			
			url = "/view_table?pageid=" + pageid
			self.redirect(url)
		#except:
			#logging.error('-- Error: Exception thrown during execution.')
			#self.response.out.write('-- Error: Exception thrown during execution.')