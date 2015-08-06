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

class submit_table(webapp2.RequestHandler):

	def post(self):
	
		args = self.request.arguments()
		self.response.out.write(args)
		self.response.out.write("\n\n\n")
		
		for arg in args:
			self.response.out.write(arg)
			self.response.out.write(": ")
			self.response.out.write(self.request.get(arg))
			self.response.out.write("\n")
		
	
	
	
	
	
	