from google.appengine.ext import ndb

class Customer(ndb.Model):
	name = ndb.StringProperty(required=True)
	email = ndb.StringProperty(required=True)
	password = ndb.StringProperty(required=True)
	phone = ndb.StringProperty(required=True)
	phone_type = ndb.StringProperty(required=True)
	sports = ndb.KeyProperty(repeated=True)
	
class Sports(ndb.Model):
	name = ndb.StringProperty(required=True)
	