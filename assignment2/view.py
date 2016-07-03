import webapp2
import base_page
from google.appengine.ext import ndb
import db_defs

class View(base_page.BaseHandler):
	def __init__(self, request, response):
		self.initialize(request, response)
		self.template_values = {}
		
	def get(self):
		customer_key = ndb.Key(urlsafe=self.request.get('key'))
		customer = customer_key.get()
		self.template_values['key'] = self.request.get('key')
		self.template_values['name'] = customer.name
		self.template_values['email'] = customer.email
		self.template_values['password'] = customer.password
		self.template_values['phone'] = customer.phone
		self.template_values['phone_type'] = customer.phone_type
		sports = db_defs.Sports.query(ancestor=ndb.Key(db_defs.Sports, self.app.config.get('default-group'))).fetch()
		sport = []
		for s in sports:
			if s.key in customer.sports:
				sport.append({'name':s.name})
		self.template_values['sports'] = sport
		self.template_values['key'] = self.request.get('key')
		self.render('view.html', self.template_values)