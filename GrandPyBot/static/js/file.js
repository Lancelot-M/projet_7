let map;
function initMap() 
	{
		map = new google.maps.Map(document.getElementById("map"), 
									{center: {lat: 0.000, lng: 0.000 },
							  		zoom: 2,});
	}
$( "#search_adress" ).on("submit", function( event ) {
	$(".loader").css("display", "block");
	var data_question = $("input").val();
	var url = "/ask/";
	$.ajax({
		method:"POST",
        url: url,
        data: {question: data_question},
        success: function(datas)
        {
        	chat_quest(datas);
        	if (datas["maps_call"] == 1)
        	{
	        	map = new google.maps.Map(document.getElementById("map"), 
										{center: datas["maps_answ"]["location"],
								  		zoom: 15,});
	        	const marker = new google.maps.Marker(
	        	{
			        position: datas["maps_answ"]["location"],
			        map: map,
        		});
	        }
        },
        complete: function()
        {
        	$(".loader").css("display", "none");
        }
    });
    event.preventDefault();
});

function question(obj){
  	var question = 	'<div class="d-flex justify-content-end"><div class="logo-user"><img src="../static/pictures/user.png" width="50" height="50" alt="logo_user" class="rounded-circle"></div><div class="rounded-pill msg-research">' +
					  	obj + '</div></div>';
	return question;
}

function answer(obj){
	var answer =   '<div class="d-flex justify-content-start"><div class="rounded-pill msg-answer">' +
							obj + '</div><div class="logo-bot"><img src="../static/pictures/robot1.jpg" width="50" height="50" alt="logo_bot" class="rounded-circle"></div>';
	return answer;
}

function anecdote(obj){
	var anecdote = '<div class="d-flex justify-content-start"><div class="rounded-pill msg-answer">' +
							obj["wiki_answ"]["extract"] + '<a href=' + 
							obj["wiki_answ"]["fullurl"] + '>En savoir plus</a></div><div class="logo-bot"><img src="../static/pictures/robot1.jpg" width="50" height="50" alt="logo_bot" class="rounded-circle"></div>';
	return anecdote
}

function chat_quest(obj)
{
	if (obj["maps_call"] == "1"){
		$(".chat-box").append(question(obj["question"]));
		$(".chat-box").append(answer(obj["maps_answ"]["formatted_address"]));
		$(".chat-box").append(anecdote(obj));
	}
	else {
		$(".chat-box").append(question(obj["question"]));
		$(".chat-box").append(answer(obj["maps_answ"]));
	}
}