from django.test import TestCase, RequestFactory

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

#class ViewsTests(TestCase):
#    def setUp(self):
#        self.factory = RequestFactory()
#
#    def test_index(self):
#        request = self.factory.get("/")
#        response = views.index(request)
#        self.assertEqual(response.status_code, 200)
#        print(response.templates)

#    def test_auth(self):
#        request = self.factory.get("/auth?code=123&state=456")
#        response = views.index(request)
#        self.assertRedirects(response, '/accounts/login/?next=/sekrit/')
