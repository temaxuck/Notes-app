const change = document.querySelector('.hero__btn--test');

if(document.documentElement.clientWidth <= 512) {
   const asideList = document.querySelectorAll(".aside__list span");
   asideList.forEach((item) => item.classList.toggle("visible-hidden"));

   const header = document.querySelector(".aside__logo");
   (header.innerHTML.trim() === "NotOnlyNotes") ? header.innerHTML = "N" : header.innerHTML = "NotOnlyNotes";
   
   if(header.style.padding === "40px 40px 0px 40px") {
      header.style.padding = "40px 0px 0px 1px";
      header.style.margin = "0px auto 40px auto";
   }
   else if (header.style.padding === "40px 0px 0px 1px") {
      header.style.padding = "40px 40px 0px 40px";
      header.style.margin = "";
   }
   else {
      header.style.padding = "40px 0px 0px 1px";
      header.style.margin = "0px auto 40px auto";
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
      paddingEl.forEach((item) => item.style.padding = "0px");
      paddingEl.forEach((item) => item.style.marginBottom = "2rem");
   }
   else if (paddingEl[0].style.padding === "0px") {
      paddingEl.forEach((item) => item.style.padding = "10px 0px 10px 40px");
      paddingEl.forEach((item) => item.style.marginBottom = "0px");
   }
   else {
      paddingEl.forEach((item) => item.style.padding = "0px");
      paddingEl.forEach((item) => item.style.marginBottom = "2rem");
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

   const asideLink = document.querySelectorAll(".aside__link");
   if(asideLink[0].style.justifyContent === "center") {
      asideLink.forEach((item) => {
         item.style.justifyContent = "flex-start"
         const linkImg = item.querySelector(".aside__link-icon");
         linkImg.style.margin = "0 1rem 0 0";
      });
   }
   else if (asideLink[0].style.justifyContent === "flex-start") {
      asideLink.forEach((item) => {
         item.style.justifyContent = "center";
         const linkImg = item.querySelector(".aside__link-icon");
         linkImg.style.margin = "0 auto";
      });
   }
   else {
      asideLink.forEach((item) => {
         item.style.justifyContent = "center";
         const linkImg = item.querySelector(".aside__link-icon");
         linkImg.style.margin = "0 auto";
      });
   }
}



change.addEventListener('click', () => {
   const asideList = document.querySelectorAll(".aside__list span");
   asideList.forEach((item) => item.classList.toggle("visible-hidden"));

   const header = document.querySelector(".aside__logo");
   (header.innerHTML.trim() === "NotOnlyNotes") ? header.innerHTML = "N" : header.innerHTML = "NotOnlyNotes";
   
   if(header.style.padding === "40px 40px 0px 40px") {
      header.style.padding = "40px 0px 0px 1px";
      header.style.margin = "0px auto 40px auto";
   }
   else if (header.style.padding === "40px 0px 0px 1px") {
      header.style.padding = "40px 40px 0px 40px";
      header.style.margin = "";
   }
   else {
      header.style.padding = "40px 0px 0px 1px";
      header.style.margin = "0px auto 40px auto";
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
      paddingEl.forEach((item) => item.style.padding = "0px");
      paddingEl.forEach((item) => item.style.marginBottom = "2rem");
   }
   else if (paddingEl[0].style.padding === "0px") {
      paddingEl.forEach((item) => item.style.padding = "10px 0px 10px 40px");
      paddingEl.forEach((item) => item.style.marginBottom = "0px");
   }
   else {
      paddingEl.forEach((item) => item.style.padding = "0px");
      paddingEl.forEach((item) => item.style.marginBottom = "2rem");
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

   const asideLink = document.querySelectorAll(".aside__link");
   if(asideLink[0].style.justifyContent === "center") {
      asideLink.forEach((item) => {
         item.style.justifyContent = "flex-start"
         const linkImg = item.querySelector(".aside__link-icon");
         linkImg.style.margin = "0 1rem 0 0";
      });
   }
   else if (asideLink[0].style.justifyContent === "flex-start") {
      asideLink.forEach((item) => {
         item.style.justifyContent = "center";
         const linkImg = item.querySelector(".aside__link-icon");
         linkImg.style.margin = "0 auto";
      });
   }
   else {
      asideLink.forEach((item) => {
         item.style.justifyContent = "center";
         const linkImg = item.querySelector(".aside__link-icon");
         linkImg.style.margin = "0 auto";
      });
   }

});