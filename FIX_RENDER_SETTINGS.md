# 🔧 Fix Render Build Command Error

## ❌ Current Error
```
Running build command 'cd backend && pip install -r requirements.txt'...
bash: line 1: cd: backend: No such file or directory
Build failed 😡
```

## 🔍 Problem
The build command has `cd backend &&` but Root Directory is already set to `backend`, so it's trying to `cd` into a directory that doesn't exist from that context.

---

## ✅ SOLUTION: Update Render Dashboard Settings

**You need to update the settings directly in Render Dashboard** (not just render.yaml):

### Step 1: Go to Render Dashboard
1. Go to https://dashboard.render.com
2. Click on your **backend service** (ml-classification-backend)

### Step 2: Go to Settings
1. Click **Settings** (left sidebar)
2. Scroll to **Build & Deploy** section

### Step 3: Fix Build Command
1. Find **Build Command** field
2. Click **Edit** (pencil icon)
3. **Current (WRONG):**
   ```bash
   cd backend && pip install -r requirements.txt
   ```
4. **Change to (CORRECT):**
   ```bash
   pip install -r requirements.txt
   ```
5. **Remove `cd backend &&` completely!**

### Step 4: Fix Start Command
1. Find **Start Command** field
2. Click **Edit** (pencil icon)
3. **Current (WRONG):**
   ```bash
   cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
4. **Change to (CORRECT):**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
5. **Remove `cd backend &&` completely!**

### Step 5: Verify Root Directory
1. Check **Root Directory** field
2. Should be: `backend`
3. If empty or different, set it to: `backend`

### Step 6: Save and Redeploy
1. Click **Save Changes**
2. Go to **Manual Deploy** → **Deploy latest commit**
3. Watch the logs - should work now!

---

## 🎯 Correct Configuration

| Setting | Value |
|---------|-------|
| **Root Directory** | `backend` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn main:app --host 0.0.0.0 --port $PORT` |

**NO `cd backend &&` in either command!**

---

## ✅ After Fix

You should see in logs:
```
==> Running build command 'pip install -r requirements.txt'...
Collecting fastapi>=0.104.1
...
Successfully installed ...
```

**NOT:**
```
bash: line 1: cd: backend: No such file or directory
```

---

## 📝 Why This Happens

- **Root Directory = `backend`** means Render runs commands FROM the `backend/` directory
- Adding `cd backend &&` tries to go INTO `backend/` again
- But you're already there, so it fails!

**Solution:** Remove `cd backend &&` from commands when Root Directory is set.

---

## 🆘 Still Not Working?

1. **Clear build cache:**
   - Manual Deploy → **Clear build cache & deploy**

2. **Verify Root Directory:**
   - Make sure it's exactly `backend` (not `./backend` or `/backend`)

3. **Check file exists:**
   - Verify `backend/requirements.txt` is in your GitHub repo
   - Check: https://github.com/ob971/Supervised-ML-Web-UGR-7425-14/tree/main/backend

---

**This will fix it!** ✅

