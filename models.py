from google.appengine.ext import ndb

class Recommendation(ndb.model):
    mood = ndb.StringProperty()
    occasion = ndb.StringProperty()
    
