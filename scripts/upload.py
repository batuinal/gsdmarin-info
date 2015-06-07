import MySQLdb
import urllib
import jinja2
import os
import urllib
import cgi
import csv
import StringIO
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import webapp
from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import ndb

from google.appengine.api import users
import webapp2
import logging

#IMPORTNAT NOTE: DOUBLE SPACE WAS USED IN ORDER TO IMPLEMENT INDENTATION FOR PYTHON< PLEASE USE THIS CONVENTION!!!

# Define your production Cloud SQL instance information.
_INSTANCE_NAME = 'gsdmarin-info:database'


class BlobIterator:
    """Because the python csv module doesn't like strange newline chars and
    the google blob reader cannot be told to open in universal mode, then
    we need to read blocks of the blob and 'fix' the newlines as we go.
    Fixed the problem with the corrupted lines when fetching new data into the buffer."""
 
    def __init__(self, blob_reader):
        self.blob_reader = blob_reader
        self.last_line = ""
        self.line_num = 0
        self.lines = []
        self.buffer = None
 
    def __iter__(self):
        return self
 
    def next(self):
        if not self.buffer or len(self.lines) == self.line_num + 1:
            if self.lines:
                self.last_line = self.lines[self.line_num]
            self.buffer = self.blob_reader.read(1048576) # 1MB buffer
            self.lines = self.buffer.splitlines()
            self.line_num = 0
 
            # Handle special case where our block just happens to end on a new line
            if self.buffer[-1:] == "\n" or self.buffer[-1:] == "\r":
                self.lines.append("")
 
        if not self.buffer:
            raise StopIteration
 
        if self.line_num == 0 and len(self.last_line) > 0:
            result = self.last_line + self.lines[self.line_num] + "\n"
        else:
            result = self.lines[self.line_num] + "\n"
 
        self.line_num += 1
        return result

class UserFile(ndb.Model):
  #user = ndb.StringProperty()
  # blob_key = blobstore.BlobReferenceProperty()
  blob_key = ndb.BlobKeyProperty()

class FileUpload(webapp2.RequestHandler):
  def get(self):
    upload_url = blobstore.create_upload_url('/upload_file')
    html = ''
    html += '<html><body>'
    html += '<form action="%s" method="POST" enctype="multipart/form-data">' % upload_url
    html += """Upload File: <input type="file" name="xlfile"><br> <input type="submit"
            name="submit" value="Parse"> </form></body></html>"""
    self.response.out.write(html)
    #self.redirect('/pages/parser/upload1.html')


class Upload(blobstore_handlers.BlobstoreUploadHandler):
  def post(self):
    try:
      upload_files = self.get_uploads('xlfile')
      logging.info('File upload received.  File count=%d' % len(upload_files))
      if len(upload_files) > 0:
        blob_info = upload_files[0]
        logging.info('Blob stored key=%s' % (blob_info.key()))
        user_file = UserFile(blob_key=blob_info.key())
        user_file.put()

        blob_reader = blobstore.BlobReader(blob_info.key())
        blob_iterator = BlobIterator(blob_reader)
        reader = csv.reader(blob_iterator, skipinitialspace=True, delimiter=',')
#!!!!!AYHUN !!!!!
# IMPLEMENT PARSER HERE
#object to use: csv iterator called "reader"
# Create/Stick into database
        count = 1
        big_dict = {}
        num_cols = 0
        titles = []
        for row in reader:
          #self.response.out.write(count)  
          #self.response.out.write(row)  
          if count == 1:
            num_cols = 0
            for elts in row:
                catg_list = [elts]
                big_dict[num_cols] = catg_list
                num_cols += 1
          else:
            iter_num = 0  
            for elts in row:
              big_dict[iter_num].append(elts)
              iter_num += 1
          count += 1     
        self.response.out.write(str(big_dict))   
###############SQL CODE -----> use big_dict (dictionary object) to generate SQL code
            #big_dict current format: dictionary object where key is 0-number of cols in csv file
            #value is list of values in each row, where the first element of the list is the name of column
            #use this value to create values for the attributes in database and remainder of list to fill the 
            #the data corresponding to the attribute


      logging.info('>>-----------------We have liftoff------------------------------------------------------------->>')
      logging.info(os.getenv('SERVER_SOFTWARE'))
      self.response.out.write(os.getenv('SERVER_SOFTWARE'))
      logging.info(os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/'))
      if (os.getenv('SERVER_SOFTWARE') and (os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/') or os.getenv('SERVER_SOFTWARE').startswith('Development/') )):
        self.response.out.write("HERE1")
        #db = MySQLdb.connect(unix_socket='/cloudsql/' + _INSTANCE_NAME, db='gsdmarin', user='ruifu', passwd='1234')
        db = MySQLdb.connect(host='173.194.82.159', port=3306, db='gsdmarin', user='ruifu', passwd='1234')
        self.response.out.write("HERE2")  
      else:
        self.response.out.write("HERE3")
        #Cant connect to localhost + if we fall in here we need error handling! Unacceptable.
        db = MySQLdb.connect(host='127.0.0.1', port=3306, db='gsdmarin', user='ruifu', passwd='1234')
        self.response.out.write("HERE4")  
    
            # Alternatively, connect to a Google Cloud SQL instance using:
            # db = MySQLdb.connect(host='ip-address-of-google-cloud-sql-instance', port=3306, user='root', charset='utf 8')
      cursor = db.cursor()

     ####### AYHUN!!!!!!!!
     

     ######################

####################

        #self.redirect('/parse/%s' % blob_info.key()) ### TO CALL DOWNLOAD
    except:
        logging.error('Error in Uploading/Parsing')
        self.response.out.write('Error in processing the file')

###DOWNLOADING!!!! FOR FUTURE REF.
class Parse(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, file_key):
        if not blobstore.get(file_key):
            self.error(404)
        else:
            self.send_blob(file_key)
  