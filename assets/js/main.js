function openGame(url) {
  document.getElementById("gameFrame").src = url;
  document.getElementById("gameDialog").showModal();
}

function closeGame() {
  document.getElementById("gameDialog").close();
  document.getElementById("gameFrame").src = "";
}

//Load the games from a JSON file.
(async () => {
  s = await fetch("assets/games.json");
  r = await s.json();
  

  for (let i in r) {
    let z = r[i]; //One of the iterable objects.
    if (z.name == "webretro"|| z.name.includes("Upload")) continue;

    let gamesList=document.querySelector(".game-list")
    let gameDiv=document.createElement("div")
    gameDiv.className="game-item"
    gameDiv.addEventListener("click",e=>openGame(z.path))
    gameDiv.innerText=z.name
    gamesList.appendChild(gameDiv)
  }
})();
