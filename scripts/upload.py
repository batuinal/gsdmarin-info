
import cgi
import webapp2

from google.appengine.api import users
import MySQLdb
import os
import urllib
import jinja2


# Define your production Cloud SQL instance information.
_INSTANCE_NAME = 'gsdmarin-info:database'

class FileUpload(webapp2.RequestHandler):
	def get(self):
		 # Display existing guestbook entries and a form to add new entries.
		if (os.getenv('SERVER_SOFTWARE') and os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/')):
			db = MySQLdb.connect(unix_socket='/cloudsql/' + _INSTANCE_NAME, db='gsdmarin', user='batu', charset='utf 8')
		else:
			db = MySQLdb.connect(host='127.0.0.1', port=3306, db='guestbook', user='root', charset='utf 8')
            # Alternatively, connect to a Google Cloud SQL instance using:
            # db = MySQLdb.connect(host='ip-address-of-google-cloud-sql-instance', port=3306, user='root', charset='utf 8')
  		cursor = db.cursor()
  		db.close()
  		return

		#return self.redirect('/pages/parser/upload.html')