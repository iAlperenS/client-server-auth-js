console.log("Script started")

function ch() {
    return new Promise((resolve, reject) => {
        fetch("http://localhost:5000/get_hwid_status", {
            method: "GET"
        })
        .then(response => {
            if (response.ok) {
                alert("Valid");
                return response.json();
            } else {
                hx();
                re();
                reject("Not valid");
            }
        })
        .then(data => {
            resolve(data.status === "valid");
        })
        .catch(error => {
            hx();
            re();
            reject(error);
        });
    });
}

function hx() {
    // Display hides
    document.body.style.display = "none";
}

function re() {
    // Return the url
    window.location.href = "https://github.com/iAlperenS";
}

ch().then(isValid => {
    if (isValid) {
        // True passed
    } else {
        // False
        hx();
        re();
    }
}).catch(error => {
    // Error
    hx();
    re();
});
