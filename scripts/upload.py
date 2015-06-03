
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
    db = MySQLdb.connect(host='173.194.82.159', port=3306, db='gsdmarin', user='ruifu', passwd='1234')
            # Alternatively, connect to a Google Cloud SQL instance using:
            # db = MySQLdb.connect(host='ip-address-of-google-cloud-sql-instance', port=3306, user='root', charset='utf 8')
    cursor = db.cursor()
    sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
    cursor.execute(sql)
    db.close()
    return

		#return self.redirect('/pages/parser/upload.html')