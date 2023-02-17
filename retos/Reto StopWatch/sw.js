let start = document.getElementById('start');
let stop = document.getElementById('stop');
let reset = document.getElementById('reset');
let lap = document.getElementById('lap');

let lapText = document.getElementById('lapText');
let hourHtml = document.getElementById('hour');
let minHtml = document.getElementById('min');
let secHtml = document.getElementById('sec');

let hour = 0;
let min = 0;
let sec = 0;
let lap_num = 0;

let interval;

start.addEventListener('click', function () {
    interval = setInterval(function () {
        if (sec < 59) {
            sec++;
            secHtml.innerHTML = sec < 10 ? "0" + sec : sec;
        } else {
            sec = 0;
            secHtml.innerHTML = sec < 10? "0" + sec : sec;
            if (min < 59) {
                min++;
                minHtml.innerHTML = min < 10 ? "0" + min + ":" : min + ":";
            } else {
                min = 0;
                minHtml.innerHTML = min < 10 ? "0" + min + ":" : min + ":";
                if (hour < 23) {
                    hour++;
                    hourHtml.innerHTML = hour < 10 ? "0" + hour + ":" : hour + ":";
                } else {
                    hour = 0;
                    hourHtml.innerHTML = hour < 10 ? "0" + hour + ":" : hour + ":";
}}}}, 100);
});

lap.addEventListener('click', function () {
    lap_num++;
    lapText.innerHTML += ("<br>Lap#" + lap_num + ": " +
    (hour < 10 ? "0" + hour : hour) + ":" +
    (min < 10 ? "0" + min : min) + ":" +
    (sec < 10 ? "0" + sec : sec))
});

stop.addEventListener('click', function () {
    clearInterval(interval);
});

reset.addEventListener('click', function () {
    clearInterval(interval);
    lap_num = 0;  // reiniciar el contador de vueltas
    hour = 0;
    min = 0;
    sec = 0;
    hourHtml.innerHTML = "00:";
    minHtml.innerHTML = "00:";
    secHtml.innerHTML = "00";
    lapText.innerHTML = "";
});
