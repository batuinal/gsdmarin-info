import os
import urllib
import cgi
from google.appengine.ext.webapp.util import run_wsgi_app

from google.appengine.api import users
import webapp2

class LoginPage(webapp2.RequestHandler):
    def get(self):
        return self.redirect('/pages/login.html')