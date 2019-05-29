import unittest
from app.models import Pitch


id = db.Column(db.Integer, primary_key = True)
    pitch_id = db.Column(db.Integer)
    title = db.Column(db.String(255))
    content = db.Column(db.String)
    category = db.Column(db.String())
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class TestUser(unittest):
    def setUp(self):
        self.new_pitch = Pitch(title='Concerts', downvote=0, upvote=0,content="What if you did not have to...", id=1, category="Events", pitch_id=1,)

    def tearDown(self):
        User.query.delete()
        
    def test_instance_initialization(self):
        self.assertEquals(self.new_pitch.title, 'Graphic Designer')
        self.assertEquals(self.new_pitch.body, 'Hi, I\'m Molly, so nice to meet you!...')
        self.assertEquals(self.new_pitch.posted_at, '2019-05-27 14:15:43.587649')
        self.assertEquals(self.new_pitch.id, '1')
        self.assertEquals(self.new_category, 'Elevator')
    

if __name__ == "__main__":
    unittest.main()