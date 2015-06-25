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

# This Python File uses Tabs for Alignment

class create_table(webapp2.RequestHandler):
		
	def post(self):
		try:

			
			select = []
			textbox = []
			
			pageid = self.request.get('pageid')
			tname = self.request.get('table_name')
			
			for arg in self.request.arguments():
				elt = self.request.get(arg)
				if re.match(r'select',arg):
					select.append(elt)
				elif re.match(r'textbox',arg):
					textbox.append(elt)
		
			out = "-- Page ID: " + pageid + ", Table Name: " + tname + " <br>"
			self.response.out.write(out)
			
			self.response.out.write("-- Attributes: <br>")
			for i in range(len(select)):
				out = "(" + select[i-1] + "," + textbox[i-1] + ") <br>"
				self.response.out.write(out)
		
		except:
			logging.error('-- Error: Exception thrown during execution.')
			self.response.out.write('-- Error: Exception thrown during execution.')