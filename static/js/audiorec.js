function runApi() {
    const button = document.getElementById("runButton");
    button.disabled = true;
    button.innerText = "Processing...";

    fetch('/api_1_run', {
        method: 'POST'
    })
    .then(response => {
        if (response.status === 403) {
            throw new Error("You have already used this API.");
        }
        return response.json();
    })
    .then(data => {
        if (data.song && data.artist && data.cover_art) {
            localStorage.setItem('apiResult', JSON.stringify(data));
            localStorage.setItem('apiUsed', 'true');

            displayResult(data);
            button.innerText = "✅ Success";
        } else {
            document.getElementById("result").innerText = "Track not found.";
            button.innerText = "Error";
        }
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("result").innerText = error.message;
        button.innerText = "Blocked";
    });
}

function displayResult(data) {
    document.getElementById("result").innerHTML = `
        <h3>🎵 Song: ${data.song}</h3>
        <p>🎤 Artist: ${data.artist}</p>
        <img src="${data.cover_art}" alt="Cover Art" width="200">
    `;
}

window.onload = function () {
    const saved = localStorage.getItem('apiResult');
    const used = localStorage.getItem('apiUsed');
    const button = document.getElementById("runButton");

    if (saved && used === 'true') {
        const data = JSON.parse(saved);
        displayResult(data);
        button.disabled = true;
        button.innerText = "✅ Success";
    }
};
