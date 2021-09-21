// https://www.javascripttutorial.net/javascript-bom/javascript-get-query-string/

$('document').ready(function() {
    const urlParams = new URLSearchParams(location.search);
    if( urlParams.has('sort')) {
        $('.top-btn').addClass('border');
    } else {
        $('.new-btn').addClass('border')
    }
})