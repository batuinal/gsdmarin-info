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

# This file is indented by tabs.

class attrlib:
	# Make "lim" (character limit) come from a central source?
	def getAttr(self, attr):
		if (attr == "text"):
			return "VARCHAR(255)"
		elif (attr == "num"):
			return "SMALLINT"
		elif (attr == "bool"):
			return "VARCHAR(7)"
		elif (attr == "char"):
			return "CHARACTER(1)"
		elif (attr == "ship"):
			return "VARCHAR(15)"
		elif (attr == "date"):
			return "DATE"
		elif (attr == "time"):
			return "TIME"
		elif (attr == "link"):
			return "VARCHAR(255)"
		elif (attr == "loc"):
			return "VARCHAR(63)"
		elif (attr == "coord"):
			return "VARCHAR(63)"
		elif (attr == "file"):
			return "VARCHAR(255)"
		else:
			err = "Error - Unknown attribute type: " + attr
			logging.info(err)
			return "INVALID"