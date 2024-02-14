// Olle Ö

// Get buttons from html
record = document.getElementById("record")
listen = document.getElementById("listen")
satisfied = document.getElementById("satisfied")
recordedAudio = document.getElementById("recordedAudio")

// Makes it posible to record audio
navigator.mediaDevices.getUserMedia({ audio: true }).then((stream) => {
    handlerFunction(stream)
})

let i = 0

let blob

// Saves the recorded audio as a blob
function handlerFunction (stream) {
    console.log("Got media device")
    rec = new MediaRecorder(stream)
    rec.ondataavailable = (e) => {
        audioChunks.push(e.data)
        if (rec.state == "inactive") {
            blob = new Blob(audioChunks, { type: "audio/wav" })
            recordedAudio.src = URL.createObjectURL(blob)
            recordedAudio.controls = false
            recordedAudio.autoplay = true
            sendData(blob)
        }
    }
}

function sendData (data) { }
// To start the recording and stops after 4 recordings
record.onclick = (e) => {
    record.disabled = true
    satisfied.disabled = true
    listen.disabled = true
    audioChunks = []
    if (i == 0) {
        rec.start()
    } else {
        rec.resume()
    }
    setTimeout(function () {
        i++
        record.disabled = false
        if (i == 4) {
            satisfied.disabled = false
            listen.disabled = false
            rec.stop()
            i = 0
        } else {
            rec.pause()
        }
    }, 1000)
}

// Plays back the sound you just recorded
listen.onclick = (e) => {
    recordedAudio.play()
}

// Sends of the finished recording to the server
satisfied.onclick = (e) => {
    // makeRec(recordedAudio.src)
    var xmlhttp = new XMLHttpRequest()
    var url = "https://b862-13-48-25-29.ngrok-free.app//recording"
    xmlhttp.open("POST", url, true)
    xmlhttp.setRequestHeader("Content-type", "audio/wav")
    xmlhttp.send(blob)
}
