// Olle Ö

// Makes a new value in cookie
function setCookie (cname, cvalue, exdays) {
    const d = new Date()
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000))
    let expires = "expires=" + d.toUTCString()
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/"
}

// Serches after value in cookie
function getCookie (cname) {
    let name = cname + "="
    let ca = document.cookie.split(';')
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i]
        while (c.charAt(0) == ' ') {
            c = c.substring(1)
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length)
        }
    }
    return ""
}

// Checks for existing cookie
// function checkCookie () {
let user = getCookie("username")
if (user != "") {
    console.log("Welcome again " + user)
} else {
    user = prompt("Please enter your name:", "")
    if (user != "" && user != null) {
        setCookie("username", user, 365)
    }
}
// }

// Saves recordings as a value in cookie
function makeRec (cvalue) {
    let ca = document.cookie
    for (let i = 0; i < 5; i++) {
        if (('rec' + i + '=') in ca) {
            continue
        }
        else {
            setCookie(('rec' + i), cvalue, 30)
        }
    }
}