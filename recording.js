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
record.onclick = e => {
    record.disabled = true
    record.style.backgroundColor = "blue"
    // stopRecord.disabled=false;
    // resume.disabled = true;
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
        // stopRecord.disabled=true;
        record.style.backgroundColor = "white"
        if (i == 4) {
            rec.stop()
        }
        else {
            rec.pause()
        }
    }, 1050)
}