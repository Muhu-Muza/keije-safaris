const navslide = ()=> {
    const drop = document.querySelector('.drop');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');
    
drop.addEventListener('click',()=>{
    //to toggle Nav
        nav.classList.toggle('nav-active');

     // to animate the Links    
    navLinks.forEach((link,index)=>{
            if(link.style.animation){
                link.style.animation = ``
            }else {
                link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 1}s`;

            }
        });
        //drop animation
        drop.classList.toggle('toggle');
});
   
}

navslide();
