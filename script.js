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
                alert("Not valid");
                reject("Not valid");
            }
        })
        .then(data => {
            resolve(data.status === "valid");
        })
        .catch(error => {
            alert("Error");
            reject(error);
        });
    });
}

ch();
