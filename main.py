import os
import urllib
import cgi
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import webapp
from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import ndb

from google.appengine.api import users
import webapp2
import logging

#Somebody fix this importing scheme...
import scripts.upload
import scripts.login
import scripts.error404
import scripts.images
		
app = webapp2.WSGIApplication([
    ('/', scripts.login.LoginPage),	
	('/upload', scripts.upload.FileUpload),
	('/upload_file', scripts.upload.Upload),
	('/images', scripts.images.ImageUpload),
	('/images_upload', scripts.images.Upload),
	('/parse/([^/]+)?', scripts.upload.Parse),
	('/*', scripts.error404.NotFoundHandler)
], debug=True)

