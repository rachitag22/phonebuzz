function handleForm() {
    var phoneNum = document.getElementById("numberInput").value;
    var delay = document.getElementById("delayInput").value;
    var phoneNumModel = /^\d{10}$/;
    
    if (phoneNum == null || phoneNum == "") {
        document.getElementById("numberInput").parentElement.className = "input-group has-error";
            $("#success-alert").hide();
            $("#warning-alert").hide();
            $("#error-alert").show();
    } else if (!(phoneNum.match(phoneNumModel))) {
        document.getElementById("numberInput").parentElement.className += "input-group has-warning";
            $("#success-alert").hide();
            $("#error-alert").hide();
            $("#warning-alert").show();
    } else {
        document.getElementById("numberInput").parentElement.className = "input-group";
        if (delay == null || delay == "") {
            delay = 0;
        }
        successForm(phoneNum, delay);
    }
}

function successForm(phoneNum, delay) {
    $("#success-alert").show();
    $("#warning-alert").hide();
    $("#error-alert").hide();
    var http = new XMLHttpRequest();
    var url = "https://lendup-challenge-phonebuzz-rachitag22.c9users.io/outbound";
    var params = "num=" + phoneNum + "&delay=" + delay;
    console.log(params);
    
    http.open("POST", url, true);
    http.send(params);
}

$(document).ready(function() {
    $("#success-alert").hide();
    $("#warning-alert").hide();
    $("#error-alert").hide();
});