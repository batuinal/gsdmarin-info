import os
import urllib
import cgi

from google.appengine.api import users
import webapp2

class LoginPage(webapp2.RequestHandler):
    def get(self):
        return self.redirect('/',permanent=True)

class LoginChecker(webapp2.RequestHandler):
    def post(self):
		return self.redirect('/main/win8/docs/index.html',permanent=True)

app = webapp2.WSGIApplication([
    ('/', LoginPage),	
    ('/loggedin', LoginChecker)
], debug=True)

