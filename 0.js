//somewhere else.
window.onload=(()=>{
    setTimeout(()=>{
        var a=document.querySelector(".AREYOULOOKING");
        document.querySelector(".MESSAGE").innerHTML=window.atob(a.innerText).split("\n")[Math.floor(Math.random()*(24))];
        a.parentElement.removeChild(a);
    },Math.floor(Math.random()*1000)+1000);
});