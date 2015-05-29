import os
import urllib
import cgi

from google.appengine.api import users
import webapp2

class LoginPage(webapp2.RequestHandler):
    def get(self):
        return self.redirect('/pages/login.html')

class LoginChecker(webapp2.RequestHandler):
    def post(self):
		return self.redirect('/pages/index.html')

class UploadHandler(webapp2.RequestHandler):
    def post(self):

    print self.request.POST['file'].filename
		
class NotFoundHandler(webapp2.RequestHandler):
	def get(self):
		self.error(404)
		self.response.write('<head><title>Page Not Found</title></head> \n <body><h1>Error 404 - Page Not Found.</h1></body>')

app = webapp2.WSGIApplication([
    ('/', LoginPage),	
    ('/loggedin', LoginChecker),
	('/*', NotFoundHandler)
], debug=True)

