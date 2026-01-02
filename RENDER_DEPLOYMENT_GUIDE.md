# 🚀 Complete Render Deployment Guide - Frontend & Backend

This guide will walk you through deploying both your **Backend** (FastAPI) and **Frontend** (Static HTML) on Render.

---

## 📋 Prerequisites Checklist

Before starting, make sure:

- [ ] All model files are in `backend/models/`:
  - `logistic_model.pkl`
  - `decision_tree.pkl`
  - `scaler.pkl`
- [ ] Your code is pushed to GitHub
- [ ] You have a Render account (sign up at [render.com](https://render.com) with GitHub)

---

## 🎯 Step 1: Deploy Backend (Web Service)

### 1.1 Create Web Service on Render

1. Go to [render.com](https://render.com) and sign in
2. Click **"+ New"** button (top right)
3. Select **"Web Service"** (NOT Static Site)

### 1.2 Connect GitHub Repository

1. Click **"Connect GitHub"** or **"Connect account"**
2. Authorize Render to access your repositories
3. Select your repository: `ml_Logistic_Regression` (or your repo name)
4. Click **"Connect"**

### 1.3 Configure Backend Settings

Fill in the following configuration:

| Field | Value |
|-------|-------|
| **Name** | `ml-classification-backend` (or any name you prefer) |
| **Region** | Choose closest to you (e.g., `Oregon (US West)`) |
| **Branch** | `main` |
| **Root Directory** | `backend` |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn main:app --host 0.0.0.0 --port $PORT` |
| **Instance Type** | `Free` (or upgrade if needed) |

**Important Settings:**
- **Root Directory**: `backend` (this tells Render where your backend code is)
- **Build Command**: `pip install -r requirements.txt` (installs dependencies)
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT` (starts FastAPI server)

### 1.4 Environment Variables (Optional)

You can add environment variables if needed, but for this project, none are required.

### 1.5 Deploy Backend

1. Click **"Create Web Service"**
2. Wait 3-5 minutes for deployment
3. Render will show build logs - watch for any errors
4. Once deployed, you'll get a URL like: `https://ml-classification-backend.onrender.com`

### 1.6 Test Backend

1. Visit: `https://your-backend-url.onrender.com/health`
2. Should show: `{"status": "healthy", "models_loaded": true}`
3. Visit: `https://your-backend-url.onrender.com/docs` to see API documentation

**✅ Save your backend URL!** You'll need it for the frontend.

---

## 🌐 Step 2: Deploy Frontend (Static Site)

### 2.1 Create Static Site on Render

1. In Render dashboard, click **"+ New"** again
2. Select **"Static Site"** (NOT Web Service)

### 2.2 Connect GitHub Repository

1. Select the same repository: `ml_Logistic_Regression`
2. Click **"Connect"**

### 2.3 Configure Frontend Settings

Fill in the following configuration:

| Field | Value |
|-------|-------|
| **Name** | `ml-classification-frontend` (or any name you prefer) |
| **Branch** | `main` |
| **Root Directory** | `frontend` |
| **Build Command** | *(leave EMPTY)* |
| **Publish Directory** | `.` (just a dot) |

**Important Settings:**
- **Root Directory**: `frontend` (tells Render where your frontend files are)
- **Build Command**: **LEAVE EMPTY** (static HTML doesn't need building)
- **Publish Directory**: `.` (current directory, since Root Directory is already `frontend`)

### 2.4 Deploy Frontend

1. Click **"Create Static Site"**
2. Wait 1-2 minutes for deployment
3. Once deployed, you'll get a URL like: `https://ml-classification-frontend.onrender.com`

---

## 🔗 Step 3: Connect Frontend to Backend

### 3.1 Update Frontend API URL

Before the frontend can connect to your backend, you need to update the default API URL.

1. Open `frontend/index.html` in your code editor
2. Find line **272** (the API URL input field)
3. Change the default value from `http://localhost:8080` to your backend URL:

```html
<!-- BEFORE -->
<input type="text" id="apiUrl" value="http://localhost:8080" placeholder="http://localhost:8080">

<!-- AFTER (replace with your actual backend URL) -->
<input type="text" id="apiUrl" value="https://ml-classification-backend.onrender.com" placeholder="https://ml-classification-backend.onrender.com">
```

4. **Save the file**

### 3.2 Update Backend CORS (Optional but Recommended)

To ensure your frontend can communicate with the backend, update CORS settings:

1. Open `backend/main.py`
2. Find line **24** (CORS configuration)
3. Update to include your frontend URL:

```python
# BEFORE
allow_origins=["*"],  # In production, specify your frontend URL

# AFTER (replace with your actual frontend URL)
allow_origins=[
    "https://ml-classification-frontend.onrender.com",
    "http://localhost:3000",  # Keep for local development
],
```

4. **Save the file**

### 3.3 Commit and Push Changes

```bash
git add frontend/index.html backend/main.py
git commit -m "Update API URL and CORS for Render deployment"
git push origin main
```

**Note:** Render will automatically redeploy when you push to GitHub!

---

## ✅ Step 4: Verify Everything Works

### 4.1 Test Backend

1. Visit: `https://your-backend-url.onrender.com/health`
   - Should show: `{"status": "healthy", "models_loaded": true}`
2. Visit: `https://your-backend-url.onrender.com/docs`
   - Should show FastAPI documentation

### 4.2 Test Frontend

1. Visit: `https://your-frontend-url.onrender.com`
2. The API URL field should show your backend URL
3. Enter test values:
   - Age: 29
   - Glucose: 85
   - BP: 66
   - Skin Thickness: 29
   - Insulin: 0
   - BMI: 26.6
   - Diabetes Pedigree: 0.351
   - Pregnancies: 0
4. Click **"Get Predictions"**
5. ✅ Should see predictions from both models!

---

## 📝 Your Deployment URLs

After deployment, save these URLs:

- **Backend**: `https://____________________.onrender.com`
- **Frontend**: `https://____________________.onrender.com`

---

## 🆘 Troubleshooting

### Backend Issues

**"Models not loaded"**
- Check that all 3 `.pkl` files are in `backend/models/` directory
- Verify files are committed to GitHub
- Check build logs in Render dashboard

**"Build failed"**
- Check that `requirements.txt` exists in `backend/` directory
- Verify Python version (should be 3.11.0)
- Check build logs for specific error messages

**"Service unavailable"**
- Free tier services spin down after 15 minutes of inactivity
- First request after spin-down takes 30-60 seconds
- Consider upgrading to paid plan for always-on service

### Frontend Issues

**"Cannot connect to backend"**
- Verify backend URL is correct in `frontend/index.html`
- Check that backend is deployed and accessible
- Test backend URL directly: `https://your-backend-url.onrender.com/health`
- Check browser console for CORS errors

**"Build failed"**
- Make sure Build Command is **EMPTY** (not `pip install`)
- Verify Root Directory is `frontend`
- Verify Publish Directory is `.`

**"404 Not Found"**
- Check that `index.html` exists in `frontend/` directory
- Verify Root Directory is set to `frontend`
- Verify Publish Directory is `.`

### CORS Errors

If you see CORS errors in browser console:
1. Update `backend/main.py` CORS settings (Step 3.2)
2. Commit and push changes
3. Wait for backend to redeploy
4. Clear browser cache and try again

---

## 🔄 Auto-Deploy

Render automatically redeploys when you push to GitHub! Just:
1. Make changes locally
2. Commit: `git commit -m "Your changes"`
3. Push: `git push origin main`
4. Wait 2-5 minutes for redeployment

---

## 💡 Tips

1. **Free Tier Limitations:**
   - Services spin down after 15 minutes of inactivity
   - First request after spin-down is slow (30-60 seconds)
   - Consider upgrading for production use

2. **Monitoring:**
   - Check Render dashboard for logs
   - Monitor service health
   - Set up alerts if needed

3. **Custom Domains:**
   - You can add custom domains in Render settings
   - Free tier supports custom domains

---

## ✅ Final Checklist

- [ ] Backend deployed and accessible at `/health`
- [ ] Frontend deployed and accessible
- [ ] Frontend API URL updated to backend URL
- [ ] Backend CORS updated to include frontend URL
- [ ] Changes committed and pushed to GitHub
- [ ] Both services redeployed successfully
- [ ] Test predictions work end-to-end

---

**🎉 Congratulations! Your ML Classification App is now live on Render!**

