import webapp2
import jinja2
import os
from models import Movie




the_jinja_environment = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions = [],
    autoescape = True)

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_environment.get_template('templates/welcome.html')
        self.response.write(welcome_template.render())
        print("welcomeget")

    def post(self):
        print("WelcomePost")
        mood = self.request.get('mood')
        occasion = self.request.get('occasion')
        result_template = the_jinja_environment.get_template('templates/loading.html')
        self.response.write(welcome_template.render())



# class Upload(webapp2.RequestHandler):  # todo: not adding movies
#     def get(self):
#         welcome_template = the_jinja_environment.get_template('templates/loading.html')
#         mood = self.request.get('mood')
#         occasion = self.request.get('occasion')
#         print("uploadget")
#         print(mood)
#         print(occasion)
#         shrek = Movie(title='Shrek', duration=123, rating=10, description='About an ogre who lives in a swamp.', mood='humorous', occasion='Family Night')
#         shrek_key = shrek.put()
#         thor = Movie(title='Thor: Ragnarok', duration=130, rating=8, description='Thor is imprisoned on the planet Sakaar, and must race against time to return to Asgard and stop Ragnarok, the destruction of his world, at the hands of the powerful and ruthless villain Hela.', mood='humorous, cheerful', occasion='Casual Watching')
#         thor_key = thor.put()
#         wake = Movie(title='Before I wake', duration=97, rating=6, description='A couple adopt an orphaned child whose dreams - and nightmares - manifest physically as he sleeps.', mood='gloomy', occasion='halloween based')
#         wake_key = wake.put()
#         santa = Movie(title='Santa Buddies', duration=88, rating=5, description='At the North Pole, Santa Claus (Father Christmas) and his chief dog Santa Paws worry as the whole toy processing system is threatened by the weakening of its magical power source, the icicle drawing on Christmas spirit.', mood='cheerful', occasion='Christmas')
#         pounds = Movie(title='Seven Pounds', duration=123, rating=8, description='A man with a fateful secret embarks on an extraordinary journey of redemption by forever changing the lives of seven strangers.', mood='inspirational', occasion='Casual Watching')
#         self.response.write(welcome_template.render())
#
#     def post(self):
#         mood = self.request.get('mood')
#         occasion = self.request.get('occasion')
#         result_template = the_jinja_environment.get_template('templates/result.html')
#         self.response.write(result_template.render())

class ResultPage(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_environment.get_template('templates/result.html')
        mood = self.request.get("mood")
        occasion = self.request.get("occasion")
        print("Resultget")
        print(mood)
        print(occasion)
        movie_query = Movie.query()
        all_movies = movie_query.fetch()
        rec_movies = []
        for movie in all_movies:
            if (movie.mood in mood) and (movie.occasion in occasion):
                rec_movies.append(movie)
        movie_dic = {
            "movies": rec_movies
        }
        self.response.write(welcome_template.render(movie_dic))


    def post(self):
        print("Resultpost")
        mood = self.request.get("mood")
        occasion = self.request.get("occasion")
        shrek = Movie(title='Shrek', duration=123, rating=10, description='About an ogre who lives in a swamp.', mood='humorous', occasion='Family Night')
        shrek_key = shrek.put()
        thor = Movie(title='Thor: Ragnarok', duration=130, rating=8, description='Thor is imprisoned on the planet Sakaar, and must race against time to return to Asgard and stop Ragnarok, the destruction of his world, at the hands of the powerful and ruthless villain Hela.', mood='humorous, cheerful', occasion='Casual Watching')
        thor_key = thor.put()
        wake = Movie(title='Before I wake', duration=97, rating=6, description='A couple adopt an orphaned child whose dreams - and nightmares - manifest physically as he sleeps.', mood='gloomy', occasion='halloween based')
        wake_key = wake.put()
        santa = Movie(title='Santa Buddies', duration=88, rating=5, description='At the North Pole, Santa Claus (Father Christmas) and his chief dog Santa Paws worry as the whole toy processing system is threatened by the weakening of its magical power source, the icicle drawing on Christmas spirit.', mood='cheerful', occasion='Christmas')
        pounds = Movie(title='Seven Pounds', duration=123, rating=8, description='A man with a fateful secret embarks on an extraordinary journey of redemption by forever changing the lives of seven strangers.', mood='inspirational', occasion='Casual Watching')
        movie_query = Movie.query()
        all_movies = movie_query.fetch()
        rec_movies = []
        for movie in all_movies:
            if (movie.mood in mood) and (movie.occasion in occasion):
                rec_movies.append(movie)
        movie_dic = {
            "movies": rec_movies
        }
        result_template = the_jinja_environment.get_template('templates/result.html')
        self.response.write(result_template.render(movie_dic))




app = webapp2.WSGIApplication([
    ('/', WelcomePage),
    # ('/loading', Upload),
    ('/result', ResultPage),
], debug=True)
