function openGame(url) {
    document.getElementById('gameFrame').src = url;
    document.getElementById('gameDialog').showModal();
}

function closeGame() {
    document.getElementById('gameDialog').close();
    document.getElementById('gameFrame').src = '';
}

(async (x)=>{
     s=await fetch("assets/games.json")
     r=await s.json()


     for(let i in r){
        z=r[i]
        if(z.type!="HTML5") continue
        document.querySelector(".game-list")
        .innerHTML+=`
        <div class="game-item" onclick="openGame('${z.path}')">
    <h3>${z.name}</h3>
</div>
        `
     }
})()