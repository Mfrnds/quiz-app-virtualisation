import audioFile from "@/assets/mouse_sound.mp3";
import "@/assets/base.css"

document.addEventListener("click", function() {
    var audio = new Audio(audioFile);
    audio.volume = 0.15
    audio.play();
});

document.addEventListener('mousedown', function(e) {
    var cursor = document.createElement('div');
    cursor.className = 'click-cursor';
    cursor.style.left = (e.pageX - 30) + 'px';
    cursor.style.top = (e.pageY - 30) + 'px';
    document.body.appendChild(cursor);
    setTimeout(function() {
      cursor.parentNode.removeChild(cursor);
    }, 700);
  });