const cursorDot = document.querySelector("[data-cursor-dot]");
const cursorOutline = document.querySelector("[data-cursor-outline]");

window.addEventListener("mousemove", function(e) 
{

    const posX = e.clientX;
    const posY = e.clientY;

    cursorDot.style.left = `${posX}px`;
    cursorDot.style.top = `${posY}px`;

    //cursorOutline.style.left =`${posX}px`;
    //cursorOutline.style.top =`${posY}px`;


    cursorOutline.animate({
        left:`${posX}px`,
        top: `${posY}px`
    },{duration: 500, fill: "forwards"})

})


let menu = document.querySelector('#menu-icon');
let navlist = document.querySelector('.navlist');


menu.onclick = () => {
    menu.classList.toggle('bx-x');
    navlist.classList.toggle('open')
}
