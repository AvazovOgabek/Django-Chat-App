const deleteChatBtn = document.querySelector('.exit');
const card = document.querySelector('.card');

deleteChatBtn.addEventListener('click', () => {
    card.style.display = 'flex'; 
});


function hideCard() {
    card.style.display = 'none';
}