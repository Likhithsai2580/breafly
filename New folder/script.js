
document.getElementById('close-btn').addEventListener('click', function () {
    const currentPlay = document.getElementById('current-play');
    const current = document.getElementById('close-btn');
    currentPlay.classList.toggle('open');
    current.classList.toggle('open-close-btn');

});

function forToggle(params) {
    const currentPlay = document.getElementById('current-play');
    const current = document.getElementById('close-btn');
    currentPlay.classList.add('open');
    current.classList.add('open-close-btn');

}
