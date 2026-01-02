# 🚀 Render Static Site Configuration for Frontend

## ✅ Correct Settings for Your Frontend

Based on your Render Static Site setup, here are the **correct values**:

---

## 📋 Configuration Values

### **Name:**
```
Supervised-ML-Web-App
```
✅ Keep this as is

---

### **Branch:**
```
main
```
✅ Keep this as is

---

### **Root Directory (IMPORTANT!):**
```
frontend
```
**Why:** This tells Render to look in the `frontend/` folder for your static files.

---

### **Build Command (FIX THIS!):**
**Current (WRONG):** `$ pip install -r requirements.txt`

**Correct (CHOOSE ONE):**

**Option 1 - Empty (Recommended for static HTML):**
```
(leave empty)
```

**Option 2 - Simple echo:**
```
echo "Building static site..."
```

**Why:** Your frontend is static HTML/JS - it doesn't need Python packages. The current command is for backend, not frontend!

---

### **Publish Directory:**
```
.
```
**OR**
```
frontend
```

**Why:** This is where your `index.html` file is located. Since Root Directory is `frontend`, use `.` (current directory) or `frontend`.

---

## 🎯 Complete Configuration Summary

| Field | Value |
|-------|-------|
| **Name** | `Supervised-ML-Web-App` |
| **Branch** | `main` |
| **Root Directory** | `frontend` |
| **Build Command** | *(leave empty)* |
| **Publish Directory** | `.` |

---

## ⚠️ Important: Update API URL First!

**Before deploying**, you need to update the frontend to point to your backend URL:

1. Open `frontend/index.html`
2. Find line ~272 (the API URL input field)
3. Change the default value to your backend URL:
   ```html
   <input type="text" id="apiUrl" value="https://your-backend.onrender.com" placeholder="https://your-backend.onrender.com">
   ```
4. **Commit and push** this change to GitHub
5. Then deploy on Render

---

## 📝 Step-by-Step on Render

1. **Name:** `Supervised-ML-Web-App` ✅
2. **Branch:** `main` ✅
3. **Root Directory:** Type `frontend`
4. **Build Command:** **DELETE** the pip install command, leave it **EMPTY**
5. **Publish Directory:** Type `.` (just a dot)
6. **Environment Variables:** Not needed for static site
7. Click **"Create Static Site"**

---

## 🔍 Verify Your File Structure

Make sure your GitHub repo has this structure:
```
your-repo/
  frontend/
    index.html    ← This is what Render will serve
    (other files if any)
  backend/
    (backend files)
  (other files)
```

---

## ✅ After Deployment

1. **Get your frontend URL:** `https://supervised-ml-web-app.onrender.com`
2. **Test it:** Open the URL in browser
3. **Update backend CORS** to include this URL:
   - In `backend/main.py`, update line 24:
   ```python
   allow_origins=["https://supervised-ml-web-app.onrender.com", "http://localhost:3000"]
   ```
4. **Redeploy backend** if needed

---

## 🆘 Common Issues

### "Build failed"
- **Fix:** Make sure Build Command is **empty** (not the pip install command)

### "Publish directory not found"
- **Fix:** Change Publish Directory to `.` or `frontend`

### "Cannot find index.html"
- **Fix:** Verify Root Directory is `frontend` and Publish Directory is `.`

### Frontend can't connect to backend
- **Fix:** Update API URL in `frontend/index.html` to your backend URL
- **Fix:** Update CORS in backend to allow your frontend URL

---

## 🎯 Quick Fix Checklist

- [ ] Root Directory: `frontend`
- [ ] Build Command: **EMPTY** (delete the pip install line)
- [ ] Publish Directory: `.`
- [ ] Updated API URL in `frontend/index.html` to backend URL
- [ ] Pushed changes to GitHub
- [ ] Clicked "Create Static Site"

---

**That's it! Your frontend will be live in 1-2 minutes!** 🚀

