Auth = {

  authorise: function () {
    //var whereTo = "https://d11g903oyygnp2.cloudfront.net/auth.html"
    var whereTo = "https://strava-segmented.firebaseapp.com/auth.html"
    var redirectUrl = 'https://www.strava.com/oauth/authorize?client_id=14681&response_type=code&redirect_uri='+whereTo+'&approval_prompt=force';
    window.location.href = redirectUrl;
  },

  handshake: function () {
    var url_string = window.location.href;
    var url = new URL(url_string);
    var code = url.searchParams.get("code");
    var state = url.searchParams.get("state");
    console.log(code);
    console.log(state);
    Auth.oauth(code);
  },


  oauth: function (code) {
      var form = new FormData();
    form.append("client_id", "14681");
    form.append("client_secret", "11a7876f133ab52f30681e1b97e271153b18fa2f");
    form.append("code", code);

    var settings = {
      "async": false,
      "crossDomain": true,
      "url": "https://www.strava.com/oauth/token",
      "method": "POST",
      "processData": false,
      "contentType": false,
      "mimeType": "multipart/form-data",
      "data": form
    };

    $.ajax(settings).done(function (response) {
      var auth = JSON.parse(response);
      console.log(auth.athlete);
      localStorage.access_token = auth.access_token;
      localStorage.athlete = JSON.stringify(auth.athlete);
      window.location.href = "/segments.html" ;
    });
  }
}
