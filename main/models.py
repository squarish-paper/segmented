from django.db import models

class Athlete(models.Model):
    strava_id = models.IntegerField()
    first_name = models.TextField()
    last_name = models.TextField()
    auth_date = models.DateTimeField("date authed", auto_now_add=True)
    last_logon_date = models.DateTimeField("last logon")
    bearer = models.TextField()
    public = models.BooleanField()
    picture_url = models.TextField()
    user_name = models.TextField()

class Activities(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    activity_id = models.IntegerField()

class Segment(models.Model):
    segment_id = models.IntegerField()
    name = models.TextField()
    distance = models.IntegerField()
    elevation = models.IntegerField()
    type = models.TextField()
    total_efforts = models.IntegerField()
    total_athletes = models.IntegerField()
    top_time = models.IntegerField()
    tenth_time = models.IntegerField()
    refresh_date = models.DateTimeField("date refreshed", auto_now_add=True)

class Efforts(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    segment = models.ForeignKey(Segment, on_delete=models.CASCADE)
    pb = models.IntegerField()
    efforts = models.IntegerField()
    rank = models.IntegerField()
