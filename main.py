from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://urici3i0icy8cuufham5:FrtbL6FqnCsROZMWocDBkgoOeoZC7R@b81s1xhecmfxnpmteb27-postgresql.services.clever-cloud.com:50013/b81s1xhecmfxnpmteb27"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Author(db.Model):
        __tablename__ = "authors"

        author_id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False)
        bio = db.Column(db.Text)

@app.route("/authores/", methods=['GET'])
def getAutorov():
    autor = Author.query.all()
    serialized_authors = [{"author_id": author.author_id, "name": author.name, "bio": author.bio} for author in autor]
    return jsonify(serialized_authors)
    #return autor


if __name__ == "__main__":
    app.run(debug=True)
