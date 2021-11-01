// #############################################################
// #############################################################
// ## Name: article_list.js
// ## Author: Bradley Dowling, 2021
// ## Description: article_list.js controls the functions of
// ##              opening and closing a list of articles.

var type_headers = document.getElementsByClassName("type-header");
var i; // iterator

for (i = 0; i < type_headers.length; i++) {
	type_headers[i].addEventListener("click", function() {
		this.classList.toggle("active");
		var content = this.nextElementSibling; // content block containing article list
		if (content.style.maxHeight) {
			// content block is currently open, so close it
			content.style.maxHeight = null;
			this.textContent = "[+] " + this.textContent.substr(4);
    } else {
			// content block is currently closed, so open it
			content.style.maxHeight = content.scrollHeight + "px";
			this.textContent = "[-] " + this.textContent.substr(4);
		}
	});
}

// opening a section based on the section ID:
function closeSection(sectionID) {
  var section = document.getElementById(sectionID);
	section.click();
}