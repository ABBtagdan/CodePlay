// Olle Ö

let i = 0

let aud = document.getElementById('audio')

let musicList = []

function init (ml) {
    musicList = ml
}

// Function to play the music on the site
function play () {
    console.log(musicList)
    aud.pause()
    aud.src = ""
    aud.load()
    aud.src = musicList[i] + '.mp3'
    aud.load()
    aud.play()
    // console.log("playing "+musicList[i]+".mp3")
    // aud.play().catch(function (error) {
    //     console.error('Error during playback:', error.message)
    // })
}

// aud.addEventListener("ended", ()=>{if (i != 0){play()}})