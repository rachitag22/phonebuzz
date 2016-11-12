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
        phoneNum = "+1" + phoneNum;
        successForm(phoneNum, delay);
    }
}

function successForm(phoneNum, delay) {
    $("#success-alert").show();
    $("#warning-alert").hide();
    $("#error-alert").hide();
}

$(document).ready(function() {
    $("#success-alert").hide();
    $("#warning-alert").hide();
    $("#error-alert").hide();
});