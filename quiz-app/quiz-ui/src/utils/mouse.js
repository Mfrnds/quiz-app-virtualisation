import audioFile from "@/assets/mouse_sound.mp3";
import "@/assets/base.css"

document.addEventListener("click", function() {
    var audio = new Audio(audioFile);
    audio.volume = 0.15
    audio.play();

});
