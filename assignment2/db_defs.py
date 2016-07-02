from google.appengine.ext import ndb

class Customer(ndb.Model):
	name = ndb.StringProperty(required=True)
	email = ndb.StringProperty(required=True)
	phone = ndb.IntegerProperty(required=True)
	phone_type = ndb.StringProperty(required=True)
	sports = ndb.StringProperty(repeated=True)
	