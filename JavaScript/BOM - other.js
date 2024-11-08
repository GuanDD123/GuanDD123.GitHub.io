function Date_() {
    now = new Date();

    localTime = now.toString();
    utcTime = now.toGMTString();

    hours = now.getHours();
    minutes = now.getMinutes();
    seconds = now.getSeconds();
    milliseconds = now.getMilliseconds();
}

function Math_() {
    Math.floor(float)
    Math.random() // 0~1 之间
}
