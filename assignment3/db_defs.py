#Ryan Peters
#07/16/16
#Definitions for database entities.  Overrides to_dict() so entities
#can be converted to JSON

from google.appengine.ext import ndb

class Model(ndb.Model):
	def to_dict(self):
		d = super(Model, self).to_dict()
		d['key'] = self.key.id()
		return d

class Shelter(Model):
	name = ndb.StringProperty(required=True)
	phone = ndb.StringProperty(required=True)
	address = ndb.StringProperty(required=True)
	city = ndb.StringProperty(required=True)
	state = ndb.StringProperty(required=True)
	zip = ndb.StringProperty(required=True)
	
class Dog(Model):
	name = ndb.StringProperty(required=True)
	breed = ndb.StringProperty(required=True)
	age = ndb.StringProperty(required=True)
	arrival = ndb.DateProperty(auto_now_add=True)
	shelter = ndb.KeyProperty()
	
	def to_dict(self):
		d = super(Dog, self).to_dict()
		d['arrival'] = self.arrival.strftime('%m/%d/%Y')
		if self.shelter:
			d['shelter'] = self.shelter.id()
		return d
	
class Cat(Model):
	name = ndb.StringProperty(required=True)
	breed = ndb.StringProperty(required=True)
	age = ndb.StringProperty(required=True)
	arrival = ndb.DateProperty(auto_now_add=True)
	shelter = ndb.KeyProperty()
	
	def to_dict(self):
		c = super(Cat, self).to_dict()
		c['arrival'] = self.arrival.strftime('%m/%d/%Y')
		if self.shelter:
			c['shelter'] = self.shelter.id()
		return c
	