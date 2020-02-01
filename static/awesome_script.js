
var  index = 5;

function whenButtonClicked() {
	index += 1;
	$("#index").val(index);
	
	var oldContent = $("#div1").html();
	
	$("#div1").html(oldContent + "<div class='bg'></div>")
	
	console.log(index);
}