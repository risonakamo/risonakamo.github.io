//somewhere else.
window.onload=(()=>{
    var a=document.querySelector(".AREYOULOOKING");
    document.querySelector(".MESSAGE").innerHTML=window.atob(a.innerText).split("\n")[Math.floor(Math.random()*(24))];
    a.parentElement.removeChild(a);
});