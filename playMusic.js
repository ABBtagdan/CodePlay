// Olle Ö

let i = 0

function play (musicList) {

    if (i < musicList.length) {
        let aud = document.getElementById('audio')
        aud.src = musicList[i] + '.mp3'
        aud.play()
        i++
        aud.addEventListener("ended", function () {
            play()
        })
    }
    else {
        i = 0
    }
}