function resetEverything() {
    localStorage.removeItem('apiUsed');
    localStorage.removeItem('apiResult');

    const button = document.getElementById("runButton");
    if (button) {
        button.disabled = false;
        button.innerText = "🎧 Run Shazam API";
    }

    const result = document.getElementById("result");
    if (result) {
        result.innerHTML = "";
    }
}

if (window.location.pathname === "/reset") {
    resetEverything();
    setTimeout(() => {
        window.location.href = "/";
    }, 0);
}
