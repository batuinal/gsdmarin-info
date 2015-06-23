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
      value = self.request.get('entity')

      # AYHUN: Senin inputlarindan bir tek burada dict yok, onun icin farkli bir debugging dusuneblirsn.
      #       Input variable adlari yukarida tanimli, kulanman icin..

      self.response.out.write('Method to Call: %s <br>' % (func))
      self.response.out.write('Name of Table:  %s <br>' % (name))
      self.response.out.write('Attribute:      %s <br>' % (attribute))
      self.response.out.write('ID:             %s <br>' % (_id_))
      self.response.out.write('Value:         %s <br>' % (value))
      
      possibles = globals().copy()
      possibles.update(locals())
      method = possibles.get(func)
      # self.response.out.write(method)
      if not method:
        self.response.out.write('Not a Valid Method Name')
      elif func == 'AddEntityWithValues':
        self.response.out.write('Dictionary for AddEntityWithValues is given by hand')
        dict = []
        dict.append(['SHIP'])
        dict[0].append('ship1')
        dict[0].append('ship2')
        dict.append(['DATE'])
        dict[1].append('1991-12-21')
        dict[1].append('1010-10-10')
        dict.append(['REPORT'])
        dict[2].append('report1')
        dict[2].append('report2')
        AddEntityWithValues(name, dict)
      elif func == "AddAttribute":
        AddAttribute(name, attribute, "VARCHAR(100)")
      elif func == "RemoveAttribute":
        RemoveAttribute(name, attribute)
      elif func == "RemoveEntity":
        RemoveEntity(name, _id_)
      elif func == "SetValue":
        SetValue(name, _id_, attribute, value)
      elif func == "GetValue":
        GetValue(name,_id_,attribute)
      elif func == "SetAllEntities":
        SetAllEntities(name, attribute, value)
      elif func == "SetAllAttributes":
        dict = []
        dict.append(['pay'])
        dict[0].append('11')
        dict.append(['day'])
        dict[1].append('21')
        SetAllAttributes(name, _id_, dict)
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
  
def ListEntities(name):
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
  entities = []
  for f in field_names:
    entities.append([f])
  
  for row in cursor.fetchall():
    i=0
    for ele in row:
      entities[i].append(ele)
      i += 1
  
  print entities
  return entities
      
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

def AddEntity(name):
  sql = "SELECT * FROM `gsdmarin`.`%s` LIMIT 1" % name
  db = ConnectToDB()
  cursor = db.cursor()
  try:
    cursor.execute(sql)
  except:
    logging.info('sictik:' + sql)
    return 0
  
  nulls = "null"
  num_fields = len(cursor.description)-1
  while num_fields > 0:
    num_fields-=1
    nulls += ',null'
  sql = "INSERT INTO `gsdmarin`.`%s` VALUES(%s);" % (name, nulls)
  
  try:
    cursor.execute(sql)
    db.commit()
  except:
    logging.info('sictik:' + sql)
    return 0
  
  cursor.close()
  db.close()
  return cursor.lastrowid

def AddEntityWithValues(name, dict):
  db = ConnectToDB()
  db.autocommit(False) # start transaction
  cursor = db.cursor()
  try:
    for row in range(1,len(dict[0])):  
      sql = []
      sql.append("INSERT INTO `gsdmarin`.`%s` (" % name)
      for col in range(0,len(dict)-1):
        sql.append("`%s`," % dict[col][0])
      sql.append("`%s`)" % dict[len(dict)-1][0])
      sql.append("VALUES (")    
      for col in range(0,len(dict) - 1):
        sql.append("'%s'," % dict[col][row])
      sql.append("'%s' );" % dict[len(dict) - 1][row])
      print "----\n%s\n----" % ' '.join(sql)
      cursor.execute(' '.join(sql))
    db.commit()
  except:
    db.rollback()
    print "make sure that the column names are exactly the same as the column names in the real table"
    return 0

  cursor.close()
  db.close()
  return cursor.lastrowid

def AddAttribute(name, attribute, type):
  db = ConnectToDB()
  cursor = db.cursor()
  
  sql = "ALTER TABLE `gsdmarin`.`%s` ADD COLUMN `%s` %s NULL ;" % (name,attribute, type)
  print sql
  
  try:
    cursor.execute(sql)
    db.commit()
  except:
    print "sictik ki ne sictikkk"
    return 0
  cursor.close()
  db.close()  
  return 1

def RemoveAttribute(name, attribute):
  db = ConnectToDB()
  cursor = db.cursor()
  
  sql = "ALTER TABLE `gsdmarin`.`%s` DROP COLUMN `%s`;" % (name, attribute)

  try:
    cursor.execute(sql)
    db.commit()
  except:
    print "sictik ki ne sictikkk"
    print sql
    return 0
  
  cursor.close()
  db.close()
  return 1

def RemoveEntity(name, id):
  db = ConnectToDB()
  cursor = db.cursor()
  
  sql = "DELETE FROM `gsdmarin`.`%s` WHERE ID = %s;" % (name, id)
  
  try:
    cursor.execute(sql)
    db.commit()
  except:
    print "sictik ki ne sictikkk"
    print sql
    return 0
  
  cursor.close()
  db.close()  
  return 1  
  
def GetValue(table, id, attribute):
  sql = "SELECT `%s` FROM `gsdmarin`.`%s` WHERE ID = '%s';" % (attribute, table, id)
  db = ConnectToDB()
  cursor = db.cursor()
  
  try:
    cursor.execute(sql)
  except:
    logging.info('sictik:' + sql)
    return 0  
  
  for row in cursor.fetchall():
    res = row[0]
  
  cursor.close()
  db.close()
  return res
  
def SetValue(table, id, attribute, value):
  db = ConnectToDB()
  cursor = db.cursor()
  sql = "UPDATE `gsdmarin`.`%s` SET `%s`='%s' WHERE `ID`='%s';" % (table,attribute,value,id)

  try:
    cursor.execute(sql)
    db.commit()
  except:
    print "sictik ki ne sictikkk"
    print sql
    return 0
  
  cursor.close()
  db.close()  
  return 1 

def SetAllEntities(table, attribute, value):
  db = ConnectToDB()
  cursor = db.cursor()
  sql = "UPDATE `gsdmarin`.`%s` SET `%s`='%s' WHERE `ID` > '0';" % (table, attribute, value)
  try:
    cursor.execute(sql)
    db.commit()
  except:
    print "sictik ki ne sictikkk"
    print sql
    return 0
  
  cursor.close()
  db.close()  
  return 1 

def SetAllAttributes(table, id, dict):
  sql = "UPDATE `gsdmarin`.`%s`" % table
  sql = [sql]
  sql.append("SET")
  middle = []
  for i in range(0,len(dict)):
    middle.append("`%s` = '%s'" % (dict[i][0],dict[i][1]))
  sql.append(', '.join(middle))
  sql.append("WHERE ID = %s;" % id)
  
  sql = ' '.join(sql)
  print sql
  db = ConnectToDB()
  cursor = db.cursor()
  try:
    cursor.execute(sql)
    db.commit()
  except:
    print "sictik ki ne sictikkk"
    print sql
    return 0
  
  cursor.close()
  db.close()  
  return 1
    
  
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
