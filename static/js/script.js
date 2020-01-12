function Read2(){
    $.ajax({
		url: 'read',
		type: 'POST',
		async: false,
		data:{
			res: 1,
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
		},
		success: function(response){
			$('#result').html(response);
		}
    });
}
function Read1(){
    $.ajax({
		url: 'rndsoru',
		type: 'POST',
		async: false,
		data:{
			res: 1,
			csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
		},
		success: function(response){
			$('#result').html(response);
		}
    });
}
