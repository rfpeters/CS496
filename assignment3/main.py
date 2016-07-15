import webapp2

app = webapp2.WSGIApplication([], debug=True)
app.router.add(webapp2.Route(r'/shelter/<id:[0-9]>', 'shelter.Shelter'))
app.router.add(webapp2.Route(r'/cat/<id:[0-9]>', 'cat.Cat'))