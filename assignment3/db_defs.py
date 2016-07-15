from google.appengine.ext import ndb

class Shelter(ndb.Model):
	name = ndb.StringProperty(required=True)
	phone = ndb.StringProperty(required=True)
	address = ndb.StringProperty(required=True)
	city = ndb.StringProperty(required=True)
	state = ndb.StringProperty(required=True)
	zip = ndb.KeyProperty(repeated=True)
	
class Dog(ndb.Model):
	name = ndb.StringProperty(required=True)
	breed = ndb.StringProperty(required=True)
	age = ndb.StringProperty(required=True)
	arrival = ndb.DateProperty(auto_add_now=True)
	shelter = ndb.KeyProperty()
	
class Cat(ndb.Model):
	name = ndb.StringProperty(required=True)
	breed = ndb.StringProperty(required=True)
	age = ndb.StringProperty(required=True)
	arrival = ndb.DateProperty(auto_add_now=True)
	shelter = ndb.KeyProperty()