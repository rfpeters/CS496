import webapp2
import base_page
from google.appengine.ext import ndb
import db_defs

class Index(base_page.BaseHandler):
	def __init__(self, request, response):
		self.initialize(request, response)
		self.template_values = {}
		
	def render(self, page):
		self.template_values['customers'] = [{'name':x.name, 'key':x.key.urlsafe()} for x in db_defs.Customer.query(ancestor=ndb.Key(db_defs.Customer, self.app.config.get('default-group'))).fetch()]
		base_page.BaseHandler.render(self, page, self.template_values)
	
	def get(self):
		self.render('index.html')
		
	def post(self):
		action = self.request.get('action')
		if action == 'add_customer':
			k = ndb.Key(db_defs.Customer, self.app.config.get('default-group'))
			cust = db_defs.Customer(parent=k)
			cust.name = self.request.get('name_input')
			cust.email = self.request.get('email_input')
			cust.password = self.request.get('password_input')
			cust.phone = self.request.get('phone_input')
			cust.phone_type = self.request.get('phone_type')
			cust.put()
		self.render('index.html')