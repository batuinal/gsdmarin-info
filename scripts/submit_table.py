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

		name_table = self.request.get('table')
		args = self.request.arguments()

		row_dict = {}
		for arg in args:
			row_col = arg.split('_')
			if row_dict.has_key(int(row_col[0])):
				row_dict[int(row_col[0])].append(pair(row_col[1], self.request.get(arg)))
			else:
				row_dict[int(row_col[0])] = []
				row_dict[int(row_col[0])].append(pair(row_col[1], self.request.get(arg)))

		sqlimpl = sqllib();
		sqlimpl.RemoveAllEntities(name_table)

		for key in row_dict:
			r_id = sqlimpl.AddEntity(name_table)
			sqlimpl.SetAttributes(name_table, r_id, row_dict[key])

		#Debugging..
		#self.response.out.write(row_dict)
		#for x in range(-2,4):
		#	logging.info("ROW NUMBER IS: " + str(x))
		#	for y in range(0,4):
		#		logging.info(row_dict[x][y].first)
		#		logging.info(row_dict[x][y].second)
		