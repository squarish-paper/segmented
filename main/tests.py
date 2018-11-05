from django.test import TestCase, Client

from main import views
from main import models
#from main.views import index

class ModelsTest(TestCase):

    def test_athlete_string_representation(self):
        athlete = models.Athlete(strava_id=118515,first_name="Jim",last_name="Jones")
        self.assertEqual(str(athlete), "Jim Jones")

    def test_segment_string_representation(self):
        segment = models.Segment(segment_id=18150,name="LONG HILL SECTION",distance=150)
        self.assertEqual(str(segment), "18150 LONG HILL SECTION")

class ViewsTests(TestCase):
    def setUp(self):
        client = Client()

    def test_index(self):
        client = Client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, "index.html")

#    def test_connect(self):
#        client = Client()
#        response = client.get("/connect")
#        self.assertEqual(response.status_code, 200)
#        self.assertEqual(response.templates.name, "connect.html")

#    def test_private(self):
#        client = Client()
#        response = client.get("/private")
#        self.assertEqual(response.status_code, 200)
#        self.assertEqual(response.templates[0].name, "private.html")
