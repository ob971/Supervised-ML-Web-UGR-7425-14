# 🚀 Quick Deployment Guide (5 Minutes)

## Fastest Method: Render (Backend) + Vercel (Frontend)

---

## Step 1: Prepare GitHub Repository (2 minutes)

### 1.1 Push to GitHub
```bash
# If not already on GitHub:
git init
git add .
git commit -m "Ready for deployment"
git branch -M main
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

**Or use GitHub Desktop/GUI to push your code**

---

## Step 2: Deploy Backend to Render (2 minutes)

### 2.1 Create Render Account
1. Go to **https://render.com**
2. Click **"Get Started for Free"**
3. Sign up with **GitHub** (easiest)

### 2.2 Create Web Service
1. Click **"New +"** → **"Web Service"**
2. **Connect** your GitHub repository
3. Select your repository

### 2.3 Configure Settings
**Basic Settings:**
- **Name**: `ml-classification-backend` (or any name)
- **Environment**: `Python 3`
- **Region**: Choose closest to you
- **Branch**: `main`

**Build & Deploy:**
- **Build Command**: 
  ```bash
  cd backend && pip install -r requirements.txt
  ```
- **Start Command**: 
  ```bash
  cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT
  ```

**Advanced:**
- **Auto-Deploy**: `Yes`

### 2.4 Deploy
1. Click **"Create Web Service"**
2. Wait 3-5 minutes
3. **Copy your backend URL**: `https://your-app.onrender.com`

---

## Step 3: Deploy Frontend to Vercel (1 minute)

### 3.1 Create Vercel Account
1. Go to **https://vercel.com**
2. Click **"Sign Up"**
3. Sign up with **GitHub**

### 3.2 Import Project
1. Click **"Add New..."** → **"Project"**
2. **Import** your GitHub repository
3. Select your repository

### 3.3 Configure Settings
- **Framework Preset**: `Other`
- **Root Directory**: `frontend`
- **Build Command**: (leave empty)
- **Output Directory**: `.`
- **Install Command**: (leave empty)

### 3.4 Update API URL
**Before deploying**, update `frontend/index.html`:
1. Find line ~272 (API URL input)
2. Change default value to your Render backend URL:
   ```html
   <input type="text" id="apiUrl" value="https://your-app.onrender.com" placeholder="https://your-app.onrender.com">
   ```
3. **Commit and push** this change

### 3.5 Deploy
1. Click **"Deploy"**
2. Wait 1-2 minutes
3. **Copy your frontend URL**: `https://your-app.vercel.app`

---

## Step 4: Update CORS (Important!)

### 4.1 Update Backend CORS
1. Go to your **Render dashboard**
2. Find your service → **Settings** → **Environment**
3. Or update `backend/main.py`:
   ```python
   allow_origins=["https://your-frontend.vercel.app", "http://localhost:3000"]
   ```
4. **Redeploy** backend

---

## ✅ Done! Your App is Live!

### Your URLs:
- **Frontend**: `https://your-app.vercel.app`
- **Backend**: `https://your-app.onrender.com`
- **API Docs**: `https://your-app.onrender.com/docs`

---

## 🎯 Quick Checklist

- [ ] Code pushed to GitHub
- [ ] Backend deployed to Render
- [ ] Got backend URL
- [ ] Updated frontend API URL
- [ ] Frontend deployed to Vercel
- [ ] Updated CORS in backend
- [ ] Tested live application

---

## ⚡ Even Faster Alternative: Railway (All-in-One)

### Railway (Backend + Frontend together)

1. Go to **https://railway.app**
2. Sign up with GitHub
3. **"New Project"** → **"Deploy from GitHub repo"**
4. Select your repo
5. Railway auto-detects and deploys!

**For frontend**, add a second service:
1. **"New"** → **"GitHub Repo"**
2. Select same repo
3. Set **Root Directory**: `frontend`
4. Deploy!

---

## 🆘 Quick Troubleshooting

### Backend shows "Models not loaded"
- ✅ Models are in `backend/models/` - they'll be deployed
- ✅ Render includes all files from your repo

### CORS Error
- Update `backend/main.py` CORS to include your Vercel URL
- Redeploy backend

### Frontend can't connect
- Verify API URL in frontend matches Render URL
- Check backend is running: `https://your-backend.onrender.com/health`

---

## 📝 Summary

**Fastest Path:**
1. Push to GitHub (2 min)
2. Deploy backend to Render (2 min)
3. Deploy frontend to Vercel (1 min)
4. Update CORS (1 min)

**Total: ~5-6 minutes!** ⚡

---

**Need help? Check `DEPLOYMENT.md` for detailed instructions!**

