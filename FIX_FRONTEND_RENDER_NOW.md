# 🚨 URGENT: Fix Frontend Service on Render

## ❌ The Problem

Your **Frontend** is incorrectly configured as a **Web Service (Python)** instead of a **Static Site**.

**Error you're seeing:**
```
Installing Python version 3.13.4...
Running build command 'cd backend && pip install -r requirements.txt'...
bash: line 1: cd: backend: No such file or directory
Build failed 😞
```

**Why this is wrong:**
- Frontend is **static HTML/JS** - it doesn't need Python!
- It's trying to run backend commands
- It should be a **Static Site**, not a Web Service

---

## ✅ SOLUTION: Fix Frontend Service Type

### Option 1: Delete and Recreate (Recommended)

**The frontend service is configured wrong. Delete it and create a new Static Site:**

1. **Go to:** https://dashboard.render.com
2. **Find** your frontend service (probably named `Supervised-ML-Web-UGR-7425-14` or similar)
3. **Click** on it
4. **Click** **Settings** → Scroll to bottom
5. **Click** **Delete Service** (red button at bottom)
6. **Confirm** deletion

### Then Create New Static Site:

1. **Click** **"+ New"** button (top right)
2. **Select** **"Static Site"** (NOT Web Service!)
3. **Connect** your GitHub repo: `ob971/Supervised-ML-Web-UGR-7425-14`
4. **Fill in these EXACT values:**

| Field | Value |
|-------|-------|
| **Name** | `ml-classification-frontend` (or keep existing name) |
| **Branch** | `main` |
| **Root Directory** | `frontend` ⚠️ **CRITICAL!** |
| **Build Command** | *(leave EMPTY)* or `echo "Building static site..."` |
| **Publish Directory** | `.` (just a dot) |

5. **Click** **"Create Static Site"**
6. **Wait 2-3 minutes** for deployment

---

## ✅ Option 2: Update Existing Service (If Possible)

**If Render allows you to change service type:**

1. **Go to:** https://dashboard.render.com
2. **Click** on your frontend service
3. **Click** **Settings**
4. **Look for** **Service Type** or **Runtime** field
5. **Change** from **"Web Service"** to **"Static Site"**
6. **Update** these fields:

   - **Root Directory:** `frontend`
   - **Build Command:** *(delete everything, leave EMPTY)*
   - **Publish Directory:** `.`
   - **Start Command:** *(delete this - not needed for static sites)*

7. **Save** and **Redeploy**

**Note:** Render might not allow changing service type. If so, use **Option 1** (delete and recreate).

---

## 🎯 Correct Configuration Summary

### Frontend Service Should Be:

| Setting | Value |
|---------|-------|
| **Type** | Static Site (NOT Web Service!) |
| **Name** | `ml-classification-frontend` |
| **Branch** | `main` |
| **Root Directory** | `frontend` |
| **Build Command** | *(empty)* |
| **Publish Directory** | `.` |
| **Start Command** | *(not needed - static sites don't have this)* |

### Backend Service Should Be:

| Setting | Value |
|---------|-------|
| **Type** | Web Service |
| **Name** | `ml-classification-backend` |
| **Root Directory** | `backend` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn main:app --host 0.0.0.0 --port $PORT` |

---

## ✅ Success Indicators

**After fixing, you should see:**

```
==> Cloning from https://github.com/ob971/Supervised-ML-Web-UGR-7425-14
==> Checking out commit ...
==> Building static site...
==> Publishing directory: .
==> Build succeeded! ✅
```

**NOT:**
```
Installing Python version...
Running build command 'cd backend && pip install...'
Build failed 😞
```

---

## 📋 Quick Checklist

- [ ] Went to Render Dashboard
- [ ] Found frontend service
- [ ] Deleted the incorrectly configured service
- [ ] Created NEW Static Site (NOT Web Service!)
- [ ] Set Root Directory = `frontend`
- [ ] Set Build Command = *(empty)*
- [ ] Set Publish Directory = `.`
- [ ] Saved and deployed
- [ ] Verified build succeeds (no Python errors)

---

## 🔍 Why This Happened

You probably created the frontend service as a **Web Service** by mistake, or Render auto-detected it as Python because it saw Python files in the repo.

**Solution:** Explicitly create it as a **Static Site** and set Root Directory to `frontend` so it only sees HTML/JS files.

---

**Delete the wrong service and create a Static Site - that's the fix!** ✅

