import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) #have to set the path because
#Python can't find the app package when you run pytest because it’s not in the PYTHONPATH.
import unittest
from app import create_app, db
from app.models import URL

class URLModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_url_creation(self):
        url = URL(original_url='https://example.com', short_id='abc123')
        db.session.add(url)
        db.session.commit()

        found = URL.query.filter_by(short_id='abc123').first()
        self.assertIsNotNone(found)
        self.assertEqual(found.original_url, 'https://example.com')

    def test_generate_short_id_unique(self):
        ids = set()
        for _ in range(100):
            sid = URL.generate_short_id()
            self.assertNotIn(sid, ids)
            ids.add(sid)

if __name__ == '__main__':
    unittest.main()