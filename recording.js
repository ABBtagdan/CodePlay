// Olle Ö

// Makes it posible to record audio
navigator.mediaDevices.getUserMedia({ audio: true })
    .then(stream => { handlerFunction(stream) })

let i = 0

function handlerFunction (stream) {
    rec = new MediaRecorder(stream)
    rec.ondataavailable = e => {
        audioChunks.push(e.data)
        if (rec.state == "inactive") {
            let blob = new Blob(audioChunks, { type: 'audio/mp3' })
            recordedAudio.src = URL.createObjectURL(blob)
            recordedAudio.controls = true
            recordedAudio.autoplay = true
            sendData(blob)
        }
    }
}

function sendData (data) { }
// To start the recording and stops after 4 recordings
record.onclick = e => {
    record.disabled = true
    satisfied.disabled = true
    listen.disabled = true
    audioChunks = []
    if (i == 0) {
        rec.start()
    }
    else {
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
        }
        else {
            rec.pause()
        }
    }, 1000)
}

// Plays back the sound you just recorded
listen.onclick = e => {
    recordedAudio.play()
}

// Sends of the finished recording to the server
satisfied.onclick = e => {
    makeRec(recordedAudio.src)
    fetch(blob,
        {
            method: "POST",
            body: "recording",
        })
}