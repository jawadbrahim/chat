from database.postgres import db

class Orm:
 def add (self,obj):
    db.session.add(obj)

 def commit(self):
  db.session.commit()