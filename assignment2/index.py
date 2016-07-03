import webapp2
import base_page
from google.appengine.ext import ndb
import db_defs

class Index(base_page.BaseHandler):	
	def __init__(self, request, response):
		self.initialize(request, response)
		self.template_values = {}
		self.phone_types = []
		self.phone_types.append({'name':'home', 'checked':True})
		self.phone_types.append({'name':'work', 'checked':False})
		self.phone_types.append({'name':'cell', 'checked':False})
		
	def render(self, page):
		self.template_values['customers'] = [{'name':x.name, 'key':x.key.urlsafe()} for x in db_defs.Customer.query(ancestor=ndb.Key(db_defs.Customer, self.app.config.get('default-group'))).fetch()]
		self.template_values['sports'] = [{'name':x.name, 'key':x.key.urlsafe(), 'checked':False} for x in db_defs.Sports.query(ancestor=ndb.Key(db_defs.Sports, self.app.config.get('default-group'))).fetch()]
		self.template_values['phone_type'] = self.phone_types
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
			cust.sports = [ndb.Key(urlsafe=x) for x in self.request.get_all('sports[]')]
			cust.put()
		elif action == 'add_sport':
			k = ndb.Key(db_defs.Sports, self.app.config.get('default-group'))
			sport = db_defs.Sports(parent=k)
			sport.name = self.request.get('sport_input')
			sport.put()
		elif action == 'edit_customer':
			cust_key = ndb.Key(urlsafe=self.request.get('key'))
			cust = cust_key.get()
			cust.name = self.request.get('name_input')
			cust.email = self.request.get('email_input')
			cust.password = self.request.get('password_input')
			cust.phone = self.request.get('phone_input')
			cust.phone_type = self.request.get('phone_type')
			cust.sports = [ndb.Key(urlsafe=x) for x in self.request.get_all('sports[]')]
			cust.put()
		self.render('index.html')