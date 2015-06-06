import logging
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
<<<<<<< Updated upstream
    logging.info('>>-----------------We have liftoff------------------------------------------------------------->>')
    logging.info(os.getenv('SERVER_SOFTWARE'))
    if (os.getenv('SERVER_SOFTWARE') and (os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/') or os.getenv('SERVER_SOFTWARE').startswith('Development/') )):
          db = MySQLdb.connect(host='173.194.82.159', port=3306, db='gsdmarin', user='ruifu', passwd='1234')
    else:
          db = MySQLdb.connect(host='127.0.0.1', port=3306, db='gsdmarin', user='ruifu', passwd='1234')
    
            # Alternatively, connect to a Google Cloud SQL instance using:
            # db = MySQLdb.connect(host='ip-address-of-google-cloud-sql-instance', port=3306, user='root', charset='utf 8')
    cursor = db.cursor()
    
    # Assuming we managed to get file name (which will be used as table name) and file content as a 2d array
    FILE_NAME = "EMPLOYEE"
    FILE_CONTENT = []
    FILE_CONTENT.append(['FIRST_NAME', 'LAST_NAME', 'AGE', 'SEX', 'INCOME'])
    FILE_CONTENT.append(['Ayhun', 'Tekat', '123', 'm', '456'])
    # -----------------------------------------------------------------------------------------------------
    
    # print file name and content to console, just for seeing it
    logging.info('File name:')
    logging.info(FILE_NAME)
    logging.info('File content:')
    logging.info(FILE_CONTENT)
    # query the 'information_schema' to see if a table that has the 'file_name' as its name exists
    table_exists = False
    sql = "SELECT * FROM information_schema.tables WHERE table_name = '%s'" % FILE_NAME
    logging.info("query:" + sql)
    logging.info("result:")
    cursor.execute(sql)
    for row in cursor.fetchall():
          table_exists = True
          
          logging.info( ' '.join(str(e) for e in row)) 

    if table_exists:
          logging.info("Table %s already exists." % FILE_NAME)
          logging.info("**********Database before insertion:")    
          sql = "SELECT * FROM gsdmarin.%s" % FILE_NAME
          cursor.execute(sql)
          for row in cursor.fetchall():
                logging.info( ' '.join(str(e) for e in row) )

          # TODO: insert to existing table here
          sql = []
          sql.append("INSERT INTO `gsdmarin`.`%s`" % FILE_NAME)
          sql.append("(`%s`," % FILE_CONTENT[0][0])
          for i in range(1,len(FILE_CONTENT[0])-1):
                sql.append("`%s`," % FILE_CONTENT[0][i])
          sql.append("`%s`)" % FILE_CONTENT[0][len(FILE_CONTENT[0]) - 1])
          sql.append("VALUES")
          
#VALUES
#(<{FIRST_NAME: }>,
#<{LAST_NAME: }>,
#<{AGE: }>,
#<{SEX: }>,
#<{INCOME: }>);
          logging.info("insertion query(not complete yet):\n" + '\n'.join(sql))
          # end of insertion

          logging.info("**********Database after insertion:")    
          sql = "SELECT * FROM gsdmarin.%s" % FILE_NAME
          cursor.execute(sql)
          for row in cursor.fetchall():
                logging.info( ' '.join(str(e) for e in row) )

    else:
          logging.info('Table %s does not exist. Create it' % FILE_NAME)
          # TODO: table creation code 

   

    
    db.close()
    logging.info('<<------------------------Everything went well?------------------------------------------------<<')
    return
=======
    self.redirect('/pages/parser/upload.html')

class Parse(webapp2.RequestHandler):
  def post(self):
    
    #self.response.write(cgi.escape(self.request.get('xlfile')))
    #content = 
    self.response.out.write(cgi.escape(self.request.get('xlfile')))




    #content = self.request.POST.get('file').file.read()
     # logging.info(content)
      #self.response.out.write(content)
   # name = self.request.get('searchbox') # this will get the value from the field named username
    #self.response.write(name)
        

    #form = cgi.FieldStorage()
    #seachterm =  form.getvalue('searchbox')
    #a = 2
    #self.response.write('<html><body><h1> %s </h1></body></html>' % seachterm)
    
		 # Display existing guestbook entries and a form to add new entries.
    #db = MySQLdb.connect(host='173.194.82.159', port=3306, db='gsdmarin', user='ruifu', passwd='1234')
            # Alternatively, connect to a Google Cloud SQL instance using:
            # db = MySQLdb.connect(host='ip-address-of-google-cloud-sql-instance', port=3306, user='root', charset='utf 8')
    #cursor = db.cursor()
    #cursor.execute(sql)
    #db.close()

>>>>>>> Stashed changes

		#return self.redirect('/pages/parser/upload.html')
