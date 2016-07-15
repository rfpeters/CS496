from google.appengine.ext import ndb

class Shelter(ndb.Model):
	name = ndb.StringProperty(required=True)
	phone = ndb.StringProperty(required=True)
	address = ndb.StringProperty(required=True)
	city = ndb.StringProperty(required=True)
	state = ndb.StringProperty(required=True)
	zip = ndb.StringProperty(required=True)
	dogs = ndb.KeyProperty()
	cats = ndb.KeyProperty()
	
class Dog(ndb.Model):
	name = ndb.StringProperty(required=True)
	breed = ndb.StringProperty(required=True)
	age = ndb.StringProperty(required=True)
	arrival = ndb.DateProperty(auto_now_add=True)
	
	def to_dict(self):
		d = super(Dog, self).to_dict()
		d['arrival'] = d.arrival.strftime('%m/%d/%Y')
		return d
	
class Cat(ndb.Model):
	name = ndb.StringProperty(required=True)
	breed = ndb.StringProperty(required=True)
	age = ndb.StringProperty(required=True)
	arrival = ndb.DateProperty(auto_now_add=True)
	