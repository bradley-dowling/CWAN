// #############################################################
// #############################################################
// ## Name: inline_incrementer.js
// ## Author: Bradley Dowling, 2021
// ## Description: inline_incrementer.js controls the auto-
// ##              incrementing feature in the inline citation
// ##              tabs in the article admin page. It was necessary
// ##              to implement this because this is not a builtin
// ##              feature in Django apparently.

jQuery(function($) {
  $(document).ready(function(){
    $(".add-row").click(function(){
      let c = document.getElementsByClassName("field-citation_number");
      c[c.length - 2].firstElementChild.value = c.length - 1;
    });
  });
});