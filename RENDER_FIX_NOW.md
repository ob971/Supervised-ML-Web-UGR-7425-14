# 🚨 URGENT FIX: Build Command Error

## ❌ Current Error
```
ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'
```

## 🔍 Root Cause
Render is running the build command from the **repository root**, but `requirements.txt` is in the `backend/` folder.

**The build command `pip install -r requirements.txt` is looking in the wrong directory!**

---

## ✅ IMMEDIATE FIX

### Option 1: Update Build Command (Easiest - Do This!)

**In Render Settings → Build & Deploy:**

**Change Build Command FROM:**
```bash
pip install -r requirements.txt
```

**TO:**
```bash
cd backend && pip install -r requirements.txt
```

**Change Start Command FROM:**
```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

**TO:**
```bash
cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT
```

**Root Directory:** Leave it **EMPTY** or set to root (`.`)

---

### Option 2: Set Root Directory (Alternative)

**In Render Settings → Build & Deploy:**

1. **Root Directory:** Set to `backend`
2. **Build Command:** Keep as `pip install -r requirements.txt`
3. **Start Command:** Keep as `uvicorn main:app --host 0.0.0.0 --port $PORT`

---

## 🎯 RECOMMENDED: Use Option 1

**This is the safest and most reliable method.**

### Complete Settings for Option 1:

| Setting | Value |
|---------|-------|
| **Root Directory** | *(leave empty or `.`)* |
| **Build Command** | `cd backend && pip install -r requirements.txt` |
| **Start Command** | `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT` |

---

## 📝 Step-by-Step Fix in Render

1. Go to your backend service on Render
2. Click **Settings** (left sidebar)
3. Scroll to **Build & Deploy** section
4. Find **Build Command** field
5. **Change it to:** `cd backend && pip install -r requirements.txt`
6. Find **Start Command** field
7. **Change it to:** `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
8. **Root Directory:** Make sure it's **EMPTY** or set to `.`
9. Click **Save Changes**
10. Go to **Manual Deploy** → **Deploy latest commit**

---

## ✅ Verify After Fix

After redeploying, check the logs. You should see:
```
==> Running build command 'cd backend && pip install -r requirements.txt'...
Collecting fastapi>=0.104.1
Collecting uvicorn[standard]>=0.24.0
...
Successfully installed ...
```

**NOT:**
```
ERROR: Could not open requirements file
```

---

## 🔍 Why This Happens

Render clones your repo to the root directory. When you run `pip install -r requirements.txt`, it looks for the file in the root, but your file is in `backend/requirements.txt`.

By using `cd backend &&`, you:
1. Change to the `backend/` directory
2. Then run the command from there
3. Now it finds `requirements.txt` correctly

---

## 🆘 Still Not Working?

### Check File Path in Git
```bash
git ls-files backend/requirements.txt
```

If this returns nothing, the file isn't committed:
```bash
git add backend/requirements.txt
git commit -m "Add requirements.txt"
git push origin main
```

### Check Render Logs
Look at the full build log to see:
- What directory it's running from
- What files are available
- The exact error message

---

## 📋 Quick Checklist

- [ ] Build Command: `cd backend && pip install -r requirements.txt`
- [ ] Start Command: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
- [ ] Root Directory: Empty or `.`
- [ ] Saved changes in Render
- [ ] Redeployed service
- [ ] Checked build logs for success

---

## 🎯 Summary

**The fix is simple:**
- Add `cd backend &&` before both commands
- This ensures commands run from the correct directory
- Save and redeploy

**This will fix the issue immediately!** ✅

