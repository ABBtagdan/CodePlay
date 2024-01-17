// Olle Ö

let musicList = ['we-live-we-love-we-lie-made-with-Voicemod-technology.mp3', 'Find_Your_One_Way.mp3', 'Play_the_Hero.mp3', 'Operation_Pyrite.mp3']

let i = 0

function play () {

    if (i < musicList.length) {
        let aud = document.getElementById('audio')
        aud.src = musicList[i]
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