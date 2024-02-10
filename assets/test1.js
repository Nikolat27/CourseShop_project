let H1elm = document.querySelector("h1")
let contianerMenu = document.querySelector("ul")
let contianer = document.querySelector(".container")

let isAcive = false

H1elm.addEventListener("click", () => {
    isAcive = !isAcive
    showstyle(isAcive)
})

function showstyle(isAcive) {
    isAcive ? (contianerMenu.style.display = "flex") : contianerMenu.style.display = "none"
    isAcive ? (contianer.style.height = "42vh") : contianer.style.height = "fit-content"
}