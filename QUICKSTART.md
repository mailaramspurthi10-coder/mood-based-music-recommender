🚀 QUICK START GUIDE - Mood-Based Music Recommender
====================================================

## ⚡ 5-Minute Setup

### Step 1: Start Backend Server
```bash
cd backend
pip install -r requirements.txt
python app.py
```
Backend will run on: http://127.0.0.1:5000

### Step 2: Start Frontend
```bash
cd frontend
python -m http.server 8000
```
Frontend will run on: http://localhost:8000

### Step 3: Open in Browser
Visit: http://localhost:8000
Select your mood and get music recommendations!

---

## 🎯 Using AI Features (Optional)

### Option A: No AI (Default)
Just select your mood and enjoy basic recommendations - No setup needed!

### Option B: Ollama (Local AI) - RECOMMENDED FOR BEGINNERS

1. **Download & Install Ollama**
   - Visit: https://ollama.ai
   - Download for your OS
   - Install and run

2. **Pull a Model**
   ```bash
   ollama pull llama2
   ```

3. **Start Ollama**
   ```bash
   ollama serve
   ```

4. **Configure in App**
   - Click ⚙️ Settings button
   - Select "Local AI (Ollama)"
   - Keep default settings:
     - Endpoint: http://localhost:11434
     - Model: llama2
   - Click "Save Settings"

### Option C: OpenAI

1. Get API key: https://platform.openai.com/api-keys
2. Click ⚙️ Settings
3. Select "OpenAI"
4. Paste your API key
5. Click "Save Settings"

### Option D: Google Gemini

1. Get API key: https://makersuite.google.com/app/apikey
2. Click ⚙️ Settings
3. Select "Google Gemini"
4. Paste your API key
5. Click "Save Settings"

---

## 🌍 Changing Language

1. Use dropdown in top right of header
2. Choose: English, Telugu, or Hindi
3. All text updates instantly!

---

## 📁 Project Structure

```
mood-based-music-recommender/
├── README.md                    # Full documentation
├── QUICKSTART.md               # This file
├── backend/
│   ├── app.py                  # Flask server
│   └── requirements.txt        # Python packages
└── frontend/
    ├── index.html              # Main UI
    ├── style.css               # Styling
    ├── script.js               # i18n + AI logic
    └── translations/
        ├── en.json            # English
        ├── te.json            # Telugu
        └── hi.json            # Hindi
```

---

## ✨ Features to Explore

✅ Select mood: Happy, Sad, Relaxed, Energetic
✅ Get song recommendations
✅ Click to open songs on YouTube
✅ Switch between 3 languages
✅ Enable AI for smart explanations
✅ Configure AI providers in Settings
✅ Settings saved automatically

---

## 🐛 Quick Troubleshooting

**Backend won't start?**
```bash
# Make sure port 5000 is free
# Try: python app.py
```

**Ollama not connecting?**
- Ensure Ollama is running
- Check: curl http://localhost:11434/api/tags
- Restart Ollama if needed

**Frontend not loading?**
- Open browser console (F12)
- Check for CORS errors
- Try a different port: python -m http.server 8001

**Translations not appearing?**
- Clear browser cache (Ctrl+Shift+Delete)
- Check network tab in DevTools
- Ensure translations/ folder exists

---

## 📚 Learn More

Read the full README.md for:
- Detailed configuration
- Security best practices
- Advanced features
- API documentation
- Development guidelines

---

**Questions? Check README.md for complete documentation!**
