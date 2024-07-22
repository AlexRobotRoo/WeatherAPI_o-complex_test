import unittest
from app import app, db
from app.models import SearchHistory

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_weather_search(self):
        response = self.app.post('/', data=dict(city='London'))
        self.assertIn(b'Weather for London', response.data)

if __name__ == '__main__':
    unittest.main()