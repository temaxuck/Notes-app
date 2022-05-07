const openNotes = document.querySelectorAll(".hero__notes-el");

openNotes.forEach((item) => item.addEventListener('click', () => {
   item.classList.toggle("hero__notes-el--test");
   
   let bar = item.querySelector(".hero__util");
   (bar.style.display === "block") ? bar.style.display = 'none' : bar.style.display = 'block';

   let date = item.querySelector('.hero__notes-date');
   (date.style.display === "none") ? date.style.display = 'block' : date.style.display = 'none';
}));