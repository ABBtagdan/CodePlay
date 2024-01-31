// Olle Ö

record = document.getElementById('record')
listen = document.getElementById('listen')
satisfied = document.getElementById('satisfied')
recordedAudio = document.getElementById('recordedAudio')

// Makes it posible to record audio
navigator.mediaDevices.getUserMedia({ audio: true })
    .then(stream => { handlerFunction(stream) })

let i = 0

let blob

function handlerFunction (stream) {
    console.log("Got media device")
    rec = new MediaRecorder(stream)
    rec.ondataavailable = e => {
        audioChunks.push(e.data)
        if (rec.state == "inactive") {
            blob = new Blob(audioChunks, { type: 'audio/mp3' })
            recordedAudio.src = URL.createObjectURL(blob)
            recordedAudio.controls = false
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
    // makeRec(recordedAudio.src)
    const file = new File([blob], 'cropped_image.png', blob);

    // Create a new FormData object and append the file to it
    var formData = new FormData();
    formData.append('audio', file);

    fetch("https://3c46-16-171-29-166.ngrok-free.app/recording",
        {
            method: "POST",
            body: formData
        })
}