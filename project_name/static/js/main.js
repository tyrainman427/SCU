function toggle_visibility(divId1, divId2){
	if(document.getElementById(divId1).style.display == 'block'){
    document.getElementById(divId1).style.display = 'none';
    document.getElementById(divId2).style.display = 'block';
	}else{
	  document.getElementById(divId2).style.display = 'none';
	  document.getElementById(divId1).style.display = 'block'
	}
}
