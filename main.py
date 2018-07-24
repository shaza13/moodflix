import webapp2
import jinja2
import os
from models import Movie

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
        result_template = the_jinja_environment.get_template('templates/loading.html')
        self.response.write(welcome_template.render())
        mood = self.request.get('mood')
        occasion = self.request.get('occasion')


class Upload(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_environment.get_template('templates/loading.html')
        shrek = Movie(title='Shrek', duration=123, rating=10, description='About an ogre who lives in a swamp.', mood='casual, silly', occasion='kids, family')
        shrek_key = shrek.put()
        thor = Movie(title='Thor: Ragnarok', duration=130, rating=8, description='Thor is imprisoned on the planet Sakaar, and must race against time to return to Asgard and stop Ragnarök, the destruction of his world, at the hands of the powerful and ruthless villain Hela.', mood='humorous, cheerful', occasion='feeling super, casual')
        thor_key = thor.put()
        # self.response.write(welcome_template.render())
        self.redirect("/result")


class ResultPage(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_environment.get_template('templates/result.html')
        mood = self.request.get("mood")
        occasion = self.request.get("occasion")
        movie_query = Movie.query()
        all_movies = movie_query.fetch()
        movie_dic = {
            "movies": all_movies
        }
        self.response.write(welcome_template.render(movie_dic))
        # if mood == "casual":
        #     return Shrek


    def post(self):
        result_template = the_jinja_environment.get_template('templates/result.html')
        self.response.write(result_template.render())









app = webapp2.WSGIApplication([
    ('/', WelcomePage),
    ('/loading', Upload),
    ('/result', ResultPage),
], debug=True)
