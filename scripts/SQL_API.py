import MySQLdb
import urllib
import jinja2
import os
import urllib
import cgi
import csv
import StringIO
import string
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import webapp
from google.appengine.ext import blobstore
from google.appengine.ext import db
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import ndb

from google.appengine.api import users
import webapp2
import logging

class call_method(webapp2.RequestHandler):
  def post(self):
    try:
      func = self.request.get('func')
      name = self.request.get('name')
      attribute = self.request.get('attribute')
      _id_ = self.request.get('_id_')
      entity = self.request.get('entity')

      # AYHUN: Senin inputlarindan bir tek burada dict yok, onun icin farkli bir debugging dusuneblirsn.
      #       Input variable adlari yukarida tanimli, kulanman icin..

      self.response.out.write('Method to Call: %s <br>' % (func))
      self.response.out.write('Name of Table:  %s <br>' % (name))
      self.response.out.write('Attribute:      %s <br>' % (attribute))
      self.response.out.write('ID:             %s <br>' % (_id_))
      self.response.out.write('Entity:         %s <br>' % (entity))
      
      possibles = globals().copy()
      possibles.update(locals())
      method = possibles.get(func)
      # self.response.out.write(method)
      if not method:
        self.response.out.write('Not a Valid Method Name')
      elif func == 'AddEntity':
        self.response.out.write('Parameter of AddEntity is given by hand')
        AddEntity("aaaaaa","bbbbbbbbb", "sdfsdfasd")
      else:
        self.response.out.write('method output:<br>' + string.replace(str(method(name)),'\n','<br>'))         
    except:
      logging.error('Error in getting/running correct func')
      self.response.out.write('Error in getting/running correct func')

# test edecgn fonksyonu maalesf burya kopyla yapistr :)
def CreateTable(name):
  sql = 'CREATE TABLE `gsdmarin`.`%s` ( `ID` INT NOT NULL AUTO_INCREMENT, PRIMARY KEY (`ID`));' % name
  db = ConnectToDB()

  logging.info('Creating.. Table Name: %s' % (name))
  
  cursor = db.cursor()
  try:
    cursor.execute(sql)
  except:
    logging.info("Something went wrong nigga")
    return 0;
    
  logging.info('Creation complete...')
  logging.info('SQL:\n' + sql)
  
  cursor.close()
  db.close()
  return 1

def PrintTable(name):
  sql = "SELECT * FROM `gsdmarin`.`%s`" % name
  db = ConnectToDB()
  cursor = db.cursor()
  
  try:
    cursor.execute(sql)
  except:
    logging.info('sictik:' + sql)
    return 0
  
  num_fields = len(cursor.description)
  field_names = [i[0] for i in cursor.description]
  
  res = []
  res.append(str(field_names))  
  for row in cursor.fetchall():
    res.append(', '.join(str(e) for e in row) )
  
  stringRepresentation = '\n'.join(res) 
  logging.info('String representation of the queried table:\n' + stringRepresentation)
  
  cursor.close()
  db.close()
  return stringRepresentation
  
def RemoveTable(name):
  sql = "DROP TABLE `gsdmarin`.`%s`;" % name
  db = ConnectToDB()
  cursor = db.cursor()
  
  try:
    cursor.execute(sql)
  except:
    logging.info('sictik:' + sql)
    return 0
  cursor.close()
  db.close()
  return 1

def AddEntity(name,  *args):
  if len(args) > 0
    dict = args[0]
  else 
    dict = None
    
  logging.info("oldu")
  logging.info(name)
  return "method is not written yet"
  
  
def ConnectToDB():
  try:
    if (os.getenv('SERVER_SOFTWARE') and os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/')):
      logging.info("I should be running on the cloud right now 1<br>")
      db = MySQLdb.connect(host='127.0.0.1', port=3306, db='gsdmarin', user='ruifu', passwd='1234')
      logging.info("I should be running on the cloud right now 2<br>")
    else:
      logging.info("I should be running on a normal computer right now 1")
      db = MySQLdb.connect(host='173.194.82.159', port=3306, db='gsdmarin', user='ruifu', passwd='1234')
      logging.info("I should be running on a normal computer right now 2")
  except:
    logging.info("Can't connect to database")
  return db


# Ayhun Senin yazacagin ancak bir Class olacak, adi:SQL_API. Bu interfacein tek amaci senin debug/testin icin. 
# Cok kasmadim isini cat pat gorur diye, En kotu sen classni asagiya yaz normal test etmek istedgn fonksyonu 
# CreateTable orenginde oldugu gibi copy pastle, dogru argumanlri pasla debug info nu disari logla

class SQL_API:
  def CreateTable(name):
    return
