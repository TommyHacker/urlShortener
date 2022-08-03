from app import db


class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    old_url = db.Column(db.String(100), unique=True, nullable=False)
    new_url = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"Urls('{self.old_url}', '{self.new_url}')"