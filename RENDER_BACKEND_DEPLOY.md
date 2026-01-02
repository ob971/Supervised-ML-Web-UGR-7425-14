# 🚀 Deploy Backend to Render - Step by Step Guide

## 📋 Complete Configuration for Render Web Service

Based on your Render setup, here are the **exact values** to fill in:

---

## ✅ Field-by-Field Configuration

### 1. **Name**
```
ml-classification-backend
```
**OR any unique name like:**
```
supervised-ml-backend
ml-backend-api
classification-backend
```

**⚠️ Important:** The name must be **unique** on Render. If you see "Name is already in use", try a different name.

**Why:** This will be part of your backend URL: `https://your-name.onrender.com`

---

### 2. **Project (Optional)**
**Leave this EMPTY** - Skip it

You can add it to a project later if needed.

---

### 3. **Language**
```
Python 3
```
✅ Keep this as is (should already be selected)

---

### 4. **Branch**
```
main
```
✅ Keep this as is (should already be selected)

---

### 5. **Region**
```
Oregon (US West)
```
✅ Keep this as is (or choose closest to you)

**Other options:**
- Singapore (Asia Pacific)
- Frankfurt (EU Central)
- Ohio (US East)

---

### 6. **Root Directory (IMPORTANT!)**
```
backend
```
**Type exactly:** `backend`

**Why:** This tells Render to look in the `backend/` folder for your Python code (main.py, requirements.txt).

---

## 🔧 Build & Start Commands

After filling the basic fields, you'll see more fields. Here's what to fill:

### **Build Command:**
**Since Root Directory is `backend`, use:**
```bash
pip install -r requirements.txt
```

**Why:** Root Directory already sets the working directory to `backend/`, so you don't need `cd backend`. This installs all Python dependencies from `backend/requirements.txt`.

**⚠️ Important:** If Root Directory is NOT set to `backend`, then use:
```bash
cd backend && pip install -r requirements.txt
```

---

### **Start Command:**
**Since Root Directory is `backend`, use:**
```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

**Why:** Root Directory already sets the working directory to `backend/`, so you don't need `cd backend`. This starts your FastAPI server. `$PORT` is automatically set by Render.

**⚠️ Important:** If Root Directory is NOT set to `backend`, then use:
```bash
cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT
```

---

## 🎯 Complete Configuration Summary

| Field | Value |
|-------|-------|
| **Name** | `ml-classification-backend` (or unique name) |
| **Project** | *(leave empty)* |
| **Language** | `Python 3` |
| **Branch** | `main` |
| **Region** | `Oregon (US West)` (or closest) |
| **Root Directory** | `backend` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn main:app --host 0.0.0.0 --port $PORT` |

---

## ⚠️ IMPORTANT: Environment Variables

You **don't need** any environment variables for basic deployment, but you can add:

### Optional: Python Version
If you want to specify Python version:
- **Name:** `PYTHON_VERSION`
- **Value:** `3.11.0` (or your preferred version)

**Note:** Render usually auto-detects Python version, so this is optional.

---

## 📝 Step-by-Step on Render UI

1. ✅ **Name:** Type `ml-classification-backend` (or unique name)
2. ⏭️ **Project:** Skip (leave empty)
3. ✅ **Language:** `Python 3` (should be selected)
4. ✅ **Branch:** `main` (should be selected)
5. ✅ **Region:** `Oregon (US West)` (or choose closest)
6. 📝 **Root Directory:** Type `backend`
7. 📝 **Build Command:** Type `pip install -r requirements.txt` (NO `cd backend` needed!)
8. 📝 **Start Command:** Type `uvicorn main:app --host 0.0.0.0 --port $PORT` (NO `cd backend` needed!)
9. ⏭️ **Environment Variables:** Skip (not needed for basic setup)
10. ✅ Click **"Create Web Service"**

---

## 🔍 Verify Your File Structure

Make sure your GitHub repo has this structure:
```
your-repo/
  backend/
    main.py              ← Your FastAPI app
    requirements.txt     ← Python dependencies
    models/
      logistic_model.pkl ← Model files
      decision_tree.pkl
      scaler.pkl
  frontend/
    index.html
  ml/
    notebook.ipynb
  README.md
```

**Important:** Make sure `backend/models/` contains all `.pkl` files!

---

## ✅ After Deployment

### 1. Get Your Backend URL
Render will give you a URL like:
```
https://ml-classification-backend.onrender.com
```

### 2. Test Your Backend
1. **Health Check:** `https://ml-classification-backend.onrender.com/health`
   - Should return: `{"status":"healthy","models_loaded":true}`

2. **API Docs:** `https://ml-classification-backend.onrender.com/docs`
   - Should show Swagger UI

3. **Test Prediction:** Use the `/predict` endpoint

### 3. Update Frontend API URL
1. Open `frontend/index.html`
2. Find line ~272
3. Change to your backend URL:
   ```html
   <input type="text" id="apiUrl" value="https://ml-classification-backend.onrender.com">
   ```
4. Commit and push

### 4. Update CORS (Important!)
**Option A: Update in Render Dashboard**
1. Go to your backend service on Render
2. Go to **Settings** → **Environment**
3. Add environment variable (optional, or update code)

**Option B: Update Code (Recommended)**
1. Open `backend/main.py`
2. Find line 24 (CORS configuration)
3. Update to:
   ```python
   allow_origins=[
       "https://supervised-ml-web-ugr-7425-14.onrender.com",  # Your frontend URL
       "http://localhost:3000",
       "*"  # Keep this for now, remove in production
   ]
   ```
4. **Commit and push** to GitHub:
   ```bash
   git add backend/main.py
   git commit -m "Update CORS for frontend"
   git push origin main
   ```
5. Render will **auto-redeploy** (or manually redeploy)

---

## 🆘 Common Issues & Fixes

### ❌ "Name is already in use"
**Problem:** Service name already exists
**Fix:** Use a different unique name like:
- `ml-backend-api`
- `classification-backend-2024`
- `supervised-ml-backend`

### ❌ "Build failed - Module not found"
**Problem:** Missing dependencies
**Fix:** Check `backend/requirements.txt` has all packages:
```
fastapi>=0.104.1
uvicorn[standard]>=0.24.0
pydantic>=2.5.0
scikit-learn>=1.4.0
joblib>=1.3.2
python-multipart>=0.0.6
```

### ❌ "Models not loaded"
**Problem:** Model files not in repo or wrong path
**Fix:** 
1. Make sure `backend/models/*.pkl` files are committed to Git
2. Check `.gitignore` doesn't exclude `.pkl` files
3. Verify files are in `backend/models/` directory

### ❌ "Port already in use"
**Problem:** Wrong start command
**Fix:** Use `$PORT` variable (Render sets it automatically):
```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

### ❌ "Cannot find main.py"
**Problem:** Wrong root directory
**Fix:** Make sure Root Directory is exactly `backend`

---

## 🔐 Security Notes

### For Production:
1. **Update CORS:** Don't use `allow_origins=["*"]` in production
2. **Add API Key:** Consider adding authentication
3. **Environment Variables:** Store secrets in Render Environment Variables, not in code

---

## 📊 Monitoring

After deployment, you can:
1. **View Logs:** Click on your service → **Logs** tab
2. **View Metrics:** See CPU, Memory usage
3. **Redeploy:** Manual redeploy or auto-deploy on Git push

---

## 🎯 Quick Checklist

Before clicking "Create Web Service":

- [ ] Name: Unique name (e.g., `ml-classification-backend`) ✅
- [ ] Language: Python 3 ✅
- [ ] Branch: main ✅
- [ ] Root Directory: `backend` ✅
- [ ] Build Command: `cd backend && pip install -r requirements.txt` ✅
- [ ] Start Command: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT` ✅
- [ ] Model files in `backend/models/` ✅
- [ ] Code pushed to GitHub ✅
- [ ] Ready to deploy! ✅

---

## 📝 Summary

**Fill in Render:**
- Name: `ml-classification-backend` (unique)
- Root Directory: `backend`
- Build Command: `cd backend && pip install -r requirements.txt`
- Start Command: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`

**After deployment:**
- Test: `/health` endpoint
- Update frontend API URL
- Update CORS settings
- Test full application

---

**Your backend will be live in 3-5 minutes!** 🚀

