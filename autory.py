from main import db  # Import db prenesený do modulu autory

class Author(db.Model):
    __tablename__ = "authors"

    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text)