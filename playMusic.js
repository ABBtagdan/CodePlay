// Olle Ö

let i = 0

let aud = document.getElementById('audio')

function play (musicList) {
    // console.log(musicList)
    if (i < musicList.length) {
        aud.src = musicList[i] + '.mp3'
        // console.log("playing "+musicList[i]+".mp3")
        aud.play()
        i++
        aud.addEventListener("ended", function () {
            play(musicList)
        })
    }
    else {
        i = 0
    }
}