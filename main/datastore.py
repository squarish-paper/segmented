from .models import Athlete
from .models import Activities
from .models import Segment
from .models import Efforts
from datetime import datetime

def auth_user(jsonAthlete):

    athlete = convertAthlete(jsonAthlete)

    try:
        athlete = Athlete.objects.get(strava_id=jsonAthlete['athlete']['id'])
        athlete.bearer = jsonAthlete['access_token']
        print("[DATASTORE] | auth_user | update" )
        athlete.save()
    except Athlete.DoesNotExist:
        print("[DATASTORE] | auth_user | new" )
        athlete.save()

    return athlete

def get_user(athlete_id):
    try:
        print("[DATASTORE] | get_user " )
        return Athlete.objects.get(strava_id=athlete_id)
    except Athlete.DoesNotExist:
        return None

def update_last_logon(athlete):
    print("[DATASTORE] | update_last_logon " )
    athlete.last_logon_date = datetime.now()
    athlete.save()


def save_segment(athlete,detailedSegment,leaderboard):

    segment = Segment()
    try:
        segment = Segment.objects.get(segment_id=detailedSegment['id'])
        segment.total_efforts = detailedSegment['effort_count']
        segment.total_athletes = detailedSegment['athlete_count']
        segment.top_time = leaderboard["entries"][0]["elapsed_time"]
        entries = len(leaderboard["entries"])
        segment.tenth_time = leaderboard["entries"][entries-6]["elapsed_time"]
        segment.refresh_date = datetime.now()
        print("[DATASTORE] | save_segment | update segment | " + str(detailedSegment['id'] ))
        segment.save()
    except Segment.DoesNotExist:
        segment.segment_id = detailedSegment['id']
        segment.name = detailedSegment['name']
        segment.distance = detailedSegment['distance']
        segment.elevation = detailedSegment['total_elevation_gain']
        segment.type = detailedSegment['activity_type']
        segment.total_efforts = detailedSegment['effort_count']
        segment.total_athletes = detailedSegment['athlete_count']
        segment.top_time = leaderboard["entries"][0]["elapsed_time"]
        entries = len(leaderboard["entries"])
        segment.tenth_time = leaderboard["entries"][entries-6]["elapsed_time"]
        segment.refresh_date = datetime.now()
        print("[DATASTORE] | save_segment | new segment | " + str(detailedSegment['id'] ))
        segment.save()


    try:
        effort = Efforts.objects.get(athlete=athlete,segment=segment)
        effort.pb = detailedSegment['athlete_segment_stats']['pr_elapsed_time']
        effort.efforts = detailedSegment['athlete_segment_stats']['effort_count']
        effort.rank = getRank(athlete,leaderboard)
        print("[DATASTORE] | save_segment | update effort ")
        effort.save()
    except Efforts.DoesNotExist:
        effort = Efforts()
        effort.athlete = athlete
        effort.segment = segment
        effort.pb = detailedSegment['athlete_segment_stats']['pr_elapsed_time']
        effort.efforts = detailedSegment['athlete_segment_stats']['effort_count']
        effort.rank = getRank(athlete,leaderboard)
        print("[DATASTORE] | save_segment | new effort | " )
        effort.save()

def update_segment(athlete,segment,leaderboard,new_time):

    try:
        segment = Segment.objects.get(segment_id=detailedSegment['id'])
        segment.total_athletes = leaderboard['effort_count']
        segment.top_time = leaderboard["entries"][0]["elapsed_time"]
        entries = len(leaderboard["entries"])
        segment.tenth_time = leaderboard["entries"][entries-6]["elapsed_time"]
        segment.refresh_date = datetime.now()
        print("[DATASTORE] | update_segment | segment | " + str(detailedSegment['id'] ))
        segment.save()
    except Segment.DoesNotExist:
        pass

    try:
        effort = Efforts.objects.get(athlete=athlete,segment=segment)
        if effort.pb > new_time:
            effort.pb = new_time
        effort.efforts += 1
        effort.rank = getRank(athlete,leaderboard)
        print("[DATASTORE] | update_segment | effort ")
        effort.save()
    except Efforts.DoesNotExist:
        pass

def get_segment(segment_id):
    print("[DATASTORE] | get_segment | " )
    try:
        segment = Segments.objects.filter(segment_id=segment_id)
        return segment
    except Efforts.DoesNotExist:
        return None

def get_efforts(athlete):
    print("[DATASTORE] | get_efforts | " )
    try:
        efforts = Efforts.objects.filter(athlete=athlete)
        return efforts
    except Efforts.DoesNotExist:
        return None

def get_frequent(athlete):
    print("[DATASTORE] | get_efforts | " )
    try:
        efforts = Efforts.objects.filter(athlete=athlete).order_by('-efforts')[:10]
        return efforts
    except Efforts.DoesNotExist:
        return None

def save_activity(athlete, activity_id):
    print("[DATASTORE] | save_activity | " )
    activities = Activities()
    activities.athlete = athlete
    activities.activity_id = activity_id
    activities.save()

def get_activity(athlete, activity_id):
    print("[DATASTORE] | get_activity | " )
    try:
        activities = Activities.objects.filter(athlete=athlete, activity_id=activity_id)
        return activities
    except Efforts.DoesNotExist:
        return None


def convertAthlete(jsonAthlete):
    athlete = Athlete()
    print(jsonAthlete)
    athlete.strava_id = jsonAthlete['athlete']['id']
    athlete.first_name = jsonAthlete['athlete']['firstname']
    athlete.last_name = jsonAthlete['athlete']['lastname']
    athlete.bearer = jsonAthlete['access_token']
    athlete.public = True
    athlete.picture_url = jsonAthlete['athlete']['profile_medium']
    athlete.user_name = jsonAthlete['athlete']['username']
    return athlete

def getRank(athlete,leaderboard):
    rank = 0
    if len(leaderboard["entries"]) > 10:
        rank = leaderboard["entries"][12]["rank"]
    return rank
