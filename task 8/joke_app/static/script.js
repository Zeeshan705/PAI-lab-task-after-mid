let selectedCategory = 'random';
let jokeCount = 0;

const setupEl = document.getElementById('setup');
const punchlineEl = document.getElementById('punchline');
const badgeEl = document.getElementById('jokeBadge');
const jokeBtn = document.getElementById('jokeBtn');
const revealBtn = document.getElementById('revealBtn');
const countEl = document.getElementById('count');
const catBtns = document.querySelectorAll('.cat-btn');

catBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        catBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        selectedCategory = btn.dataset.cat;
    });
});

revealBtn.addEventListener('click', () => {
    punchlineEl.classList.remove('hidden');
    revealBtn.classList.add('hidden');
    jokeCount++;
    countEl.textContent = jokeCount;
});

jokeBtn.addEventListener('click', fetchJoke);

function fetchJoke() {
    jokeBtn.disabled = true;
    setupEl.innerHTML = '<span class="loading">Loading joke...</span>';
    punchlineEl.classList.add('hidden');
    revealBtn.classList.remove('hidden');
    badgeEl.textContent = '...';

    let url = '/get_joke';
    if (selectedCategory !== 'random') {
        url = `/get_joke/${selectedCategory}`;
    }

    fetch(url)
        .then(res => res.json())
        .then(data => {
            setupEl.textContent = data.setup;
            punchlineEl.textContent = data.punchline;
            badgeEl.textContent = data.type;
            jokeBtn.disabled = false;
        })
        .catch(() => {
            setupEl.textContent = 'Could not load joke. Check your internet!';
            revealBtn.classList.add('hidden');
            jokeBtn.disabled = false;
        });
}
