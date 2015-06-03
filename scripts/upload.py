import os
import urllib
import cgi

from google.appengine.api import users
import webapp2

class FileUpload(webapp2.RequestHandler):
	def get(self):
		return self.redirect('/pages/ananinami.html')