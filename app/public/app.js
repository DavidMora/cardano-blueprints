function sendCommand() {
	let commands = $('#commandsInput').val();
	$.ajax({
		type: "POST",
		url: "/api/executeMovements",
		contentType:"application/json; charset=utf-8",
		data: JSON.stringify({ commands }),
		success: (data) => {
			if (Array.isArray(data)) {
				let ul = $('<ul/>');
				data.forEach((element) => {
					if (Array.isArray(element)) {
						let li = $('<li/>')
						if (element.length > 0) {
							let html = ''
							element.forEach((element) => {
								html += `[ Id: ${element.id} - Position: (${element.position[0]}, ${element.position[1]}) - Angle: ${element.angle} ]    `
							})
							li.html(html)
						} else {
							li.html('Create grid')
						}

						ul.append(li)
					}
				})
				$('#results').empty()
				$('#results').append(ul)
			} 
		}
	});
}
