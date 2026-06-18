console.log("SCRIPT LOADED SUCCESSFULLY");

async function getSongs() {
    let mood = document.getElementById("mood").value;

    try {
        const response = await fetch("http://127.0.0.1:5000/recommend", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ mood: mood })
        });

        const data = await response.json();

        let output = document.getElementById("output");
        output.innerHTML = "";

        // ❌ ERROR CASE
        if (!response.ok) {
            output.innerHTML = `<p>${data.error || "Something went wrong"}</p>`;
            return;
        }

        // 🎯 FIXED RESPONSE HANDLING (matches backend)
        if (data.songs && Array.isArray(data.songs)) {

            data.songs.forEach(song => {
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

        } else {
            output.innerHTML = `<p>Unexpected response format</p>`;
        }

    } catch (error) {
        console.error("ERROR:", error);

        document.getElementById("output").innerHTML =
            "<p>Something went wrong ❌</p>";
    }
}


// 🌐 LANGUAGE SWITCHING
function changeLanguage(lang) {

    if (lang === "te") {

        document.getElementById("title").innerText =
            "మూడ్ ఆధారిత సంగీత సిఫార్సుదారు 🎵";

        document.getElementById("selectMoodLabel").innerText =
            "మీ మూడ్‌ను ఎంచుకోండి:";

        document.getElementById("getRecBtn").innerText =
            "సిఫార్సులు పొందండి";

    } else if (lang === "hi") {

        document.getElementById("title").innerText =
            "मूड आधारित संगीत अनुशंसक 🎵";

        document.getElementById("selectMoodLabel").innerText =
            "अपना मूड चुनें:";

        document.getElementById("getRecBtn").innerText =
            "सिफारिशें प्राप्त करें";

    } else {

        document.getElementById("title").innerText =
            "Mood-Based Music Recommender 🎵";

        document.getElementById("selectMoodLabel").innerText =
            "Select Your Mood:";

        document.getElementById("getRecBtn").innerText =
            "Get Recommendations";
    }
}


// ⚙️ SETTINGS MODAL
function openSettings() {
    document.getElementById("settingsModal").style.display = "block";
}

function closeSettings() {
    document.getElementById("settingsModal").style.display = "none";
}


// 💾 SAVE SETTINGS
function saveSettings() {

    const lang = document.getElementById("languageSelect").value;

    changeLanguage(lang);

    localStorage.setItem("language", lang);

    alert("Settings saved successfully! ✓");

    closeSettings();
}


// 🤖 AI Provider (future use)
function updateAIProvider() {
    console.log("AI Provider changed");
}


// 🔄 LOAD SAVED LANGUAGE
window.onload = function () {

    const savedLang = localStorage.getItem("language");

    if (savedLang) {
        document.getElementById("languageSelect").value = savedLang;
        document.getElementById("languageSelector").value = savedLang;
        changeLanguage(savedLang);
    }
};