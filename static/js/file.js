/*
$(document).ready(function(){
	# code ici
});
*/

$( "#search_adress" ).on("submit", function( event ) {

	var data_question = $("input").val();
	var url = "/ask/";
	$.ajax({
		method:"POST",
        url: url,
        data: {question: data_question},
        success:function(datas){
        	$(".chat-box").append(question(datas["question"]));
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
	return answer
}