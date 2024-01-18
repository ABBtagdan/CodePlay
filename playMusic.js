// Olle Ö

let i = 0

let aud = document.getElementById('audio')

let musicList = []

function init (ml) {
    musicList = ml
}

function play () {
    // console.log(musicList)
    if (i < musicList.length) {
        aud.pause()

        aud.src = musicList[i] + '.mp3'

        aud.load()
        // console.log("playing "+musicList[i]+".mp3")
        // aud.play().catch(function (error) {
        //     console.error('Error during playback:', error.message)
        // })
        i++
        setTimeout(function () {
            play()
        }, 250)
    }
    else {
        i = 0
    }
}

aud.addEventListener('canplaythrough', function () {
    aud.play().catch(function (error) {
        console.error('Error during playback:', error.message);
    });
})

// aud.addEventListener("ended", ()=>{if (i != 0){play()}})