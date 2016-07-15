from google.appengine.ext import ndb

class Shelter(ndb.Model):
	name = ndb.StringProperty()
	phone = ndb.StringProperty()
	address = ndb.StringProperty()
	city = ndb.StringProperty()
	state = ndb.StringProperty()
	zip = ndb.KeyProperty()
	
class Dog(ndb.Model):
	name = ndb.StringProperty(required=True)
	breed = ndb.StringProperty(required=True)
	age = ndb.StringProperty(required=True)
	arrival = ndb.DateProperty(auto_now_add=True)
	shelter = ndb.KeyProperty()
	
class Cat(ndb.Model):
	name = ndb.StringProperty(required=True)
	breed = ndb.StringProperty(required=True)
	age = ndb.StringProperty(required=True)
	arrival = ndb.DateProperty(auto_now_add=True)
	shelter = ndb.KeyProperty()