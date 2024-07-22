from . import db

class SearchHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100), nullable=False)
    search_count = db.Column(db.Integer, default=1)