# 👨‍💻 Developer's Implementation Guide

## Code Architecture Overview

```
Frontend (HTML/CSS/JS)
        ↓
   Translation Layer (i18n)
        ↓
   Settings Management
        ↓
   AI Integration Layer
        ↓
   Backend API (Flask)
        ↓
   Song Database
```

---

## Frontend Architecture

### 1. Translation System (i18n Module)

**File:** `frontend/script.js` (Lines 1-100)

#### Key Functions:

```javascript
// Load translation file for specific language
async function loadTranslations(lang) {
  const response = await fetch(`./translations/${lang}.json`);
  translations[lang] = await response.json();
}

// Change language and update UI
async function changeLanguage(lang) {
  currentLanguage = lang;
  const trans = await loadTranslations(lang);
  updateUIText(trans);
  localStorage.setItem('preferredLanguage', lang);
}

// Update all UI text elements
function updateUIText(trans) {
  document.getElementById('title').textContent = trans.title;
  document.getElementById('selectMoodLabel').textContent = trans.selectMood;
  // ... updates for all UI elements
}
```

#### How It Works:

1. **Loading:** Translations loaded from JSON files
2. **Caching:** Translations stored in memory
3. **Switching:** Language changed dynamically without reload
4. **Persistence:** User preference saved in localStorage
5. **Initialization:** On page load, saved language is restored

#### Translation File Structure:

```json
{
  "key": "English Value",
  "mood": "Mood",
  "happy": "Happy 😊",
  // ... more key-value pairs
}
```

#### Adding New Language:

1. Create `translations/xx.json` (replace xx with language code)
2. Copy all keys from `en.json`
3. Translate all values
4. Add option to HTML: `<option value="xx">Language Name</option>`

---

### 2. Settings Management System

**File:** `frontend/script.js` (Lines 102-240)

#### Key Data Structure:

```javascript
const DEFAULT_SETTINGS = {
  language: 'en',              // Currently selected language
  aiProvider: 'none',          // none|ollama|openai|gemini
  ollamaEndpoint: 'http://localhost:11434',
  ollamaModel: 'llama2',
  openaiKey: '',
  geminiKey: ''
};

let appSettings = { ...DEFAULT_SETTINGS };
```

#### Key Functions:

```javascript
// Load settings from localStorage
function loadSettings() {
  const saved = localStorage.getItem('musicRecommenderSettings');
  appSettings = JSON.parse(saved) || DEFAULT_SETTINGS;
  applySettingsToUI();
}

// Save settings to localStorage
function saveSettings() {
  // Collect values from UI
  appSettings.language = document.getElementById('languageSelect').value;
  appSettings.aiProvider = getSelectedProvider();
  appSettings.openaiKey = document.getElementById('openaiKey').value;
  
  // Save to localStorage
  localStorage.setItem('musicRecommenderSettings', JSON.stringify(appSettings));
}

// Show/hide provider sections based on selection
function updateAIProvider() {
  const provider = getSelectedAIProvider();
  
  // Hide all sections
  document.getElementById('ollamaSettings').style.display = 'none';
  document.getElementById('openaiSettings').style.display = 'none';
  
  // Show selected section
  if (provider === 'ollama') {
    document.getElementById('ollamaSettings').style.display = 'block';
  }
}
```

#### Settings Storage:

**Location:** Browser's localStorage
**Key:** `musicRecommenderSettings`
**Format:** JSON string

```javascript
localStorage.setItem('musicRecommenderSettings', JSON.stringify({
  language: 'en',
  aiProvider: 'ollama',
  ollamaEndpoint: 'http://localhost:11434',
  ollamaModel: 'llama2',
  openaiKey: 'sk-...',
  geminiKey: 'AIza...'
}));
```

---

### 3. AI Integration System

**File:** `frontend/script.js` (Lines 242-410)

#### API Callers:

**Ollama:**
```javascript
async function callOllamaAPI(prompt) {
  const response = await fetch(
    `${appSettings.ollamaEndpoint}/api/generate`,
    {
      method: 'POST',
      body: JSON.stringify({
        model: appSettings.ollamaModel,
        prompt: prompt,
        stream: false,
        temperature: 0.7,
        num_predict: 150
      })
    }
  );
  const data = await response.json();
  return data.response;
}
```

**OpenAI:**
```javascript
async function callOpenAIAPI(prompt) {
  const response = await fetch(
    'https://api.openai.com/v1/chat/completions',
    {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${appSettings.openaiKey}`
      },
      body: JSON.stringify({
        model: 'gpt-3.5-turbo',
        messages: [
          { role: 'user', content: prompt }
        ],
        temperature: 0.7,
        max_tokens: 150
      })
    }
  );
  const data = await response.json();
  return data.choices[0].message.content;
}
```

**Google Gemini:**
```javascript
async function callGeminiAPI(prompt) {
  const response = await fetch(
    `https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=${appSettings.geminiKey}`,
    {
      method: 'POST',
      body: JSON.stringify({
        contents: [{ parts: [{ text: prompt }] }],
        generationConfig: {
          temperature: 0.7,
          maxOutputTokens: 150
        }
      })
    }
  );
  const data = await response.json();
  return data.candidates[0].content.parts[0].text;
}
```

#### AI Feature Functions:

**Get Explanation:**
```javascript
async function getAIExplanation(mood, songTitle, artist) {
  const prompt = `Explain why "${songTitle}" by ${artist} 
                 matches "${mood}" mood in 1-2 sentences.`;
  
  // Call appropriate API based on provider
  if (appSettings.aiProvider === 'ollama') {
    return await callOllamaAPI(prompt);
  }
  // ... other providers
}
```

**Get Related Moods:**
```javascript
async function getRelatedMoods(mood) {
  const prompt = `List 2-3 moods related to "${mood}" 
                 as comma-separated list.`;
  
  return await callSelectedAPI(prompt);
}
```

**Get Recommended Genres:**
```javascript
async function getRecommendedGenres(mood) {
  const prompt = `List 3-4 music genres for "${mood}" mood 
                 as comma-separated list.`;
  
  return await callSelectedAPI(prompt);
}
```

#### Error Handling:

```javascript
try {
  const response = await fetch(apiEndpoint);
  if (!response.ok) {
    throw new Error(`API error: ${response.status}`);
  }
  const data = await response.json();
  return data.result;
} catch (error) {
  console.error('API Error:', error);
  return null;  // Graceful fallback
}
```

---

### 4. Main Recommendation Function

**File:** `frontend/script.js` (Lines 412-480)

#### Flow:

```
getSongs() called
    ↓
Get mood from dropdown
    ↓
Show loading spinner
    ↓
Fetch songs from backend API
    ↓
For each song:
  - If AI enabled: Get AI explanation
  - Display song card
    ↓
Get AI insights (related moods, genres)
    ↓
Display all results
    ↓
Hide loading spinner
```

#### Code:

```javascript
async function getSongs() {
  // 1. Get user's mood selection
  const mood = document.getElementById("mood").value;
  const trans = translations[currentLanguage];
  
  // 2. Show loading spinner
  const spinner = document.getElementById('loadingSpinner');
  spinner.classList.add('show');
  
  try {
    // 3. Fetch songs from backend
    const response = await fetch(
      `http://127.0.0.1:5000/recommend/${mood}`
    );
    const data = await response.json();
    
    // 4. Get AI recommendations if enabled
    let relatedMoods = await getRelatedMoods(mood);
    let genres = await getRecommendedGenres(mood);
    
    // 5. Display each song
    for (const song of data) {
      let explanation = await getAIExplanation(
        mood, 
        song.title, 
        song.artist
      );
      
      // Create and append song card
      createSongCard(song, explanation);
    }
    
    // 6. Display AI insights
    if (relatedMoods || genres) {
      displayInsights(relatedMoods, genres);
    }
    
  } catch (error) {
    showError(error);
  } finally {
    spinner.classList.remove('show');
  }
}
```

---

### 5. Modal System

**File:** `frontend/script.js` (Lines 224-240)

#### Functions:

```javascript
// Open settings modal
function openSettings() {
  document.getElementById('settingsModal').classList.add('show');
}

// Close settings modal
function closeSettings() {
  document.getElementById('settingsModal').classList.remove('show');
}

// Close modal when clicking outside
window.onclick = function(event) {
  const modal = document.getElementById('settingsModal');
  if (event.target === modal) {
    closeSettings();
  }
};
```

#### CSS Classes:

```css
.modal {
  display: none;  /* Hidden by default */
  position: fixed;
  z-index: 1000;
}

.modal.show {
  display: flex;  /* Show when .show class added */
  align-items: center;
  justify-content: center;
}
```

---

## Backend Architecture

### Flask Application

**File:** `backend/app.py`

#### Setup:

```python
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access
```

#### Endpoints:

**GET `/`**
```python
@app.route("/")
def home():
    return "🎵 Mood-Based Music API is running!"
```

**GET `/recommend/<mood>`**
```python
@app.route("/recommend/<mood>")
def recommend(mood):
    mood = mood.capitalize()
    
    if mood not in songs:
        return jsonify({"error": "Mood not found"}), 404
    
    return jsonify(songs[mood])
```

#### Response Format:

```json
[
  {
    "title": "Song Title",
    "artist": "Artist Name",
    "link": "https://www.youtube.com/results?search_query=..."
  },
  // ... more songs
]
```

---

## HTML Structure

**File:** `frontend/index.html`

### Key Elements:

```html
<!-- Header with language selector and settings button -->
<header>
  <h1 id="title">Title (translated)</h1>
  <select id="languageSelector" onchange="changeLanguage(this.value)">
    <option value="en">English</option>
    <option value="te">Telugu</option>
    <option value="hi">Hindi</option>
  </select>
  <button id="settingsBtn" onclick="openSettings()">⚙️</button>
</header>

<!-- Main content -->
<main>
  <select id="mood">
    <!-- Mood options with IDs for translation -->
  </select>
  <button onclick="getSongs()">Get Recommendations</button>
  <div id="output" class="output-container"></div>
</main>

<!-- Settings modal -->
<div id="settingsModal" class="modal">
  <div class="modal-content">
    <!-- Language settings -->
    <!-- AI provider selection -->
    <!-- Provider-specific settings -->
    <!-- Save/Close buttons -->
  </div>
</div>

<!-- Loading spinner -->
<div id="loadingSpinner" class="loading-spinner">
  <div class="spinner"></div>
  <p id="loadingText">Loading...</p>
</div>
```

---

## CSS Architecture

**File:** `frontend/style.css`

### Key Sections:

#### 1. Global Styles
```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Segoe UI', sans-serif;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

#### 2. Header
```css
header {
  background-color: rgba(0, 0, 0, 0.7);
  position: sticky;
  top: 0;
  z-index: 100;
}

.header-controls {
  display: flex;
  gap: 15px;
}
```

#### 3. Main Content
```css
.container {
  max-width: 900px;
  margin: 40px auto;
}

.mood-selector {
  background: white;
  padding: 30px;
  border-radius: 15px;
}
```

#### 4. Output Grid
```css
.output-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.output-container > div {
  background: white;
  padding: 25px;
  border-radius: 15px;
  transition: all 0.3s ease;
}

.output-container > div:hover {
  transform: translateY(-5px);
}
```

#### 5. Modal
```css
.modal {
  display: none;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
}

.modal.show {
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background: white;
  padding: 30px;
  border-radius: 15px;
  max-width: 600px;
  max-height: 90vh;
  overflow-y: auto;
}
```

#### 6. Responsive Design
```css
@media (max-width: 768px) {
  .output-container {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .header-controls {
    flex-direction: column;
  }
}
```

---

## Data Flow Diagram

```
User selects mood
        ↓
Clicks "Get Recommendations"
        ↓
getSongs() function triggered
        ↓
Fetch from /recommend/<mood>
        ↓
Backend returns song array
        ↓
For each song, if AI enabled:
  - Get AI explanation
  - Display with explanation
        ↓
Get related moods (if AI enabled)
        ↓
Get recommended genres (if AI enabled)
        ↓
Display insights section
        ↓
Hide loading spinner
        ↓
User can see results
```

---

## Extension Points

### Adding New AI Provider:

1. **Create API caller:**
```javascript
async function callNewProviderAPI(prompt) {
  // Make API call
  // Return response
}
```

2. **Add to feature functions:**
```javascript
async function getAIExplanation(mood, song, artist) {
  if (appSettings.aiProvider === 'newprovider') {
    return await callNewProviderAPI(prompt);
  }
}
```

3. **Add UI options:**
```html
<label>
  <input type="radio" name="aiProvider" value="newprovider">
  New Provider
</label>
```

4. **Add settings section:**
```html
<div id="newproviderSettings" style="display:none;">
  <input type="text" id="newproviderKey" placeholder="API Key">
</div>
```

### Adding New Language:

1. Create `translations/xx.json`
2. Add all keys with translations
3. Add HTML option: `<option value="xx">Language</option>`

### Adding New Moods:

1. Add to backend `songs` dictionary
2. Add mood option to HTML select
3. Add translation for mood name

---

## Testing Checklist

- [ ] Language switching works
- [ ] Settings save and persist
- [ ] AI providers switch correctly
- [ ] Ollama integration works
- [ ] OpenAI integration works
- [ ] Gemini integration works
- [ ] Song recommendations display
- [ ] UI is responsive on mobile
- [ ] Loading spinner appears during AI calls
- [ ] Error handling works gracefully
- [ ] localStorage is used correctly
- [ ] No console errors

---

## Performance Tips

1. **Lazy Load Translations:** Load only active language
2. **Cache API Responses:** Don't re-fetch same mood
3. **Debounce Settings Changes:** Batch localStorage writes
4. **Optimize CSS:** Use CSS Grid for efficiency
5. **Minimize API Calls:** Only call AI when needed

---

## Security Best Practices

1. **API Keys:** Never hardcode keys
2. **CORS:** Only allow trusted origins
3. **Input Validation:** Validate all user inputs
4. **Error Messages:** Don't expose sensitive info
5. **HTTPS:** Use in production
6. **Content Security Policy:** Implement CSP headers

---

**For complete documentation, see README.md**
