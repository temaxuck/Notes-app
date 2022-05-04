const openNotes = document.querySelectorAll(".hero__notes-el");
const closeNote = document.querySelectorAll(".hero__util-el--close");
const utilities = document.querySelectorAll(".hero__util");


openNotes.forEach((item) => item.addEventListener('click', () => {
   item.classList.toggle("hero__notes-el--test");
   let bar = item.querySelector(".hero__util");
   bar.style.display = "block";
}));