// получаем доступ к кнопке
const topBtn = document.querySelector(".go-top");

// Скроллинг окна
window.addEventListener("scroll", trackScroll);
// Реакция на нажатие
topBtn.addEventListener("click", goTop);

function trackScroll() {
    // положение от верхушки окна
    const scrolled = window.pageYOffset;
    // высота окна браузера
    const coords = document.documentElement.clientHeight;
    // если в прокрутке вышли за переделы одного экрана
    if(scrolled > coords) {
        // должна показаться кнопка
//        topBtn.classList.add("go-top--show");
        topBtn.style.display = 'block'
        } else {
        // или исчезает
        topBtn.style.display = 'none'
    }
}

function goTop() {
    // пока не дошли до верха
    if (window.pageYOffset > 0) {
        // скроллипг к верху
        window.scrollBy(0, -800);
        setTimeout(goTop, 0)
    }
}