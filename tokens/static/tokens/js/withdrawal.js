// Set cash amount of withdrawal based on token amount 
var tokens = $('#tokens');

tokens.keyup(function() {
    let cashAmount = tokens.val() / 200;
    cashAmount = cashAmount.toFixed(2);
    $('#cash').text(cashAmount);
})