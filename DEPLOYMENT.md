🚀 DEPLOYMENT & SETUP GUIDE
============================

## Local Development Setup (5 Minutes)

### Prerequisites Check
- ✅ Python 3.7+ installed
- ✅ Modern browser available
- ✅ Text editor or IDE

### Step 1: Start Backend Server (Terminal 1)

```bash
# Navigate to backend folder
cd backend

# Install Python dependencies
pip install -r requirements.txt

# Run Flask server
python app.py
```

**Expected Output:**
```
WARNING in app.run_with_reloader
Running on http://127.0.0.1:5000
```

**Verify:** Open http://127.0.0.1:5000 in browser
Should show: "🎵 Mood-Based Music API is running!"

### Step 2: Start Frontend Server (Terminal 2)

```bash
# Navigate to frontend folder
cd frontend

# Start Python HTTP server
python -m http.server 8000
```

**Expected Output:**
```
Serving HTTP on 0.0.0.0 port 8000
```

**Verify:** Open http://localhost:8000 in browser
Should show: Music recommendation UI

### Step 3: Test Basic Functionality

1. ✅ Select a mood from dropdown
2. ✅ Click "Get Recommendations"
3. ✅ See songs displayed
4. ✅ Click YouTube link to verify

### Step 4: Test Language Switching

1. ✅ Click language dropdown (top right)
2. ✅ Select "Telugu (తెలుగు)"
3. ✅ Verify all text updates to Telugu
4. ✅ Try "Hindi (हिन्दी)"

### Step 5: Setup AI Features (Optional)

#### Without AI (Test Now)
- No setup needed
- Just use the app

#### With Ollama (Recommended)

**Download Ollama:**
1. Visit https://ollama.ai
2. Download for your OS
3. Install and run

**Setup Model:**
```bash
# In terminal, run:
ollama pull llama2

# Then start Ollama:
ollama serve
```

**Configure in App:**
1. Click ⚙️ Settings
2. Select "Local AI (Ollama)"
3. Leave endpoint as: http://localhost:11434
4. Leave model as: llama2
5. Click "Save Settings"

**Test:**
1. Select mood
2. Click "Get Recommendations"
3. See AI explanations for songs

#### With OpenAI

**Get API Key:**
1. Visit https://platform.openai.com/api-keys
2. Sign in or create account
3. Click "Create new secret key"
4. Copy the key (starts with sk-)

**Configure in App:**
1. Click ⚙️ Settings
2. Select "OpenAI"
3. Paste your API key
4. Click "Save Settings"

**Test:**
1. Select mood
2. Click "Get Recommendations"
3. See AI-powered explanations

#### With Google Gemini

**Get API Key:**
1. Visit https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy the key (starts with AIza...)

**Configure in App:**
1. Click ⚙️ Settings
2. Select "Google Gemini"
3. Paste your API key
4. Click "Save Settings"

**Test:**
1. Select mood
2. Click "Get Recommendations"
3. See AI suggestions

---

## Production Deployment

### Server Options

#### Option 1: Heroku (Easy)

**Backend:**
```bash
# In backend folder
echo "Flask==2.0.1" > requirements.txt
echo "Flask-CORS==3.0.10" >> requirements.txt

# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Deploy to Heroku
heroku create your-app-name
git push heroku main
```

**Frontend:**
```bash
# Deploy to GitHub Pages or Netlify
npm run build
# Or use:
netlify deploy --prod --dir=frontend
```

#### Option 2: AWS (Scalable)

**Backend:**
```bash
# Use AWS Elastic Beanstalk
eb init
eb create
eb deploy
```

**Frontend:**
```bash
# Use AWS S3 + CloudFront
aws s3 cp frontend/ s3://your-bucket/ --recursive
```

#### Option 3: Docker (Professional)

**Create Dockerfile:**
```dockerfile
FROM python:3.9
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY backend/ .
CMD ["python", "app.py"]
```

**Build & Run:**
```bash
docker build -t mood-music .
docker run -p 5000:5000 mood-music
```

---

## Performance Optimization

### Frontend Optimization

**1. Minify CSS & JavaScript**
```bash
# Install tools
npm install -g cssnano uglifyjs

# Minify
cssnano style.css -o style.min.css
uglifyjs script.js -o script.min.js

# Update index.html to use minified versions
```

**2. Optimize Images**
```bash
# Compress images
imagemin frontend/images/* --out-dir=frontend/images-optimized
```

**3. Cache Strategies**
```javascript
// Add service worker for offline support
// Cache translations and static files
```

**4. Lazy Load Translations**
```javascript
// Load only active language instead of all 3
```

### Backend Optimization

**1. Add Caching**
```python
from flask_caching import Cache
cache = Cache(app)

@app.route('/recommend/<mood>')
@cache.cached(timeout=3600)
def recommend(mood):
    # Returns cached results for 1 hour
```

**2. Database**
```python
# Replace in-memory songs with database
# Use SQLAlchemy or MongoDB
```

**3. Load Balancing**
```bash
# Use Gunicorn for multiple workers
gunicorn -w 4 app:app
```

---

## Environment Variables

### Create .env file

```bash
# Backend
FLASK_ENV=production
FLASK_DEBUG=0
SECRET_KEY=your-secret-key

# Optional: Backend API key for cloud services
# OPENAI_API_KEY=sk-...
# GEMINI_API_KEY=AIza...
```

### Use in app.py

```python
import os
from dotenv import load_dotenv

load_dotenv()

FLASK_ENV = os.getenv('FLASK_ENV', 'development')
SECRET_KEY = os.getenv('SECRET_KEY')
```

---

## Security Hardening

### 1. HTTPS/SSL
```python
# Use SSL certificates
# Configure in production server
```

### 2. CORS Configuration
```python
# Allow only trusted origins
CORS(app, resources={
    r"/recommend/*": {
        "origins": ["https://yourdomain.com"]
    }
})
```

### 3. Rate Limiting
```python
from flask_limiter import Limiter

limiter = Limiter(app)

@app.route('/recommend/<mood>')
@limiter.limit("100 per hour")
def recommend(mood):
    # Limits to 100 requests per hour
```

### 4. API Key Management
```python
# Never hardcode API keys
# Use environment variables
# Implement server-side proxy for API calls
```

### 5. Input Validation
```python
from werkzeug.utils import secure_filename

@app.route('/recommend/<mood>')
def recommend(mood):
    mood = secure_filename(mood)
    # Validate mood is in allowed list
    if mood not in ['Happy', 'Sad', 'Relaxed', 'Energetic']:
        return {"error": "Invalid mood"}, 400
```

---

## Monitoring & Logging

### Application Logging

```python
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

@app.route('/recommend/<mood>')
def recommend(mood):
    logger.info(f"Recommendation requested for mood: {mood}")
    # ... rest of code
```

### Error Tracking

```python
import sentry_sdk

sentry_sdk.init("your-sentry-dsn")

@app.errorhandler(Exception)
def handle_error(e):
    sentry_sdk.capture_exception(e)
    return {"error": "Internal server error"}, 500
```

---

## Testing

### Frontend Testing

```bash
# Install testing tools
npm install --save-dev jest babel-jest

# Run tests
npm test
```

### Backend Testing

```bash
# Install pytest
pip install pytest

# Create test file: test_app.py
# Run tests
pytest test_app.py
```

### Example Test

```python
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

def test_recommend(client):
    response = client.get('/recommend/Happy')
    assert response.status_code == 200
    data = response.json
    assert len(data) > 0
```

---

## CI/CD Pipeline (GitHub Actions)

### Create .github/workflows/deploy.yml

```yaml
name: Deploy

on:
  push:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - name: Install dependencies
        run: |
          pip install -r backend/requirements.txt
      - name: Run tests
        run: |
          pytest backend/test_app.py

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Heroku
        run: |
          git push https://heroku:${{ secrets.HEROKU_API_KEY }}@git.heroku.com/${{ secrets.HEROKU_APP_NAME }}.git main
```

---

## Troubleshooting Deployment

### Common Issues

**Backend won't start:**
```bash
# Check Python version
python --version  # Should be 3.7+

# Check dependencies
pip list

# Try running with verbose output
python -u app.py
```

**CORS errors:**
```python
# Ensure CORS is properly configured
CORS(app, resources={
    r"/*": {"origins": "*"}
})
```

**Translations not loading:**
```bash
# Verify file paths
ls -la frontend/translations/

# Check server is serving files correctly
curl http://localhost:8000/translations/en.json
```

**AI APIs not working:**
```bash
# Check API keys in Settings
# Verify internet connection
# Check if endpoints are accessible

# Test Ollama:
curl http://localhost:11434/api/tags

# Test OpenAI:
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer YOUR_KEY"
```

---

## Performance Metrics

### Monitor These Metrics

**Frontend:**
- Page load time < 2 seconds
- Time to interactive < 3 seconds
- Lighthouse score > 90

**Backend:**
- Response time < 200ms
- API availability > 99.9%
- CPU usage < 50%
- Memory usage < 500MB

### Tools

```bash
# Frontend performance
npm install -g lighthouse
lighthouse http://localhost:8000

# Backend performance
# Use New Relic, DataDog, or similar
```

---

## Maintenance

### Regular Tasks

**Weekly:**
- Check error logs
- Monitor API usage
- Test all features

**Monthly:**
- Update dependencies
- Review security updates
- Analyze performance metrics

**Quarterly:**
- Full security audit
- Database optimization
- Capacity planning

---

## Documentation for Production

### Runbook

Create RUNBOOK.md with:
- Emergency contacts
- Common issues & solutions
- Rollback procedures
- Database backup procedures

### API Documentation

- Document all endpoints
- Include request/response examples
- Specify error codes
- Version your API

### Deployment Checklist

- [ ] Code reviewed
- [ ] Tests passing
- [ ] Dependencies updated
- [ ] Secrets configured
- [ ] Backups created
- [ ] Monitoring enabled
- [ ] Rollback plan ready

---

## Resources

- **Deployment:** https://www.heroku.com/
- **Monitoring:** https://newrelic.com/
- **Security:** https://owasp.org/
- **Performance:** https://web.dev/
- **CI/CD:** https://github.com/features/actions

---

**Happy deploying! 🚀**
