fetch("/api/products")
.then(response => response.json())
.then(products => {


    const productDiv = document.getElementById("products");


    products.forEach(product => {


        const card = document.createElement("div");

        card.className = "card";


        card.innerHTML = `
            <h3>${product.name}</h3>

            <p class="price">
                ₹${product.price}
            </p>

            <p>
                Stock: ${product.stock}
            </p>

            <button>
                Buy Now
            </button>
        `;


        productDiv.appendChild(card);


    });


})
.catch(error => {
    console.log("Error:", error);
});
