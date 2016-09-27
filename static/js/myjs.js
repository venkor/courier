// Potwierdzajka
function are_you_sure(e)
{
    if(!confirm('Are you sure?'))e.preventDefault();
}

// $('radio').on('click', function(event)){
//   event.preventDefault();
//   var package_radio = $(".package_radio:checked").val();
//   $.ajax({
//           url: '/package_list/',
//           type: 'GET',
//           data: {packages : package_radio.attr("value")},
//   });
// }
