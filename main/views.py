import requests
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import api, datastore
from .models import Athlete

# Create your views here.
def index(request):
    return render(request, "index.html")

def auth(request):
    code = request.GET.get('code')
    state = request.GET.get('state')
    athlete = api.oauth(code,state)

    datastore.auth_user(athlete)
    return redirect('/dashboard?id='+str(athlete['athlete']['id']))

def connect(request):
    return render(request,"connect.html")

def private(request):
    return render(request,"private.html")

def dashboard(request):
    athlete_id = request.GET.get('id')
    athlete = datastore.get_user(athlete_id)

    if athlete is None:
        return render(request,"connect.html")

    if athlete.public is False:
        return render(request,"private.html")

    activities = api.get_athlete_activities(athlete.bearer,athlete.last_logon_date)
    if len(activities) > 0:
        get_sements_from_activities(athlete,activities)

    efforts = datastore.get_efforts(athlete)
    datastore.update_last_logon(athlete)

    return render(request,"dashboard.html",{"athlete": athlete, "efforts" : efforts})


def get_sements_from_activities(athlete, activities):
    for activity in activities:
        activity_id = activity["id"]
        # save xref

        detailedActivity = api.get_activity(athlete.bearer,activity_id)
        segments = detailedActivity["segment_efforts"]

        for segment in segments:
            segment_id = segment["segment"]["id"]
            detailedSegment = api.get_segment(athlete.bearer,segment_id)
            leaderboard = api.get_segment_leaderboard(athlete.bearer,segment_id)
            datastore.save_segment(athlete,detailedSegment,leaderboard)
