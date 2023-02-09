from app.extensions import db
from datetime import datetime

# note that default users will not be added to the stats
# non-implemented stats are commented out
class Blog_Stats(db.Model):
    __tablename__ = "blog_stats"
    id = db.Column(db.Integer, primary_key=True)
    user_total = db.Column(db.Integer, default=0)
    # user_current = db.Column(db.Integer)
    # user_current_not_blocked = db.Column(db.Integer)
    # user_current_blocked = db.Column(db.Integer)
    # posts_total = db.Column(db.Integer)
    # posts_current = db.Column(db.Integer)
    # posts_approved = db.Column(db.Integer)
    comments_total = db.Column(db.Integer, default=0)


    def __repr__(self):
        return f"<Comment {self.id}: {self.text}>"
