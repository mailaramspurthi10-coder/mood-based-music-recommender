// ==========================================
// Translation Management
// ==========================================

let currentLanguage = 'en';
let translations = {};

// Load translation file
async function loadTranslations(lang) {
    try {
        const response = await fetch(`./translations/${lang}.json`);
        translations[lang] = await response.json();
        return translations[lang];
    } catch (error) {
        console.error(`Error loading ${lang} translations:`, error);
        return null;
    }
}

// Change language
async function changeLanguage(lang) {
    currentLanguage = lang;
    const trans = await loadTranslations(lang);
    
    if (trans) {
        updateUIText(trans);
        localStorage.setItem('preferredLanguage', lang);
        document.documentElement.lang = lang;
    }
}

// Update UI text with translations
function updateUIText(trans) {
    // Header
    const titleEl = document.getElementById('title');
    if (titleEl) titleEl.textContent = trans.title;
    
    // Mood selector
    const selectMoodLabel = document.getElementById('selectMoodLabel');
    if (selectMoodLabel) selectMoodLabel.textContent = trans.selectMood;
    
    // Mood options
    const moodHappy = document.getElementById('moodHappy');
    if (moodHappy) moodHappy.textContent = trans.happy;
    
    const moodSad = document.getElementById('moodSad');
    if (moodSad) moodSad.textContent = trans.sad;
    
    const moodRelaxed = document.getElementById('moodRelaxed');
    if (moodRelaxed) moodRelaxed.textContent = trans.relaxed;
    
    const moodEnergetic = document.getElementById('moodEnergetic');
    if (moodEnergetic) moodEnergetic.textContent = trans.energetic;
    
    // Buttons
    const getRecBtn = document.getElementById('getRecBtn');
    if (getRecBtn) getRecBtn.textContent = trans.getRecSongs;
    
    const settingsBtn = document.getElementById('settingsBtn');
    if (settingsBtn) settingsBtn.title = trans.settings;
    
    // Settings Modal
    const settingsTitle = document.getElementById('settingsTitle');
    if (settingsTitle) settingsTitle.textContent = trans.settingsTitle;
    
    const languageSettingsLabel = document.getElementById('languageSettingsLabel');
    if (languageSettingsLabel) languageSettingsLabel.textContent = trans.language;
    
    const aiProviderLabel = document.getElementById('aiProviderLabel');
    if (aiProviderLabel) aiProviderLabel.textContent = trans.aiProvider;
    
    const noneProviderLabel = document.getElementById('noneProviderLabel');
    if (noneProviderLabel) noneProviderLabel.textContent = 'None (Basic Mode)';
    
    const localAiLabel = document.getElementById('localAiLabel');
    if (localAiLabel) localAiLabel.textContent = trans.localAi;
    
    const openaiLabel = document.getElementById('openaiLabel');
    if (openaiLabel) openaiLabel.textContent = 'OpenAI';
    
    const geminiLabel = document.getElementById('geminiLabel');
    if (geminiLabel) geminiLabel.textContent = 'Google Gemini';
    
    // Ollama settings
    const ollamaSettingsTitle = document.getElementById('ollamaSettingsTitle');
    if (ollamaSettingsTitle) ollamaSettingsTitle.textContent = 'Ollama Configuration';
    
    const ollamaEndpointLabel = document.getElementById('ollamaEndpointLabel');
    if (ollamaEndpointLabel) ollamaEndpointLabel.textContent = trans.ollamaEndpoint + ':';
    
    const ollamaModelLabel = document.getElementById('ollamaModelLabel');
    if (ollamaModelLabel) ollamaModelLabel.textContent = trans.ollamaModel + ':';
    
    // OpenAI settings
    const openaiSettingsTitle = document.getElementById('openaiSettingsTitle');
    if (openaiSettingsTitle) openaiSettingsTitle.textContent = 'OpenAI Configuration';
    
    const openaiKeyLabel = document.getElementById('openaiKeyLabel');
    if (openaiKeyLabel) openaiKeyLabel.textContent = trans.openaiKey + ':';
    
    // Gemini settings
    const geminiSettingsTitle = document.getElementById('geminiSettingsTitle');
    if (geminiSettingsTitle) geminiSettingsTitle.textContent = 'Google Gemini Configuration';
    
    const geminiKeyLabel = document.getElementById('geminiKeyLabel');
    if (geminiKeyLabel) geminiKeyLabel.textContent = trans.geminiKey + ':';
    
    // Buttons
    const saveSettingsBtn = document.getElementById('saveSettingsBtn');
    if (saveSettingsBtn) saveSettingsBtn.textContent = trans.save;
    
    const closeSettingsBtn = document.getElementById('closeSettingsBtn');
    if (closeSettingsBtn) closeSettingsBtn.textContent = trans.close;
    
    const loadingText = document.getElementById('loadingText');
    if (loadingText) loadingText.textContent = trans.loading;
}

// ==========================================
// Settings Management
// ==========================================

const DEFAULT_SETTINGS = {
    language: 'en',
    aiProvider: 'none',
    ollamaEndpoint: 'http://localhost:11434',
    ollamaModel: 'llama2',
    openaiKey: '',
    geminiKey: ''
};

let appSettings = { ...DEFAULT_SETTINGS };

// Load settings from localStorage
function loadSettings() {
    const savedSettings = localStorage.getItem('musicRecommenderSettings');
    if (savedSettings) {
        appSettings = { ...DEFAULT_SETTINGS, ...JSON.parse(savedSettings) };
    }
    applySettingsToUI();
}

// Apply settings to UI
function applySettingsToUI() {
    // Set language selector
    const languageSelect = document.getElementById('languageSelect');
    if (languageSelect) languageSelect.value = appSettings.language;
    
    const languageSelector = document.getElementById('languageSelector');
    if (languageSelector) languageSelector.value = appSettings.language;
    
    // Set AI provider radio buttons
    const aiProviderRadios = document.getElementsByName('aiProvider');
    aiProviderRadios.forEach(radio => {
        radio.checked = (radio.value === appSettings.aiProvider);
    });
    
    // Set API inputs
    const ollamaEndpoint = document.getElementById('ollamaEndpoint');
    if (ollamaEndpoint) ollamaEndpoint.value = appSettings.ollamaEndpoint;
    
    const ollamaModel = document.getElementById('ollamaModel');
    if (ollamaModel) ollamaModel.value = appSettings.ollamaModel;
    
    const openaiKey = document.getElementById('openaiKey');
    if (openaiKey) openaiKey.value = appSettings.openaiKey;
    
    const geminiKey = document.getElementById('geminiKey');
    if (geminiKey) geminiKey.value = appSettings.geminiKey;
    
    updateAIProvider();
}

// Save settings to localStorage
function saveSettings() {
    // Get values from UI
    appSettings.language = document.getElementById('languageSelect').value;
    
    const aiProviderRadios = document.getElementsByName('aiProvider');
    aiProviderRadios.forEach(radio => {
        if (radio.checked) appSettings.aiProvider = radio.value;
    });
    
    appSettings.ollamaEndpoint = document.getElementById('ollamaEndpoint').value || 'http://localhost:11434';
    appSettings.ollamaModel = document.getElementById('ollamaModel').value || 'llama2';
    appSettings.openaiKey = document.getElementById('openaiKey').value;
    appSettings.geminiKey = document.getElementById('geminiKey').value;
    
    // Save to localStorage
    localStorage.setItem('musicRecommenderSettings', JSON.stringify(appSettings));
    
    alert('Settings saved successfully! ✓');
    closeSettings();
}

// Update AI provider visibility
function updateAIProvider() {
    const aiProviderRadios = document.getElementsByName('aiProvider');
    let selectedProvider = 'none';
    
    aiProviderRadios.forEach(radio => {
        if (radio.checked) selectedProvider = radio.value;
    });
    
    // Hide all provider sections
    const ollamaSettings = document.getElementById('ollamaSettings');
    const openaiSettings = document.getElementById('openaiSettings');
    const geminiSettings = document.getElementById('geminiSettings');
    
    if (ollamaSettings) ollamaSettings.style.display = 'none';
    if (openaiSettings) openaiSettings.style.display = 'none';
    if (geminiSettings) geminiSettings.style.display = 'none';
    
    // Show selected provider settings
    if (selectedProvider === 'ollama' && ollamaSettings) {
        ollamaSettings.style.display = 'block';
    } else if (selectedProvider === 'openai' && openaiSettings) {
        openaiSettings.style.display = 'block';
    } else if (selectedProvider === 'gemini' && geminiSettings) {
        geminiSettings.style.display = 'block';
    }
}

// ==========================================
// Modal Functions
// ==========================================

function openSettings() {
    const modal = document.getElementById('settingsModal');
    if (modal) {
        modal.classList.add('show');
    }
}

function closeSettings() {
    const modal = document.getElementById('settingsModal');
    if (modal) {
        modal.classList.remove('show');
    }
}

// Close modal when clicking outside
window.onclick = function(event) {
    const modal = document.getElementById('settingsModal');
    if (event.target === modal) {
        closeSettings();
    }
};

// ==========================================
// AI Integration Functions
// ==========================================

// Call Ollama API
async function callOllamaAPI(prompt) {
    try {
        const response = await fetch(`${appSettings.ollamaEndpoint}/api/generate`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                model: appSettings.ollamaModel,
                prompt: prompt,
                stream: false,
                temperature: 0.7,
                num_predict: 150
            })
        });
        
        if (!response.ok) {
            throw new Error(`Ollama API error: ${response.status}`);
        }
        
        const data = await response.json();
        return data.response;
    } catch (error) {
        console.error('Ollama API error:', error);
        return null;
    }
}

// Call OpenAI API
async function callOpenAIAPI(prompt) {
    try {
        const response = await fetch('https://api.openai.com/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${appSettings.openaiKey}`
            },
            body: JSON.stringify({
                model: 'gpt-3.5-turbo',
                messages: [
                    { role: 'system', content: 'You are a helpful music recommendation assistant.' },
                    { role: 'user', content: prompt }
                ],
                temperature: 0.7,
                max_tokens: 150
            })
        });
        
        if (!response.ok) {
            throw new Error(`OpenAI API error: ${response.status}`);
        }
        
        const data = await response.json();
        return data.choices[0].message.content;
    } catch (error) {
        console.error('OpenAI API error:', error);
        return null;
    }
}

// Call Google Gemini API
async function callGeminiAPI(prompt) {
    try {
        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=${appSettings.geminiKey}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                contents: [
                    {
                        parts: [
                            { text: prompt }
                        ]
                    }
                ],
                generationConfig: {
                    temperature: 0.7,
                    maxOutputTokens: 150
                }
            })
        });
        
        if (!response.ok) {
            throw new Error(`Gemini API error: ${response.status}`);
        }
        
        const data = await response.json();
        return data.candidates[0].content.parts[0].text;
    } catch (error) {
        console.error('Gemini API error:', error);
        return null;
    }
}

// Get AI-powered explanation
async function getAIExplanation(mood, songTitle, artist) {
    if (appSettings.aiProvider === 'none') {
        return null;
    }
    
    const prompt = `Explain in 1-2 sentences why "${songTitle}" by ${artist} is a good match for someone in a "${mood}" mood. Be concise and friendly.`;
    
    let response = null;
    
    if (appSettings.aiProvider === 'ollama') {
        response = await callOllamaAPI(prompt);
    } else if (appSettings.aiProvider === 'openai') {
        response = await callOpenAIAPI(prompt);
    } else if (appSettings.aiProvider === 'gemini') {
        response = await callGeminiAPI(prompt);
    }
    
    return response;
}

// Get related moods
async function getRelatedMoods(mood) {
    if (appSettings.aiProvider === 'none') {
        return null;
    }
    
    const prompt = `List 2-3 moods related to "${mood}" as a comma-separated list. Keep it brief.`;
    
    let response = null;
    
    if (appSettings.aiProvider === 'ollama') {
        response = await callOllamaAPI(prompt);
    } else if (appSettings.aiProvider === 'openai') {
        response = await callOpenAIAPI(prompt);
    } else if (appSettings.aiProvider === 'gemini') {
        response = await callGeminiAPI(prompt);
    }
    
    return response;
}

// Get recommended genres
async function getRecommendedGenres(mood) {
    if (appSettings.aiProvider === 'none') {
        return null;
    }
    
    const prompt = `List 3-4 music genres recommended for someone feeling "${mood}" as a comma-separated list. Keep it brief.`;
    
    let response = null;
    
    if (appSettings.aiProvider === 'ollama') {
        response = await callOllamaAPI(prompt);
    } else if (appSettings.aiProvider === 'openai') {
        response = await callOpenAIAPI(prompt);
    } else if (appSettings.aiProvider === 'gemini') {
        response = await callGeminiAPI(prompt);
    }
    
    return response;
}

// ==========================================
// Main Recommendation Function
// ==========================================

async function getSongs() {
    let mood = document.getElementById("mood").value;
    const trans = translations[currentLanguage] || translations['en'];
    
    // Show loading spinner
    const spinner = document.getElementById('loadingSpinner');
    if (spinner) spinner.classList.add('show');
    
    try {
        // Fetch songs from backend
        const response = await fetch("http://127.0.0.1:5000/recommend/" + mood);
        const data = await response.json();
        
        let output = document.getElementById("output");
        output.innerHTML = "";
        
        if (data.error || !data || data.length === 0) {
            output.innerHTML = `<p>${trans.noSongsFound}</p>`;
            if (spinner) spinner.classList.remove('show');
            return;
        }
        
        // Get AI-powered recommendations if enabled
        let relatedMoods = await getRelatedMoods(mood);
        let recommendedGenres = await getRecommendedGenres(mood);
        
        // Display songs
        for (const song of data) {
            let div = document.createElement("div");
            
            // Get AI explanation for this song
            let explanation = await getAIExplanation(mood, song.title, song.artist);
            
            let htmlContent = `
                <h3>${song.title}</h3>
                <p><strong>${trans.artist}:</strong> ${song.artist}</p>
            `;
            
            if (explanation) {
                htmlContent += `<h4>${trans.explanation}:</h4><p>${explanation}</p>`;
            }
            
            htmlContent += `
                <a href="${song.link}" target="_blank">
                    ${trans.listenYoutube}
                </a>
            `;
            
            div.innerHTML = htmlContent;
            output.appendChild(div);
        }
        
        // Add AI insights at the bottom
        if (relatedMoods || recommendedGenres) {
            let insightsDiv = document.createElement("div");
            insightsDiv.style.gridColumn = "1 / -1";
            
            let insightsContent = "<h3>🎵 Music Insights</h3>";
            
            if (relatedMoods) {
                insightsContent += `<h4>${trans.relatedMoods}:</h4><p>${relatedMoods}</p>`;
            }
            
            if (recommendedGenres) {
                insightsContent += `<h4>${trans.recommendedGenres}:</h4><p>${recommendedGenres}</p>`;
            }
            
            insightsDiv.innerHTML = insightsContent;
            output.appendChild(insightsDiv);
        }
        
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("output").innerHTML =
            `<p>${trans.error}</p>`;
    } finally {
        if (spinner) spinner.classList.remove('show');
    }
}

// ==========================================
// Initialize App
// ==========================================

document.addEventListener('DOMContentLoaded', async function() {
    // Load saved language preference
    const savedLanguage = localStorage.getItem('preferredLanguage') || 'en';
    
    // Load translations
    await loadTranslations('en');
    await loadTranslations('te');
    await loadTranslations('hi');
    
    // Load settings
    loadSettings();
    
    // Set initial language
    await changeLanguage(savedLanguage);
});