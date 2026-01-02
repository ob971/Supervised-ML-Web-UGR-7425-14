# 🚨 URGENT: Fix Render Build Command

## ❌ Current Error
```
Running build command 'cd backend && pip install -r requirements.txt'...
bash: line 1: cd: backend: No such file or directory
Build failed 😞
```

## ✅ IMMEDIATE FIX (Do This Now!)

### Step-by-Step in Render Dashboard:

1. **Go to:** https://dashboard.render.com
2. **Click** on your backend service: `ml-classification-backend`
3. **Click** **Settings** (left sidebar)
4. **Scroll** to **Build & Deploy** section

### Fix Build Command:

1. Find **Build Command** field
2. Click the **Edit** button (pencil icon) next to it
3. **DELETE** the entire current command
4. **TYPE** this exactly:
   ```bash
   pip install -r requirements.txt
   ```
5. **DO NOT** include `cd backend &&` - remove it completely!

### Fix Start Command:

1. Find **Start Command** field
2. Click the **Edit** button (pencil icon) next to it
3. **DELETE** the entire current command
4. **TYPE** this exactly:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
5. **DO NOT** include `cd backend &&` - remove it completely!

### Verify Root Directory:

1. Check **Root Directory** field
2. Should be: `backend`
3. If it's empty or different, **change it to:** `backend`

### Save and Redeploy:

1. Click **Save Changes** button
2. Go to **Manual Deploy** (top menu)
3. Click **Deploy latest commit**
4. Watch the logs - should work now!

---

## 🎯 What You Should See After Fix

**Build Command:**
```
pip install -r requirements.txt
```
**NO `cd backend &&`**

**Start Command:**
```
uvicorn main:app --host 0.0.0.0 --port $PORT
```
**NO `cd backend &&`**

**Root Directory:**
```
backend
```

---

## ✅ Success Indicators

After fixing, you should see in logs:
```
==> Running build command 'pip install -r requirements.txt'...
Collecting fastapi>=0.104.1
Collecting uvicorn[standard]>=0.24.0
...
Successfully installed fastapi uvicorn pydantic scikit-learn joblib python-multipart
==> Build succeeded!
```

**NOT:**
```
bash: line 1: cd: backend: No such file or directory
Build failed 😞
```

---

## 🔍 Why This Keeps Happening

Render is **still using the old build command** from when you first created the service. The `render.yaml` file is correct, but Render dashboard settings override it.

**You MUST update the dashboard settings directly!**

---

## 📝 Quick Checklist

- [ ] Went to Render Dashboard
- [ ] Opened backend service settings
- [ ] Found Build Command field
- [ ] Removed `cd backend &&`
- [ ] Changed to: `pip install -r requirements.txt`
- [ ] Found Start Command field
- [ ] Removed `cd backend &&`
- [ ] Changed to: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- [ ] Verified Root Directory = `backend`
- [ ] Saved changes
- [ ] Redeployed

---

**This is the ONLY way to fix it - update Render dashboard settings directly!** ✅

