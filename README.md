# 🎵 Mood-Based Music Recommender

A modern web application that recommends music based on your mood, with support for multiple languages, AI-powered features, and flexible deployment options using local or cloud AI services.

## ✨ Features

### 🌍 Internationalization (i18n) & Localization (l10n)
- **Multi-language Support**: English, Telugu (తెలుగు), Hindi (हिन्दी)
- **Dynamic Language Switching**: Change language without page reload
- **Persistent Preferences**: Your language choice is saved in browser local storage
- **Translations in JSON**: Easy to add more languages

### 🤖 AI-Powered Features
- **Mood Analysis**: Get AI-powered explanations for why songs match your mood
- **Related Moods**: Discover moods related to your current selection
- **Genre Recommendations**: AI suggests music genres that fit your mood
- **Smart Playlist Suggestions**: Personalized recommendations based on mood

### 🔌 Local AI Inference (Ollama)
- Run AI models locally without internet dependency
- **Supported Models**: llama2, mistral, gemma, neural-chat, and others
- **Privacy**: All processing happens on your machine
- **Easy Configuration**: Simple endpoint and model selection in settings

### 🔑 BYOK (Bring Your Own Key)
- **OpenAI Integration**: Use your own API key for GPT-3.5-turbo
- **Google Gemini Integration**: Use your own API key for Gemini
- **Secure Storage**: API keys stored in browser local storage (for demo purposes)
- **Provider Selection**: Easy switching between different AI providers

### 📱 Responsive UI
- Beautiful gradient design with modern aesthetics
- Mobile-friendly interface
- Smooth animations and transitions
- Settings modal for easy configuration
- Loading spinner for better UX

## 📂 Project Structure

```
mood-based-music-recommender/
├── README.md
├── backend/
│   ├── app.py                 # Flask backend server
│   ├── requirement.txt        # Python dependencies
│   ├── recommendation.py      # Recommendation logic
│   └── songs.json            # Song database
└── frontend/
    ├── index.html            # Main HTML file with enhanced UI
    ├── style.css             # Modern responsive CSS
    ├── script.js             # i18n, AI, and settings management
    └── translations/         # Translation files
        ├── en.json          # English translations
        ├── te.json          # Telugu translations
        └── hi.json          # Hindi translations
```

## 🚀 Getting Started

### Prerequisites

**Backend:**
- Python 3.7+
- Flask
- Flask-CORS

**Frontend:**
- Modern web browser (Chrome, Firefox, Safari, Edge)

**For AI Features (Optional):**
- Ollama (for local AI) - [Download](https://ollama.ai)
- OpenAI API Key - [Get Here](https://platform.openai.com/api-keys)
- Google Gemini API Key - [Get Here](https://makersuite.google.com/app/apikey)

### Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd mood-based-music-recommender
   ```

2. **Install Backend Dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Start the Backend Server**
   ```bash
   python app.py
   ```
   The server will run on `http://127.0.0.1:5000`

4. **Open the Frontend**
   ```bash
   # Navigate to the frontend directory
   cd ../frontend
   
   # Open index.html in your browser
   # You can use any local server:
   python -m http.server 8000
   # Then visit http://localhost:8000
   ```

## ⚙️ Configuration

### Language Settings
1. Click the **⚙️ Settings** button in the top right
2. Go to the **Language** section
3. Select your preferred language: English, Telugu, or Hindi
4. Click **Save Settings**

### AI Provider Configuration

#### Option 1: Basic Mode (No AI)
- Default setting - provides basic music recommendations
- No API key required
- Works offline

#### Option 2: Local AI (Ollama)

**Step 1: Install Ollama**
- Download from [ollama.ai](https://ollama.ai)
- Install for your OS (Windows, Mac, Linux)

**Step 2: Pull a Model**
```bash
ollama pull llama2    # or mistral, gemma, neural-chat
```

**Step 3: Start Ollama**
```bash
ollama serve
```
Ollama will run on `http://localhost:11434` by default

**Step 4: Configure in App**
1. Open Settings (⚙️)
2. Select "Local AI (Ollama)" as AI Provider
3. Set:
   - **Ollama Endpoint**: `http://localhost:11434`
   - **Ollama Model**: `llama2` (or your chosen model)
4. Click **Save Settings**

#### Option 3: OpenAI API

**Step 1: Get API Key**
- Visit [OpenAI Platform](https://platform.openai.com/api-keys)
- Create a new API key
- Copy the key

**Step 2: Configure in App**
1. Open Settings (⚙️)
2. Select "OpenAI" as AI Provider
3. Paste your OpenAI API Key
4. Click **Save Settings**

**Cost**: Uses gpt-3.5-turbo model (check OpenAI pricing)

#### Option 4: Google Gemini

**Step 1: Get API Key**
- Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
- Click "Create API Key"
- Copy the key

**Step 2: Configure in App**
1. Open Settings (⚙️)
2. Select "Google Gemini" as AI Provider
3. Paste your Gemini API Key
4. Click **Save Settings**

**Cost**: Free tier available, check Google's pricing

## 🔐 Security & Privacy Notes

### API Key Storage
- API keys are stored in browser's **Local Storage**
- For production use, implement server-side key management
- Never commit API keys to version control
- Consider using environment variables in production

### Data Privacy
- With Ollama: All processing is local, no data sent to servers
- With Cloud APIs: Data is sent to respective providers
- Translation files are loaded from local server
- Song recommendations are basic mood-based matching

## 📖 Usage Guide

### Basic Usage

1. **Select Your Mood**
   - Choose from: Happy 😊, Sad 😢, Relaxed 😌, Energetic ⚡
   - Music recommendations will appear based on your mood

2. **View Recommendations**
   - Each card shows song title, artist, and YouTube link
   - Click "▶ Listen on YouTube" to open in YouTube

3. **With AI Enabled**
   - See personalized explanations for why songs match your mood
   - Discover related moods and recommended music genres
   - Get AI-powered playlist suggestions

### Advanced Features

**Language Switching**
- Use the language dropdown in header or settings
- All text updates instantly
- Your choice is remembered

**AI Provider Switching**
- Test different providers from settings
- Configure multiple providers
- Switch between them anytime

**Settings Persistence**
- All settings saved in browser
- Automatic restoration on page reload
- Clear browser storage to reset

## 🛠️ API Endpoints

### Backend Endpoints

**GET `/`**
- Returns API status message

**GET `/recommend/<mood>`**
- Returns song recommendations for given mood
- Parameters:
  - `mood`: One of `Happy`, `Sad`, `Relaxed`, `Energetic`
- Response: JSON array of songs with title, artist, and YouTube link

### AI API Integrations

**Ollama API**
- Endpoint: `http://localhost:11434/api/generate`
- Model: configurable (llama2, mistral, etc.)
- Method: POST with JSON payload

**OpenAI API**
- Endpoint: `https://api.openai.com/v1/chat/completions`
- Model: gpt-3.5-turbo
- Requires: Bearer token authentication

**Google Gemini API**
- Endpoint: `https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent`
- Requires: API key in query parameter

## 📝 Implementation Details

### i18n/l10n Architecture

**Translation Files** (`translations/*.json`)
```json
{
  "title": "Mood-Based Music Recommender 🎵",
  "selectMood": "Select Your Mood",
  // ... more key-value pairs
}
```

**Dynamic Translation Loading**
```javascript
// Load translations
await loadTranslations('en');
await loadTranslations('te');
await loadTranslations('hi');

// Switch language
await changeLanguage('te');
```

**Persistent Language Preference**
```javascript
// Automatically loads saved language on page load
const savedLanguage = localStorage.getItem('preferredLanguage');
```

### Settings Management

**Default Settings**
```javascript
const DEFAULT_SETTINGS = {
  language: 'en',
  aiProvider: 'none',
  ollamaEndpoint: 'http://localhost:11434',
  ollamaModel: 'llama2',
  openaiKey: '',
  geminiKey: ''
};
```

**Saving & Loading**
```javascript
// Save to localStorage
localStorage.setItem('musicRecommenderSettings', JSON.stringify(settings));

// Load from localStorage
const savedSettings = JSON.parse(localStorage.getItem('musicRecommenderSettings'));
```

### AI Integration Pattern

**Generic AI Caller**
```javascript
async function getAIExplanation(mood, song, artist) {
  const prompt = `Explain why "${song}" matches "${mood}" mood.`;
  
  if (appSettings.aiProvider === 'ollama') {
    return await callOllamaAPI(prompt);
  } else if (appSettings.aiProvider === 'openai') {
    return await callOpenAIAPI(prompt);
  } else if (appSettings.aiProvider === 'gemini') {
    return await callGeminiAPI(prompt);
  }
}
```

## 🐛 Troubleshooting

### Backend Server Won't Start
```bash
# Check if port 5000 is in use
netstat -tuln | grep 5000

# Try a different port
python app.py --port 5001
```

### Ollama Connection Issues
```bash
# Check if Ollama is running
curl http://localhost:11434/api/tags

# Restart Ollama
ollama serve
```

### OpenAI API Key Not Working
- Verify key is active in [OpenAI Platform](https://platform.openai.com/account/api-keys)
- Check account has credit
- Ensure no leading/trailing spaces

### Gemini API Key Not Working
- Verify key is created at [Google AI Studio](https://makersuite.google.com/app/apikey)
- Check you're using `AIza...` key, not OAuth key

### Translations Not Loading
- Check browser console for CORS errors
- Ensure translation files are in `frontend/translations/`
- Try clearing browser cache

## 📚 Adding More Languages

1. **Create Translation File**
   ```
   frontend/translations/xx.json
   ```

2. **Add Key-Value Pairs**
   Copy from `en.json` and translate each value

3. **Update HTML Language Options**
   Add new option to language selectors in `index.html`

4. **Test**
   Select new language from dropdown

## 🎓 Learning Resources

- **i18n Concept**: [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Glossary/i18n)
- **Local Storage**: [MDN Local Storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)
- **Ollama Docs**: [ollama.ai](https://ollama.ai)
- **OpenAI API**: [OpenAI Documentation](https://platform.openai.com/docs)
- **Google Gemini**: [Google AI Documentation](https://ai.google.dev)

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 💬 Support & Feedback

For issues, questions, or suggestions:
- Open an GitHub issue
- Check existing documentation
- Review code comments for implementation details

---

**Happy Music Recommending! 🎵**



## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://code.swecha.org/Spurthi_10/mood-based-music-recommender.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://code.swecha.org/Spurthi_10/mood-based-music-recommender/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Set auto-merge](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing (SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thanks to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README

Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
