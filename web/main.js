eel.read_from_file()((items) => {
    for (const item in items) {
        document.querySelector(".wrapper").innerHTML += items[item]["ar"] + "<br>"
    }
})