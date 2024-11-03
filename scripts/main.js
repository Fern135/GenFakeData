if(getOS() === "Windows"){
    var baseUrl   = "localhost:3000";
}else{
    var baseUrl   = "127.0.0.1:3000";
}
// const url       = `${baseUrl}/api/`;
var url       = `localhost:3000/api/`;

//#region getting length and button. to check if it's clicked

//#region for generating users
async function genUsers(){
    let genUsrCount = document.getElementById("gen-user-count").value;
    // let genUsrBtn   = document.getElementById("gen-user-btn");
    var Url = ``;

    if(genUsrCount <= 1 && genUsrCount < 14000){
        var Url = `${url}users/${genUsrCount}`;
    }

    let x = await fetch(Url);
    let y = await x.json();
    displayGenUser(y);
}

async function loadRandUsrImg() {
    try {
        // Fetch random user data from the API
        const response = await fetch('https://randomuser.me/api/');
        const data = await response.json();

        // Get the image URL from the response
        const imageUrl = data.results[0].picture.large;

        return imageUrl;
        // Set the image URL to the img element
        // const imgElement = document.getElementById('randomImage');
        // imgElement.src = imageUrl;
    } catch (error) {
        console.error("Error fetching random image:", error);
    }
}

function displayGenUser(data){
    /*
        {
            id: i + 1,
            str_id: faker.string.uuid(), 
            name: faker.person.fullName(),
            email: faker.internet.email(),
            phone: faker.phone.number(),
        }
    */

    try {
        const container = document.getElementById('users');

        // Loop through the JSON data and format it
        data.forEach(item => {
            // Create a new div for each entry
            const entry = document.createElement('div');
            entry.classList.add('data-entry');

            // <img id="randomImage" alt="Random Person">
            // Format the content for each entry
            entry.innerHTML = `
                <div class="card">
                    <div class="card-header">
                        <img class="img-fluid rounded" id="randomImage" src="${loadRandUsrImg()}" alt="Random Person">
                    </div>
                    <div class="card-body" id="${item.str_id}">
                        <h3>Name:  ${item.name}</h3>
                        <h4>Email: ${item.email}</h4>
                        <h4>Phone: ${item.phone}</h4>
                    </div>
                    <div class="card-footer">Footer</div>
                </div>
            `;

            // Append the entry to the container
            container.appendChild(entry);
        });
    } catch (error) {
        console.error("Error loading data:", error);
    }

}

//#endregion

// generating products
// let genProdCount = document.getElementById("gen-prod-count").value;
// let genProdBtn   = document.getElementById("gen-prod-btn");

// generating companies 
// let genCompCount = document.getElementById("gen-comp-count").value;
// let genCompBtn   = document.getElementById("gen-comp-btn");

// generating credit cards
// let genCardCount = document.getElementById("gen-card-count").value;
// let genCardBtn   = document.getElementById("gen-card-btn");

// generating jobs 
// let genJobCount = document.getElementById("gen-job-count").value;
// let genJobBtn   = document.getElementById("gen-job-btn");

// generating random text
// let genTextCount = document.getElementById("gen-text-count").value;
// let genTextBtn   = document.getElementById("gen-text-btn");
//#endregion

function getOS() {
    const userAgent = navigator.userAgent;

    if (/win/i.test(userAgent)) {
        return "Windows";
    }
    if (/mac/i.test(userAgent)) {
        return "MacOS";
    }
    if (/linux/i.test(userAgent)) {
        return "Linux";
    }

    return "Unknown";
}
