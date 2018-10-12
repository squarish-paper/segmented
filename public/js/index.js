Index = {

    initialise: function() {
      console.log("Index.initialise");
      if (localStorage.athlete != null) {
        window.location.href = "/segments.html" ;
      }
    }

}
