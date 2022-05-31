function closeNote(note) {
	note.classList.remove("hero__notes-el--test");
	
	let bar = note.querySelector(".hero__util");
	bar.style.display = 'none'
	
	let date = note.querySelector('.hero__notes-date');
	date.style.display = 'block';

	let textareaHeader = note.querySelector('.hero__notes-header');
	textareaHeader.readOnly = true;
	
	let textareaDescr = note.querySelector('.hero__notes-descr');
	textareaDescr.readOnly = true;
    
    let save_btn = note.querySelector('.hero__save-note');
	save_btn.style.display = 'none';

    let delete_note_btn = note.querySelector('.delete_note_wrapper');
    delete_note_btn.style.display = 'block'; 
}

function openNote(note) {
	if (note.classList.contains('hero__notes-el--test'))
		return
	note.classList.add("hero__notes-el--test");
	
	let bar = note.querySelector(".hero__util");
	(bar.style.display === "block") ? bar.style.display = 'none' : bar.style.display = 'block';
	
	let date = note.querySelector('.hero__notes-date');
	(date.style.display === "none") ? date.style.display = 'block' : date.style.display = 'none';

	let textareaHeader = note.querySelector('.hero__notes-header');
	textareaHeader.readOnly = false;
	
	let textareaDescr = note.querySelector('.hero__notes-descr');
	textareaDescr.readOnly = false;

    let save_btn = note.querySelector('.hero__save-note');
	save_btn.style.display = "block";

    let delete_note_btn = note.querySelector('.delete_note_wrapper');
    delete_note_btn.style.display = 'none'; 
}

let openNotes = document.querySelectorAll(".hero__notes-el");
let closeNotes = document.querySelectorAll('.hero__util-el--close');
let main = document.querySelector('.main');

closeNotes.forEach((item) => item.addEventListener('click', (e) => {
	e.stopPropagation();
	closeNote(item.parentNode.parentNode.parentNode);
}));

main.addEventListener('click', (e) => {
	console.log(document.querySelector('.hero'));
	if (e.target == main || e.target == document.querySelector('.hero')) 
		document.querySelectorAll('.hero__notes-el--test').forEach(item => {
			closeNote(item);
		});
})