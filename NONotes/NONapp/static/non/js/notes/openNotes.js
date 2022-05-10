const openNotes = document.querySelectorAll(".hero__notes-el");
const closeNotes = document.querySelectorAll('.hero__util-el--close');
let flag = false;

openNotes.forEach((item) => item.addEventListener('click', () => {
   if(!flag) {
      item.classList.add("hero__notes-el--test");
      let bar = item.querySelector(".hero__util");
      (bar.style.display === "block") ? bar.style.display = 'none' : bar.style.display = 'block';

      let date = item.querySelector('.hero__notes-date');
      (date.style.display === "none") ? date.style.display = 'block' : date.style.display = 'none';

      let textareaDescr = item.querySelector('.hero__notes-descr');
      (textareaDescr.disabled == true) ? textareaDescr.disabled = false : textareaDescr.disabled = true;

      let textareaHeader = item.querySelector('.hero__notes-header');
      (textareaHeader.disabled == true) ? textareaHeader.disabled = false : textareaHeader.disabled = true;
      flag = true;
   }
}));

closeNotes.forEach((item) => item.addEventListener('click', () => {
   if(flag) {
      openNotes.forEach((item) => item.classList.remove('hero__notes-el--test'))
      // document.classList.remove("hero__notes-el--test");
      
      let bar = item.querySelector(".hero__util");
      (bar.style.display === "block") ? bar.style.display = 'none' : bar.style.display = 'block';
   
      let date = item.querySelector('.hero__notes-date');
      (date.style.display === "none") ? date.style.display = 'block' : date.style.display = 'none';
   
      let textareaDescr = item.querySelector('.hero__notes-descr');
      (textareaDescr.disabled == true) ? textareaDescr.disabled = false : textareaDescr.disabled = true;

      let textareaHeader = item.querySelector('.hero__notes-header');
      (textareaHeader.disabled == true) ? textareaHeader.disabled = false : textareaHeader.disabled = true;
      flag = false;
   }
}));