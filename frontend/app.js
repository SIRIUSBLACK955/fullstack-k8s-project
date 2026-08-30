async function loadBooks() {

    try {

        const response = await fetch(
            "http://backend-service:5000/api/books"
        );

        const books = await response.json();

        const container = document.getElementById("books");

        container.innerHTML = "";

        books.forEach(book => {

            const div = document.createElement("div");

            div.className = "book";

            div.innerHTML = `
                <h2>${book.title}</h2>
                <p>Author: ${book.author}</p>
            `;

            container.appendChild(div);

        });

    } catch (error) {

        console.error(error);

        document.getElementById("books").innerHTML =
            "<p>Unable to connect to backend.</p>";

    }
}