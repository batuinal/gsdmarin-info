import os
import urllib
import cgi

from google.appengine.api import users
import webapp2

class NotFoundHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('<head><title>Page Not Found</title></head> \n <body><h1>Error 404 - Requested page does not exist.</h1></body>')
	def post(self):
		self.response.write('<head><title>Page Not Found</title></head> \n <body><h1>Error 404 - Requested page does not exist.</h1></body>')