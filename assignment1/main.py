import webapp2
import datetime

class MainHandler(webapp2.RequestHandler):
	def get(self):
		now = datetime.datetime.now()
		self.response.write(str(now))
		
app = webapp2.WSGIApplication([
	('/', MainHandler)
], debug=True)