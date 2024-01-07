//1) Добавление задачи
let list = [];
let button = document.getElementById("btn");
    button.addEventListener("click",()=>{
        
        let text = document.getElementById("txt").value;
        
        list.push(text);
        saveContent();
        showContent();
        let picks = document.getElementsByClassName("input");
//console.log(picks);
for (let i=0;i<picks.length;i++){
    picks[i].addEventListener("click",(e)=>{
        console.log(e.target.parentElement);
        e.target.parentElement.classList.toggle("decor");
    })
    //console.log(picks[i]);
}
})
    
    function saveContent(){
        localStorage.setItem("list",JSON.stringify(list))
    }
    function showContent(){
        let content = document.getElementById("content");
        let out="";
        list.forEach(function(text){
            out+=`<li class=textList>${text}<input type="checkbox" class="input"></li>`
        })
        content.innerHTML=out;
    }




    

        
  

