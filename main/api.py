import requests, json

def oauth(code,state) :
    url = "https://www.strava.com/oauth/token"
    print("[API] | Calling " + url)

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"client_id\"\r\n\r\n14681\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"client_secret\"\r\n\r\n11a7876f133ab52f30681e1b97e271153b18fa2f\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"code\"\r\n\r\n"+code+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
        'postman-token': "028c29a5-4486-f665-2ec5-96ec926e86cd"
        }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response.json()

def get_athlete_activities(bearer, lastLogon):

    epocc = lastLogon.timestamp()
    url = "https://www.strava.com/api/v3/athlete/activities?after=" + str(epocc) + "&per_page=10"
    #url = "https://www.strava.com/api/v3/athlete/activities?per_page=10"
    return get(url,bearer)

def get_activity(bearer,activity_id):
    url = "https://www.strava.com/api/v3/activities/" + str(activity_id)
    return get(url,bearer)

def get_segment(bearer,segment_id):
    url = "https://www.strava.com/api/v3/segments/" + str(segment_id)
    return get(url,bearer)

def get_segment_leaderboard(bearer,segment_id):
    url = "https://www.strava.com/api/v3/segments/" + str(segment_id) +"/leaderboard"
    return get(url,bearer)

def get(url,bearer):
    #TODO: Error Handle this
    print("[API] | GET " + url)
    headers = {'Authorization': 'Bearer ' + bearer}
    response = requests.get(url, headers=headers)
    return response.json()
