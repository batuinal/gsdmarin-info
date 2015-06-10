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

class ImageUpload(webapp2.RequestHandler):
	def get(self):
		upload_url = blobstore.create_upload_url('/images_upload')
		html = ''
		html += '<html><body>'
		html += '<form action="%s" method="POST" enctype="multipart/form-data">' % upload_url
		html += """Description: <input type="text" name = "description"> <br>
            Upload Image: <input type="file" name="image"><br> 
            <input type="submit" name="submit" value="Parse"> </form></body></html>"""
		self.response.out.write(html)

class Upload(blobstore_handlers.BlobstoreUploadHandler, webapp2.RequestHandler):
  def post(self):
    try:
      upload_files = self.get_uploads('image')
      image_description = self.request.get('description')
      self.response.out.write('Table Name received.  Name=%s' % (image_description))
      self.response.out.write('File upload received.  File count=%d' % len(upload_files))
      if len(upload_files) > 0:
        blob_info = upload_files[0]
        self.response.out.write('Blob stored key=%s' % (blob_info.key()))
        user_file = UserFile(blob_key=blob_info.key())
        user_file.put()
        self.response.headers['Content-Type'] = 'image/png'
        self.response.out.write(user_file.avatar)
    except:
        logging.error('Error in Uploading/Parsing')
        self.response.out.write('Error in processing the file')