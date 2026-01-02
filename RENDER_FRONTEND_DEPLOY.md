# 🚀 Deploy Frontend to Render - Step by Step Guide

## 📋 Complete Configuration for Render Static Site

Based on your Render setup, here are the **exact values** to fill in:

---

## ✅ Field-by-Field Configuration

### 1. **Name**
```
Supervised-ML-Web-UGR-7425-14
```
✅ Keep this as is (or change to whatever you prefer)

---

### 2. **Branch**
```
main
```
✅ Keep this as is

---

### 3. **Root Directory (IMPORTANT!)**
```
frontend
```
**Type exactly:** `frontend`

**Why:** This tells Render to look in the `frontend/` folder for your static files (index.html).

---

### 4. **Build Command**
**Leave this EMPTY** or use:
```
echo "Building static site..."
```

**Why:** Your frontend is static HTML/JS - it doesn't need to build anything. No npm, no pip, nothing!

**⚠️ DELETE any command that's there** (like `pip install` or `npm install`)

---

### 5. **Publish Directory**
```
.
```
**Type exactly:** `.` (just a dot)

**Why:** Since Root Directory is `frontend`, the publish directory is `.` (current directory) where your `index.html` is located.

---

### 6. **Environment Variables**
**You don't need any environment variables for the frontend!**

Just skip this section - leave it empty.

---

## 🎯 Complete Configuration Summary

| Field | Value |
|-------|-------|
| **Name** | `Supervised-ML-Web-UGR-7425-14` |
| **Branch** | `main` |
| **Root Directory** | `frontend` |
| **Build Command** | *(leave empty)* |
| **Publish Directory** | `.` |
| **Environment Variables** | *(none needed)* |

---

## ⚠️ IMPORTANT: Update API URL First!

**Before clicking "Create Static Site"**, you need to update your frontend to point to your backend URL:

### Step 1: Update frontend/index.html

1. Open `frontend/index.html` in your editor
2. Find line ~272 (look for the API URL input field)
3. Change the default value from `http://localhost:8080` to your Render backend URL:

```html
<input type="text" id="apiUrl" value="https://your-backend-name.onrender.com" placeholder="https://your-backend-name.onrender.com">
```

**Replace `your-backend-name` with your actual backend service name on Render.**

### Step 2: Commit and Push

```bash
git add frontend/index.html
git commit -m "Update API URL for deployment"
git push origin main
```

### Step 3: Then Deploy on Render

Now go back to Render and click **"Create Static Site"**

---

## 📝 Step-by-Step on Render UI

1. ✅ **Name:** Already filled - `Supervised-ML-Web-UGR-7425-14`
2. ✅ **Branch:** Already filled - `main`
3. 📝 **Root Directory:** Type `frontend`
4. 🗑️ **Build Command:** **DELETE** any command, leave it **EMPTY**
5. 📝 **Publish Directory:** Type `.` (just a dot)
6. ⏭️ **Environment Variables:** Skip (don't add any)
7. ✅ Click **"Create Static Site"**

---

## 🔍 Verify Your File Structure

Make sure your GitHub repo has this structure:
```
your-repo/
  frontend/
    index.html    ← Render will serve this
    test-api.html (if you have it)
  backend/
    main.py
    models/
      *.pkl files
  ml/
    notebook.ipynb
  README.md
  (other files)
```

---

## ✅ After Deployment

### 1. Get Your Frontend URL
Render will give you a URL like:
```
https://supervised-ml-web-ugr-7425-14.onrender.com
```

### 2. Update Backend CORS
Go to your **backend service on Render**:
1. Click on your backend service
2. Go to **Settings** → **Environment**
3. Or update `backend/main.py` line 24:
   ```python
   allow_origins=[
       "https://supervised-ml-web-ugr-7425-14.onrender.com",
       "http://localhost:3000"
   ]
   ```
4. **Redeploy** the backend

### 3. Test Your Application
1. Open your frontend URL: `https://supervised-ml-web-ugr-7425-14.onrender.com`
2. Enter test values
3. Click "Get Predictions"
4. Should work! 🎉

---

## 🆘 Common Issues & Fixes

### ❌ "Build failed"
**Problem:** Build command has something in it
**Fix:** Make sure Build Command is **completely empty**

### ❌ "Publish directory not found"
**Problem:** Wrong publish directory
**Fix:** Use `.` (dot) not `frontend` or `build`

### ❌ "Cannot find index.html"
**Problem:** Wrong root directory
**Fix:** Make sure Root Directory is exactly `frontend`

### ❌ Frontend can't connect to backend
**Problem:** API URL not updated or CORS issue
**Fix:** 
1. Check API URL in `frontend/index.html` matches backend URL
2. Update backend CORS to include frontend URL
3. Redeploy both

---

## 🎯 Quick Checklist

Before clicking "Create Static Site":

- [ ] Root Directory: `frontend` ✅
- [ ] Build Command: **EMPTY** ✅
- [ ] Publish Directory: `.` ✅
- [ ] Updated API URL in `frontend/index.html` to backend URL ✅
- [ ] Committed and pushed changes to GitHub ✅
- [ ] Ready to deploy! ✅

---

## 📝 Summary

**Fill in Render:**
- Root Directory: `frontend`
- Build Command: *(empty)*
- Publish Directory: `.`

**Before deploying:**
- Update API URL in `frontend/index.html`
- Push to GitHub

**After deploying:**
- Update backend CORS
- Test the application

---

**That's it! Your frontend will be live in 1-2 minutes!** 🚀

