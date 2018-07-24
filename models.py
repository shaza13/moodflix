from google.appengine.ext import ndb

class Movie(ndb.Model):
    title = ndb.StringProperty()
    duration = ndb.IntegerProperty()
    rating = ndb.IntegerProperty()
    description = ndb.StringProperty()
    mood = ndb.StringProperty()
    occasion = ndb.StringProperty()
