const change = document.querySelector('.hero__btn--test');



change.addEventListener('click', () => {
   const asideList = document.querySelectorAll(".aside__list span");
   asideList.forEach((item) => item.classList.toggle("visible-hidden"));

   const header = document.querySelector(".aside__logo");
   (header.innerHTML.trim() === "NotOnlyNotes") ? header.innerHTML = "N" : header.innerHTML = "NotOnlyNotes";
   
   if(header.style.padding === "40px 0px 40px 40px") {
      header.style.padding = "40px 0px 40px 10px";
   }
   else if (header.style.padding === "40px 0px 40px 10px") {
      header.style.padding = "40px 0px 40px 40px";
   }
   else {
      header.style.padding = "40px 0px 40px 10px";
   }

   let accountBlock = document.querySelector(".aside__account-block");
   if(accountBlock.style.display === "grid") {
      accountBlock.style.display = "none";
   }
   else if(accountBlock.style.display === "none") {
      accountBlock.style.display = "grid";
   }
   else {
      accountBlock.style.display = "none";
   }

   const paddingEl = document.querySelectorAll(".aside__el");
   if(paddingEl[0].style.padding === "10px 0px 10px 40px") {
      paddingEl.forEach((item) => item.style.padding = "10px 0px 10px 10px");
   }
   else if (paddingEl[0].style.padding === "10px 0px 10px 10px") {
      paddingEl.forEach((item) => item.style.padding = "10px 0px 10px 40px");
   }
   else {
      paddingEl.forEach((item) => item.style.padding = "10px 0px 10px 10px");
   }

   const asideWidth = document.querySelector(".aside");
   if(asideWidth.style.width === "30%") {
      asideWidth.style.width = "5%";
   }
   else if(asideWidth.style.width === "5%") {
      asideWidth.style.width = "30%";
   }
   else {
      asideWidth.style.width = "5%";
   }


});