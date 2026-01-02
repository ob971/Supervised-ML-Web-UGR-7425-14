# 🚀 Deployment Guide

Complete step-by-step guide to deploy your ML Classification Application to cloud platforms.

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Backend Deployment](#backend-deployment)
  - [Option 1: Render (Recommended)](#option-1-render-recommended)
  - [Option 2: Railway](#option-2-railway)
  - [Option 3: Heroku](#option-3-heroku)
- [Frontend Deployment](#frontend-deployment)
  - [Option 1: Vercel (Recommended)](#option-1-vercel-recommended)
  - [Option 2: Netlify](#option-2-netlify)
- [Post-Deployment Configuration](#post-deployment-configuration)
- [Troubleshooting](#troubleshooting)

## Prerequisites

Before deploying, ensure you have:

- ✅ Trained models (`.pkl` files in `backend/models/`)
- ✅ GitHub repository with your code
- ✅ Accounts on deployment platforms

---

## Backend Deployment

### Option 1: Render (Recommended) ⭐

**Render** is free and easy to use for Python applications.

#### Step 1: Prepare Your Repository

1. Make sure all files are committed to GitHub:
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. Ensure `backend/models/` contains:
   - `logistic_model.pkl`
   - `decision_tree.pkl`
   - `scaler.pkl`

#### Step 2: Create Render Account

1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Connect your GitHub account

#### Step 3: Create Web Service

1. Click **"New +"** → **"Web Service"**
2. Connect your repository
3. Select your repository

#### Step 4: Configure Service

**Settings:**
- **Name**: `ml-classification-backend` (or any name)
- **Environment**: `Python 3`
- **Region**: Choose closest to you
- **Branch**: `main` (or your default branch)

**Build & Deploy:**
- **Build Command**: 
  ```bash
  cd backend && pip install -r requirements.txt
  ```
- **Start Command**: 
  ```bash
  cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT
  ```

**Advanced Settings:**
- **Auto-Deploy**: `Yes` (deploys on every push)

#### Step 5: Deploy

1. Click **"Create Web Service"**
2. Wait for deployment (3-5 minutes)
3. Your backend will be available at: `https://your-app-name.onrender.com`

#### Step 6: Verify Deployment

1. Visit: `https://your-app-name.onrender.com/health`
2. Should return JSON with model status
3. Visit: `https://your-app-name.onrender.com/docs` for API docs

---

### Option 2: Railway

**Railway** is another excellent option with automatic detection.

#### Step 1: Create Railway Account

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub

#### Step 2: Create New Project

1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Choose your repository

#### Step 3: Configure Service

Railway auto-detects Python projects. You may need to:

1. **Set Root Directory**: `backend`
2. **Add Start Command** (in Settings → Deploy):
   ```bash
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

#### Step 4: Add Environment Variables (if needed)

- `PORT`: Automatically set by Railway
- Add any other variables in Settings → Variables

#### Step 5: Deploy

1. Railway will automatically deploy
2. Get your URL from the service dashboard
3. Format: `https://your-app-name.up.railway.app`

---

### Option 3: Heroku

**Heroku** requires a `Procfile` for Python apps.

#### Step 1: Create Procfile

Create `backend/Procfile`:
```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

#### Step 2: Create runtime.txt

Create `backend/runtime.txt`:
```
python-3.11.0
```

#### Step 3: Deploy to Heroku

```bash
# Install Heroku CLI
# Login
heroku login

# Create app
cd backend
heroku create your-app-name

# Deploy
git push heroku main

# Open app
heroku open
```

---

## Frontend Deployment

### Option 1: Vercel (Recommended) ⭐

**Vercel** is perfect for static sites and has excellent GitHub integration.

#### Step 1: Prepare Frontend

Update `frontend/index.html` to use your deployed backend URL:

```javascript
// Find this line (around line 419)
<input type="text" id="apiUrl" value="http://localhost:8000" placeholder="http://localhost:8000">

// Change to your deployed backend URL
<input type="text" id="apiUrl" value="https://your-backend.onrender.com" placeholder="https://your-backend.onrender.com">
```

Or keep it configurable (users can change it).

#### Step 2: Create Vercel Account

1. Go to [vercel.com](https://vercel.com)
2. Sign up with GitHub

#### Step 3: Import Project

1. Click **"Add New..."** → **"Project"**
2. Import your GitHub repository
3. Select the repository

#### Step 4: Configure Project

**Project Settings:**
- **Framework Preset**: `Other`
- **Root Directory**: `frontend`
- **Build Command**: (leave empty - it's a static site)
- **Output Directory**: `.` (current directory)
- **Install Command**: (leave empty)

**Environment Variables:**
- Not needed for this simple setup

#### Step 5: Deploy

1. Click **"Deploy"**
2. Wait 1-2 minutes
3. Your frontend will be live at: `https://your-project.vercel.app`

#### Step 6: Update API URL (if hardcoded)

If you hardcoded the backend URL, update it in the deployed version or use environment variables.

---

### Option 2: Netlify

**Netlify** is another great option for static sites.

#### Step 1: Create Netlify Account

1. Go to [netlify.com](https://netlify.com)
2. Sign up with GitHub

#### Step 2: Deploy Site

1. Click **"Add new site"** → **"Import an existing project"**
2. Connect to GitHub
3. Select your repository

#### Step 3: Configure Build

**Build settings:**
- **Base directory**: `frontend`
- **Build command**: (leave empty)
- **Publish directory**: `frontend`

#### Step 4: Deploy

1. Click **"Deploy site"**
2. Your site will be live at: `https://random-name.netlify.app`
3. You can change the site name in Site settings

---

## Post-Deployment Configuration

### 1. Update CORS in Backend

If you hardcoded CORS origins, update `backend/main.py`:

```python
# Change this line
allow_origins=["*"]  # For development

# To this (replace with your frontend URL)
allow_origins=["https://your-frontend.vercel.app"]
```

Then redeploy the backend.

### 2. Update Frontend API URL

**Option A: Hardcode (Simple)**
- Edit `frontend/index.html`
- Change default API URL
- Redeploy frontend

**Option B: Environment Variable (Advanced)**
- Use a build tool like Vite
- Or keep it configurable in the UI (current implementation)

### 3. Test the Full Stack

1. Open your frontend URL
2. Enter test values
3. Click "Get Predictions"
4. Verify both models return predictions

---

## Troubleshooting

### Backend Issues

#### ❌ "Models not loaded" Error

**Solution:**
1. Ensure `.pkl` files are in `backend/models/`
2. Check file paths in `main.py`
3. Verify files are committed to Git (if not in `.gitignore`)
4. Check build logs for errors

#### ❌ Port Issues

**Solution:**
- Use `$PORT` environment variable (Render/Railway set this automatically)
- Don't hardcode port numbers

#### ❌ Import Errors

**Solution:**
- Check `requirements.txt` includes all dependencies
- Verify Python version compatibility
- Check build logs for missing packages

### Frontend Issues

#### ❌ CORS Error

**Solution:**
1. Update CORS in backend to include frontend URL
2. Redeploy backend
3. Clear browser cache

#### ❌ API Connection Failed

**Solution:**
1. Verify backend URL is correct
2. Check backend is running (visit `/health` endpoint)
3. Ensure backend allows CORS from your frontend domain
4. Check browser console for detailed errors

#### ❌ 404 on Frontend

**Solution:**
- Ensure `index.html` is in the root of `frontend/` directory
- Check Vercel/Netlify build settings

### General Issues

#### ❌ Build Fails

**Solution:**
1. Check build logs for specific errors
2. Verify all dependencies in `requirements.txt`
3. Ensure Python version is compatible
4. Check file paths are correct

#### ❌ Models Not Found After Deployment

**Solution:**
1. Models must be in `backend/models/` directory
2. Commit models to Git (or use a storage service)
3. Check `.gitignore` doesn't exclude `.pkl` files
4. Verify models are copied during build

---

## Quick Deployment Checklist

### Backend
- [ ] Models trained and `.pkl` files in `backend/models/`
- [ ] `requirements.txt` includes all dependencies
- [ ] Backend tested locally
- [ ] Repository pushed to GitHub
- [ ] Deployed to Render/Railway/Heroku
- [ ] Health endpoint works (`/health`)
- [ ] API docs accessible (`/docs`)

### Frontend
- [ ] Frontend tested locally
- [ ] API URL updated (or configurable)
- [ ] Repository pushed to GitHub
- [ ] Deployed to Vercel/Netlify
- [ ] Frontend connects to backend
- [ ] Predictions work end-to-end

### Post-Deployment
- [ ] CORS configured correctly
- [ ] Both URLs working
- [ ] Full stack tested
- [ ] Documentation updated with live URLs

---

## Example Deployment URLs

After deployment, you'll have:

- **Backend**: `https://ml-classification-backend.onrender.com`
- **Frontend**: `https://ml-classification-app.vercel.app`

Update these in your documentation and README!

---

## Need Help?

- Check platform-specific documentation:
  - [Render Docs](https://render.com/docs)
  - [Railway Docs](https://docs.railway.app)
  - [Vercel Docs](https://vercel.com/docs)
  - [Netlify Docs](https://docs.netlify.com)

- Review build logs for specific errors
- Test locally first before deploying
- Use `/health` endpoint to verify backend status

---

**Happy Deploying! 🚀**

