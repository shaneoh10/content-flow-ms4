// https://www.javascripttutorial.net/javascript-bom/javascript-get-query-string/

const urlParams = new URLSearchParams(location.search);
$('document').ready(function() {
    if( urlParams.has('sort')) {
        $('.top-btn').addClass('border-primary text-primary');
    } else {
        $('.new-btn').addClass('border-primary text-primary');
    }
    if( urlParams.has('q')) {
        $('#no-posts').text('Please enter search criteria.');
    }
});