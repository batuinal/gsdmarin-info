import os
import urllib
import cgi

from google.appengine.api import users
import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.redirect('/')

class Contents(webapp2.RequestHandler):
    def post(self):
        self.redirect('/main/index.html')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/contents', Contents),
], debug=True)

