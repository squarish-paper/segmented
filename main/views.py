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
    view = request.GET.get('view')
    athlete = datastore.get_user(athlete_id)

    if athlete is None:
        return redirect("/connect")

    if athlete.public is False:
        return redirect("/private")

    activities = api.get_athlete_activities(athlete.bearer,athlete.last_logon_date)

    if len(activities) > 0:
        get_segments_from_activities(athlete,activities)


    if view == "frequent":
        efforts = datastore.get_frequent(athlete)
    else:
        efforts = datastore.get_efforts(athlete)

    datastore.update_last_logon(athlete)

    return render(request,"dashboard.html",{"athlete": athlete, "efforts" : efforts})


def get_segments_from_activities(athlete, activities):
    for activity in activities:
        activity_id = activity["id"]

        # check if activity has already been retreived
        activity_xref = get_activity(athlete, activity_id)
        if activity_xref is not None:
            return

        detailedActivity = api.get_activity(athlete.bearer,activity_id)
        segments = detailedActivity["segment_efforts"]

        for segment in segments:
            segment_id = segment["segment"]["id"]
            leaderboard = api.get_segment_leaderboard(athlete.bearer,segment_id)

            # check if segment already exists
            db_segment = datastore.get_segment(segment_id)
            if db_segment is not None:
                detailedSegment = api.get_segment(athlete.bearer,segment_id)
                datastore.save_segment(athlete,detailedSegment,leaderboard)
            else:
                datastore.update_segment(athlete,db_segment,leaderboard,segment["elapsed_time"])
