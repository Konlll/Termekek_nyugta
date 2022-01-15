eel.read_from_file()((items) => {
    for (const item in items) {
        option = document.createElement("option")
        option.value = `${items[item]["cikkszam"]}`
        option.text = `${items[item]["kategoria"]}      ${items[item]["termeknev"]}`
        document.querySelector(".select-input").add(option, null)
    }
})

const changeSelectValue = (select) => {
    if (select.value != "start"){
        document.querySelector(".inputs").style.display = "block"
    } else{
        document.querySelector(".inputs").style.display = "none"
    }
}

const addProduct = (products, select, piece, price) => {
    pieceInput = document.querySelector("#db")
    priceInput = document.querySelector("#price")
    piece = pieceInput.value != "" ? pieceInput.value : 1
    price = priceInput.value != "" ? priceInput.value : 5000

    eel.read_from_file()(items => {
        product = {
            articleNumber: items[select]["cikkszam"],
            piece: piece,
            price: price
        }

        pieceInput.value = ""
        priceInput.value = ""
        console.log(product)
        products.push(product)
    })
}

products = []
document.querySelector("#save").addEventListener("click", (e) => {
    e.preventDefault()
    select = document.querySelector(".select-input").value
    if(select.value == "start"){
        alert("Kérem jelöljön ki egy terméket!")
    } else{
        addProduct(products, select, piece=1, price=5000)
        console.log(products)
        document.querySelector(".select-input").options[0].selected = "selected"
    }
})

document.querySelector("#showProducts").addEventListener("click", e => {

    e.preventDefault()

    e.target.style.display = "none"

    document.querySelector(".inputs").style.display = "none"
    document.querySelector(".product-list").style.display = "none"

    document.querySelector(".added-products").style.display = "block"
    document.querySelector(".product-summary").style.display = "block"
    document.querySelector(".receipt").style.display = "block"
    document.querySelector(".back").style.display = "block"

    document.querySelector(".added-products").innerHTML = ""

    pieceSummary = 0
    priceSummary = 0

    products.forEach(product => {
      document.querySelector(".added-products").innerHTML += `
        <div class="product">
            <div class="product-title">
                <h2>Cikszám: ${product.articleNumber} &nbsp; Mennyiség: ${product.piece} db &nbsp; Egységár: ${product.price} Ft</h2>
            </div>
        </div>
    `
        pieceSummary += parseInt(product.piece)
        priceSummary += parseInt(product.price) * parseInt(product.piece)
    })

    document.querySelector(".pieceDb").innerHTML = pieceSummary
    document.querySelector(".priceDb").innerHTML = priceSummary

})

const back = (e) => {
    e.preventDefault()

    document.querySelector(".back").style.display = "none"
    document.querySelector(".inputs").style.display = "none"
    document.querySelector(".product-list").style.display = "flex"

    document.querySelector(".product-summary").style.display = "none"
    document.querySelector(".receipt").style.display = "none"
    document.querySelector("#showProducts").style.display = "block"
    document.querySelector(".added-products").style.display = "none"
}

document.querySelector(".back").addEventListener("click", (e) => back(e))

document.querySelector(".receipt").addEventListener("click", e => {
    e.preventDefault()
    if(products.length == 0){
        alert("Üres nyugtát nem hozhat létre!")
    } else{
        eel.create_receipt(products)
        products = []
        back(e)
        alert("Nyugta létrehozása sikeres!")
    }
})