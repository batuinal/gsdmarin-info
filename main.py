import os
import urllib
import cgi
from google.appengine.ext.webapp.util import run_wsgi_app

from google.appengine.api import users
import webapp2

#Somebody fix this importing scheme...
import scripts.upload
import scripts.login
import scripts.error404
		
app = webapp2.WSGIApplication([
    ('/', scripts.login.LoginPage),	
	('/upload', scripts.upload.FileUpload),
	('/parse', scripts.upload.Parse),
	('/*', scripts.error404.NotFoundHandler)
], debug=True)

