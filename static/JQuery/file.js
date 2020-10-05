$( "#search_adress" ).submit(function( event ) {
	var data_question = $("input").val()
	var data_papybot = "Voyons mon poussin tu sais bien que j\'ai plus toute ma tete. Voyons mon poussin tu sais bien que j\'ai plus toute ma tete. Voyons mon poussin tu sais bien que j\'ai plus toute ma tete."
	
	var msg_papybot =   '<div class="d-flex justify-content-start"><div class="rounded-pill msg-answer">' +
						data_papybot + '</div><div class="logo-bot"><img src="../static/pictures/robot1.jpg" width="50" height="50" alt="logo_bot" class="rounded-circle"></div>'
  	var msg_question = 	'<div class="d-flex justify-content-end"><div class="logo-user"><img src="../static/pictures/user.png" width="50" height="50" alt="logo_user" class="rounded-circle"></div><div class="rounded-pill msg-research">' +
					  	data_question + '</div></div>'
  	
  	$(".chat-box").append(msg_question, [msg_papybot])
  	event.preventDefault()
});