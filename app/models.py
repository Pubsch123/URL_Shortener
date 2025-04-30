from . import db
import string, random

class URL(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    original_url = db.Column(db.String(512), nullable = False)
    short_id = db.Column(db.String(6), unique = True, nullable = False)


    @staticmethod
    def generate_short_id(num_chars = 6):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=num_chars))
    