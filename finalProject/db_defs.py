#Definitions for database entities.  Overrides to_dict() so entities
#can be converted to JSON

from google.appengine.ext import ndb

class Model(ndb.Model):
	def to_dict(self):
		d = super(Model, self).to_dict()
		d['key'] = self.key.id()
		return d

class User(Model):
	name = ndb.StringProperty(required=True)
	email = ndb.StringProperty(required=True)
	password = ndb.StringProperty(required=True)
	
class Pokemon(Model):
	name = ndb.StringProperty(required=True)
	lat = ndb.StringProperty(required=True)
	long = ndb.StringProperty(required=True)
	caught = ndb.DateProperty(auto_now_add=True)
	user = ndb.KeyProperty()
	
	def to_dict(self):
		d = super(Pokemon, self).to_dict()
		d['caught'] = self.caught.strftime('%m/%d/%Y')
		if self.user:
			d['user'] = self.user.id()
		return d
	