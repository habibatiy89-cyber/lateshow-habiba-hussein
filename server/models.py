from server.extensions import db

class Show(db.Model):
    __tablename__ = "shows"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(50))
    location = db.Column(db.String(120))

    def __repr__(self):
        return f"<Show {self.id} - {self.title}>"
