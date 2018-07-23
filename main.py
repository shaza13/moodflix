import webapp2
import jinja2
import os
# from models import Recommendation

mood = ""
occasion = ""



the_jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = [],
    autoescape = True)

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_environment.get_template('templates/welcome.html')
        self.response.write(welcome_template.render())

    def post(self):
        result_template = the_jinja_environment.get_template('templates/result.html')
        self.response.write(welcome_template.render())
        mood = self.request.get('mood')
        occasion = self.request.get('occasion')


class ResultPage(webapp2.RequestHandler):
    def get():
        welcome_template = the_jinja_environment.get_template('templates/result.html')
        self.response.write(welcome_template.render())

        Recommendation.mood = mood
        Recommendation.occasion = occasion



    def post():
        result_template = the_jinja_environment.get_template('templates/result.html')
        self.response.write(result_template.render())









app = webapp2.WSGIApplication([
    ('/', WelcomePage),
    ('/result', ResultPage),
], debug=True)
