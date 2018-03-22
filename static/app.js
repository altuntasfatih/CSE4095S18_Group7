$(document).ready(function(){

    var dropdown_menu = "<td>" +
                            "<select id='dropdown' class='selectpicker'>" +
                                "<option>TRASH</option>" +
                                "<option>YAS</option>" +
                                "<option>ILETISIM</option>" +
                                "<option>TARIH</option>" +
                                "<option>ID</option>" +
                                "<option>ADDRESS</option>" +
                                "<option>MESLEK</option>" +
                                "<option>FIRMA</option>" +
                                "<option>MEKAN</option>" +
                                "<option>OLAY</option>" +
                                "<option>ISIM</option>" +

                            "</select>" +
                        "</td>";

     $.ajax({
            url: '/list',
            type: 'GET',
            success: function(response) {

                response=JSON.parse(response)

				$("p#pure-tweet").text(response["tweet"]);
                $("p#tweet-id").text(response["tweetID"]);

                $.each(response["wordsoftweets"], function (index, value) {

                var tabel_row = "<tr>" + "<td>" + index + "</td>" + "<td>" + value + "</td>" + dropdown_menu + "</tr>";
                $(tabel_row).appendTo("#tweets-table tbody");

             });
            },
            error: function(error) {
                console.log(error);
            }
        });

     $( "#save-btn" ).click(function() {

		var tweets = [];

		$("table tbody tr").each(function(index, value) {
			$this = $(this);
    			var $table = $('#tweets-table');
    			var itemsLength = $table.find('th').length;
                var obj = {};
    			for (i=0;i<itemsLength;i++) {
				if (i==0){
        				var key = $table.find('th').eq(i).text();
        				var value = $this.find('td').eq(i).text();
        				obj[key] = value;
				} else if (i==2) {
					var key = $table.find('th').eq(i).text();
                    var value = $this.find('td').eq(i).find('#dropdown option:selected').text();
					obj[key] = value;
				}
    			}

			tweets.push(obj)
		});

     $.ajax({
            url: '/save',
            type: 'POST',
             data:JSON.stringify(tweets),
             contentType: "application/json",
            success: function(response) {
                response=JSON.parse(response)
                if (response["status"]==0)
                    location.reload();
                else
                    alert("The write to the database failed !!!")


            },
            error: function(error) {
                console.log(error);
            }
        });



	});


     $( "#previous-btn" ).click(function() {

        $("#tweets-table tbody").empty();   // Delete all table rows of old tweet

        $.ajax({
            url: '/previous',
            type: 'GET',
            success: function(response) {

                response=JSON.parse(response)

                $("p#pure-tweet").text(response["tweet"]);
                $("p#tweet-id").text(response["tweetID"]);

                $.each(response["wordsoftweets"], function (index, value) {

                var tabel_row = "<tr>" + "<td>" + index + "</td>" + "<td>" + value + "</td>" + dropdown_menu + "</tr>";
                $(tabel_row).appendTo("#tweets-table tbody");

             });
            },
            error: function(error) {
                console.log(error);
            }
        });

	});


});
