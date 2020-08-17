function toggle_visibility(divId1, divId2){
	if(document.getElementById(divId1).style.display == 'block'){
    document.getElementById(divId1).style.display = 'none';
    document.getElementById(divId2).style.display = 'block';
	}else{
	  document.getElementById(divId2).style.display = 'none';
	  document.getElementById(divId1).style.display = 'block'
	}
}
$(document).ready(function(){
	$(window).scroll(function () {
			if ($(this).scrollTop() > 50) {
				$('#back-to-top').fadeIn();
			} else {
				$('#back-to-top').fadeOut();
			}
		});
		// scroll body to 0px on click
		$('#back-to-top').click(function () {
			$('body,html').animate({
				scrollTop: 0
			}, 400);
			return false;
		});
});
