import os
import urllib
import cgi

from google.appengine.api import users
import webapp2

#Somebody fix this importing scheme...
import scripts.upload
import scripts.login
import scripts.error404

		
app = webapp2.WSGIApplication([
    ('/', scripts.login.LoginPage),	# ...and these too while you're at it.	
	('/upload', scripts.upload.FileUpload),
	('/*', scripts.error404.NotFoundHandler)
], debug=True)

