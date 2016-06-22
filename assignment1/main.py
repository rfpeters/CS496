import os
import webapp2
import datetime
from google.appengine.ext.webapp import template

class MainHandler(webapp2.RequestHandler):
	def get(self):
		now = datetime.datetime.now()		
		template_values = {'time': now}
		
		path = os.path.join(os.path.dirname(__file__), 'index.html')
		self.response.write(template.render(path, template_values))
		
app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)