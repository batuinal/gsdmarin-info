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

class call_method(webapp2.RequestHandler):
  def post(self):
    try:
      func = self.request.get('func')
      name = self.request.get('name')
      attribute = self.request.get('attribute')
      _id_ = self.request.get('_id_')
      entity = self.request.get('entity')

      #AYHUN: Senin inputlarindan bir tek burada dict yok, onun icin farkli bir debugging dusuneblirsn.
      #       Input variable adlari yukarida tanimli, kulanman icin..

      self.response.out.write('Method to Call: %s <br>' % (func))
      self.response.out.write('Name of Table:  %s <br>' % (name))
      self.response.out.write('Attribute:      %s <br>' % (attribute))
      self.response.out.write('ID:             %s <br>' % (_id_))
      self.response.out.write('Entity:         %s <br>' % (entity))
      
      possibles = globals().copy()
      possibles.update(locals())
      method = possibles.get(func)
      #self.response.out.write(method)
      if not method:
        self.response.out.write('Not a Valid Method Name')
      else:
        #AYHUN: Method senin yazdigin SQL_API icindeki cagirdgn method, icine dogru inputlari sadece feed et diger test edecegin fonksyonlar icin
        method(name) 
    except:
      logging.error('Error in getting/running correct func')
      self.response.out.write('Error in getting/running correct func')

#test edecgn fonksyonu maalesf burya kopyla yapistr :)
def CreateTable(name):
  #Yazdigin Functionda birtek log edebilrsn cunku disardn cagirdgn bir function icin "self" kelimesni kulanmzsn, python patlar
  logging.info('Created Table Name: %s' % (name))

#Ayhun Senin yazacagin ancak bir Class olacak, adi:SQL_API. Bu interfacein tek amaci senin debug/testin icin. 
#Cok kasmadim isini cat pat gorur diye, En kotu sen classni asagiya yaz normal test etmek istedgn fonksyonu 
# CreateTable orenginde oldugu gibi copy pastle, dogru argumanlri pasla debug info nu disari logla

class SQL_API:
  def CreateTable(name):
    return