console.log("SCRIPT LOADED SUCCESSFULLY");

async function getSongs() {
    let mood = document.getElementById("mood").value;

    try {
        const response = await fetch("http://127.0.0.1:5000/recommend", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                mood: mood
            })
        });

        const data = await response.json();

        let output = document.getElementById("output");
        output.innerHTML = "";

        if (data.error) {
            output.innerHTML = `<p>${data.error}</p>`;
            return;
        }

        data.forEach(song => {
            output.innerHTML += `
                <div class="song-card">
                    <h3>${song.title}</h3>
                    <p><strong>Artist:</strong> ${song.artist}</p>
                    <a href="${song.link}" target="_blank">
                        🎵 Listen on YouTube
                    </a>
                    <hr>
                </div>
            `;
        });

    } catch (error) {
        console.error("ERROR:", error);

        document.getElementById("output").innerHTML =
            "<p>Something went wrong ❌</p>";
    }
}

function changeLanguage(lang) {

    if (lang === "te") {

        document.getElementById("title").innerText =
            "మూడ్ ఆధారిత సంగీత సిఫార్సుదారు 🎵";

        document.getElementById("selectMoodLabel").innerText =
            "మీ మూడ్‌ను ఎంచుకోండి:";

        document.getElementById("getRecBtn").innerText =
            "సిఫార్సులు పొందండి";

        document.getElementById("moodHappy").innerText =
            "సంతోషంగా 😊";

        document.getElementById("moodSad").innerText =
            "విచారంగా 😢";

        document.getElementById("moodRelaxed").innerText =
            "విశ్రాంతిగా 😌";

        document.getElementById("moodEnergetic").innerText =
            "ఉత్సాహంగా ⚡";

    } else if (lang === "hi") {

        document.getElementById("title").innerText =
            "मूड आधारित संगीत अनुशंसक 🎵";

        document.getElementById("selectMoodLabel").innerText =
            "अपना मूड चुनें:";

        document.getElementById("getRecBtn").innerText =
            "सिफारिशें प्राप्त करें";

        document.getElementById("moodHappy").innerText =
            "खुश 😊";

        document.getElementById("moodSad").innerText =
            "उदास 😢";

        document.getElementById("moodRelaxed").innerText =
            "आरामदायक 😌";

        document.getElementById("moodEnergetic").innerText =
            "ऊर्जावान ⚡";

    } else {

        document.getElementById("title").innerText =
            "Mood-Based Music Recommender 🎵";

        document.getElementById("selectMoodLabel").innerText =
            "Select Your Mood:";

        document.getElementById("getRecBtn").innerText =
            "Get Recommendations";

        document.getElementById("moodHappy").innerText =
            "Happy 😊";

        document.getElementById("moodSad").innerText =
            "Sad 😢";

        document.getElementById("moodRelaxed").innerText =
            "Relaxed 😌";

        document.getElementById("moodEnergetic").innerText =
            "Energetic ⚡";
    }
}

function openSettings() {
    document.getElementById("settingsModal").style.display = "block";
}

function closeSettings() {
    document.getElementById("settingsModal").style.display = "none";
}

function saveSettings() {

    const lang =
        document.getElementById("languageSelect").value;

    changeLanguage(lang);

    localStorage.setItem("language", lang);

    alert("Settings saved successfully! ✓");

    closeSettings();
}

function updateAIProvider() {
    console.log("AI Provider changed");
}

window.onload = function () {

    const savedLang =
        localStorage.getItem("language");

    if (savedLang) {

        document.getElementById("languageSelect").value =
            savedLang;

        document.getElementById("languageSelector").value =
            savedLang;

        changeLanguage(savedLang);
    }
};