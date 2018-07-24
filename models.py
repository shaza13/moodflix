from google.appengine.ext import ndb

class Movie(ndb.Model):
    title = ndb.StringProperty()
    duration = ndb.IntegerProperty()
    rating = ndb.IntegerProperty()
    description = ndb.StringProperty()
    mood = ndb.StringProperty()

shrek = Movie(
    title='Shrek', duration=123, rating=10, description='About an ogre who lives in a swamp.', mood='casual, silly')

shrek_key = shrek.put()
