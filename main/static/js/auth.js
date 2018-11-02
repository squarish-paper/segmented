Auth = {
  authorise: function () {
    //var whereTo = "http://localhost:5000/auth"
    var whereTo = "https://infinite-cliffs-27123.herokuapp.com/auth"
    var redirectUrl = 'https://www.strava.com/oauth/authorize?client_id=14681&response_type=code&redirect_uri='+whereTo+'&approval_prompt=force';
    window.location.href = redirectUrl;
  }
}
