$(document).ready(function(){

    var dropdown_menu = "<td>" + "<select id='dropdown' class='selectpicker'>" + "<option>GOOD</option>" + "<option>Karişik</option>" + "<option>BAD</option>" + "<option>Trash</option>" + "</select>";

     $.ajax({
            url: '/list',
            type: 'GET',
            success: function(response) {

                response=JSON.parse(response)

				$("p#pure-tweet").text(response["tweet"]);
                $("p#u-name").text(response["username"]);

                $.each(response["wordsoftweets"], function (index, value) {

                var tabel_row = "<tr>" + "<td>" + index + "</td>" + "<td>" + value + "</td>" + dropdown_menu;
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
                    alert("Patlati gitti")


            },
            error: function(error) {
                console.log(error);
            }
        });



	});




});
