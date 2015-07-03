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

class create_table(webapp2.RequestHandler):

	
	def post(self):
		#try:

			
			attr = [] # holds pairs(first = select, second = textbox)
			
			pageid = self.request.get('pageid')
			tname = self.request.get('table_name')
			
			for n in range(0, 99):
				select = self.request.get('select_' + str(n),"INVALID")
				textbox = self.request.get('textbox_' + str(n),"INVALID")
				if (select != "INVALID"):
					attr.append(pair(select, textbox))
		
			out = "-- Page ID: " + pageid + ", Table Name: " + tname + " <br>"
			self.response.out.write(out)
			
			self.response.out.write("-- Attributes: <br>")
			for i in range(len(attr)):
				out = "(" + attr[i].first + "," + attr[i].second + ") <br>"
				self.response.out.write(out)
		
		#except:
			#logging.error('-- Error: Exception thrown during execution.')
			#self.response.out.write('-- Error: Exception thrown during execution.')