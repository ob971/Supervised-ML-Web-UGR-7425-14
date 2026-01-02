# ⚡ Quick Deployment Guide

## 🎯 Deployment in 3 Steps

### Step 1: Train Models & Prepare ✅

```bash
# 1. Train models using notebook (Google Colab or local)
# 2. Ensure these files exist:
backend/models/logistic_model.pkl
backend/models/decision_tree.pkl
backend/models/scaler.pkl

# 3. Commit everything to GitHub
git add .
git commit -m "Ready for deployment"
git push origin main
```

### Step 2: Deploy Backend 🚀

**Choose ONE platform:**

#### Option A: Render (Easiest) ⭐
1. Go to [render.com](https://render.com) → Sign up with GitHub
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repo
4. Configure:
   - **Build Command**: `cd backend && pip install -r requirements.txt`
   - **Start Command**: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Click **"Create Web Service"**
6. Wait 3-5 minutes → Get URL: `https://your-app.onrender.com`

#### Option B: Railway
1. Go to [railway.app](https://railway.app) → Sign up
2. **"New Project"** → **"Deploy from GitHub repo"**
3. Select your repo
4. Set **Root Directory**: `backend`
5. Deploy → Get URL: `https://your-app.up.railway.app`

#### Option C: Heroku
```bash
cd backend
heroku create your-app-name
git push heroku main
heroku open
```

**✅ Test Backend:**
- Visit: `https://your-backend-url/health`
- Should show: `{"status": "healthy", "models_loaded": true}`

### Step 3: Deploy Frontend 🌐

#### Option A: Vercel (Recommended) ⭐
1. Go to [vercel.com](https://vercel.com) → Sign up with GitHub
2. **"Add New..."** → **"Project"**
3. Import your GitHub repo
4. Configure:
   - **Root Directory**: `frontend`
   - **Framework**: `Other`
   - **Build Command**: (leave empty)
5. Click **"Deploy"**
6. Wait 1-2 minutes → Get URL: `https://your-app.vercel.app`

#### Option B: Netlify
1. Go to [netlify.com](https://netlify.com) → Sign up
2. **"Add new site"** → **"Import an existing project"**
3. Connect GitHub → Select repo
4. **Base directory**: `frontend`
5. **Deploy site**

**✅ Update API URL:**
- Open `frontend/index.html`
- Change line ~419: `value="http://localhost:8000"` 
- To: `value="https://your-backend-url.onrender.com"`
- Commit and push (Vercel auto-deploys)

### Step 4: Test Everything 🧪

1. Open your frontend URL
2. Enter test values
3. Click **"Get Predictions"**
4. ✅ Should see predictions from both models!

---

## 📝 Checklist

Before deploying:
- [ ] Models trained (`.pkl` files exist)
- [ ] Models in `backend/models/` directory
- [ ] Code pushed to GitHub
- [ ] Backend tested locally

After deploying:
- [ ] Backend `/health` endpoint works
- [ ] Backend `/docs` shows API documentation
- [ ] Frontend loads correctly
- [ ] Frontend can connect to backend
- [ ] Predictions work end-to-end

---

## 🔗 Your Deployment URLs

After deployment, update these:

- **Backend**: `https://____________________`
- **Frontend**: `https://____________________`

Add these to your README and project documentation!

---

## 🆘 Common Issues

**"Models not loaded"**
→ Check `backend/models/` has all 3 `.pkl` files

**CORS Error**
→ Update CORS in `backend/main.py` to include frontend URL

**Connection Failed**
→ Verify backend URL is correct in frontend

**For detailed troubleshooting, see [DEPLOYMENT.md](DEPLOYMENT.md)**

---

**Need more details? Read the full [DEPLOYMENT.md](DEPLOYMENT.md) guide!**

