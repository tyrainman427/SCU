$(document).ready(function() {
    let url = "https://newsapi.org/v2/everything?q=blacklivesmatter&sortBy=popularity&apiKey=722c05c77ee94c99bb4d8d5e18dedddc"

    $.ajax({ 
        url:url,
        method:"GET",
        dataType: "json",

        error: function() {
            console.log("fucked");
        },
        beforeSend: function (){
            $(".progress").show();
        },
        complete: function () {
            $(".progress").hide();
        },
        success: function (news){
            let output = "";
            let latestNews = news.articles;
            console.log("NEWS: ",lastestNews)
        },

        });
});
    $.ajax({
        method: "GET",
        error: function() {
          console.log("fucked");
        },
        success: function(data) {
          processData(data);
        }
      });
      
      function processData(data) {
        var articleItems = [];
      
        for (var i = 0; i < data.articles.length; i++) {
          var author = data.articles[i].author;
          var title = data.articles[i].title;
          var description = data.articles[i].description;
          var artUrl = data.articles[i].url;
      
          var $author = $('<div class="author">Author: ' + author + "</div >");
          var $title = $(
            "<a href=" + artUrl + '><div class="title">' + title + "</div ></a>"
          );
          var $description = $(
            "<a href=" +
              artUrl +
              '><div class="description">' +
              description +
              "</div ></a>"
          );
      
          $(".wrapper").append($author, $title, $description);
          console.log(artUrl);
        }
      }

  
  function movieSelected(id) {
      sessionStorage.setItem('movieId',id);
      window.location = 'details/';
      return false;
}
  