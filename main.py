import os
import urllib
import cgi

from google.appengine.api import users
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        return self.redirect('/',permanent=True)

class LoggedIn(webapp2.RequestHandler):
    def post(self):
		return self.redirect('/main/index.html',permanent=True)

app = webapp2.WSGIApplication([
    ('/', MainPage),	
    ('/loggedin', LoggedIn)
], debug=True)

