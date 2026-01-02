# 🚨 FIX RENDER DASHBOARD SETTINGS NOW

## The Problem
Your `render.yaml` is **CORRECT**, but Render is **ignoring it** and using old dashboard settings.

**Error:**
```
Running build command 'cd backend && pip install -r requirements.txt'...
bash: line 1: cd: backend: No such file or directory
```

## ✅ SOLUTION: Update Render Dashboard

### Step 1: Go to Render Dashboard
1. Open: https://dashboard.render.com
2. **Log in** to your account

### Step 2: Find Your Backend Service
1. Click **Services** in the left menu
2. Find: **ml-classification-backend**
3. **Click on it**

### Step 3: Open Settings
1. Click **Settings** in the left sidebar (under your service name)
2. Scroll down to **Build & Deploy** section

### Step 4: Fix Root Directory
1. Find **Root Directory** field
2. Should say: `backend`
3. If it's **empty** or says something else:
   - Click **Edit** (pencil icon)
   - Type: `backend`
   - Click **Save**

### Step 5: Fix Build Command ⚠️ CRITICAL
1. Find **Build Command** field
2. You'll see: `cd backend && pip install -r requirements.txt`
3. Click **Edit** (pencil icon) next to it
4. **DELETE** everything in the field
5. Type **exactly** this:
   ```
   pip install -r requirements.txt
   ```
6. **DO NOT** include `cd backend &&` - that's the problem!
7. Click **Save**

### Step 6: Fix Start Command ⚠️ CRITICAL
1. Find **Start Command** field
2. You'll see: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
3. Click **Edit** (pencil icon) next to it
4. **DELETE** everything in the field
5. Type **exactly** this:
   ```
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
6. **DO NOT** include `cd backend &&` - that's the problem!
7. Click **Save**

### Step 7: Save All Changes
1. Scroll to the **top** of the Settings page
2. Click **Save Changes** button (if visible)
3. Or just navigate away - changes auto-save

### Step 8: Redeploy
1. Click **Manual Deploy** in the top menu
2. Click **Deploy latest commit**
3. Watch the logs

---

## ✅ What You Should See After Fix

### In Render Dashboard Settings:

**Root Directory:**
```
backend
```

**Build Command:**
```
pip install -r requirements.txt
```
(No `cd backend &&`)

**Start Command:**
```
uvicorn main:app --host 0.0.0.0 --port $PORT
```
(No `cd backend &&`)

---

## ✅ Success Logs (After Fix)

You should see:
```
==> Cloning from https://github.com/ob971/Supervised-ML-Web-UGR-7425-14
==> Checking out commit ...
==> Installing Python version 3.13.4...
==> Using Python version 3.13.4 (default)
==> Running build command 'pip install -r requirements.txt'...
Collecting fastapi>=0.104.1
Collecting uvicorn[standard]>=0.24.0
...
Successfully installed fastapi uvicorn pydantic scikit-learn joblib python-multipart
==> Build succeeded! ✅
```

**NOT:**
```
==> Running build command 'cd backend && pip install -r requirements.txt'...
bash: line 1: cd: backend: No such file or directory
==> Build failed 😞
```

---

## 🔍 Why This Happens

Render dashboard settings **OVERRIDE** `render.yaml` file.

Even though your `render.yaml` is correct:
```yaml
rootDir: backend
buildCommand: pip install -r requirements.txt
startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT
```

Render is using the **old dashboard settings** that still have `cd backend &&`.

**Solution:** Update dashboard settings directly!

---

## 📋 Quick Checklist

- [ ] Opened https://dashboard.render.com
- [ ] Clicked on `ml-classification-backend` service
- [ ] Went to **Settings** → **Build & Deploy**
- [ ] **Root Directory** = `backend`
- [ ] **Build Command** = `pip install -r requirements.txt` (NO `cd backend &&`)
- [ ] **Start Command** = `uvicorn main:app --host 0.0.0.0 --port $PORT` (NO `cd backend &&`)
- [ ] Saved changes
- [ ] Clicked **Manual Deploy** → **Deploy latest commit**
- [ ] Watched logs - should succeed!

---

## 🆘 Still Not Working?

If after fixing you still see the error:

1. **Check if backend is in your GitHub repo:**
   - Go to: https://github.com/ob971/Supervised-ML-Web-UGR-7425-14
   - Verify `backend/` folder exists
   - Verify `backend/main.py` exists
   - Verify `backend/requirements.txt` exists

2. **Check Render is using the right branch:**
   - In Render Settings → **Build & Deploy**
   - **Branch** should be: `main`

3. **Try deleting and recreating the service:**
   - Delete the current backend service
   - Create new Web Service
   - Connect to same GitHub repo
   - Set Root Directory = `backend`
   - Set Build Command = `pip install -r requirements.txt`
   - Set Start Command = `uvicorn main:app --host 0.0.0.0 --port $PORT`

---

**This WILL fix it - just update the dashboard settings!** ✅

