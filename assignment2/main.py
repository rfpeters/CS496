import webapp2

config = {'default-group':'base-data'}

application = webapp2.WSGIApplication([
	('/', 'index.Index'),
	('/view', 'view.View'),
	('/edit', 'edit.Edit')
], debug=True, config=config)