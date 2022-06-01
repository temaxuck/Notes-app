function getImg(evt){
    let files = evt.target.files, select_img_btn = document.querySelector('#select_image_btn');
    let file = files[0];
    select_img_btn.innerHTML = "Файл: " + file.name;
}