# ⚡ Render Quick Start - Deploy Now!

## 🎯 Right Now: You're Creating Frontend Static Site

### Current Form Values (Fill These In):

| Field | Value to Enter |
|-------|----------------|
| **Name** | `ml-classification-frontend` (or keep `Supervised-ML-Web-UGR-7425-14`) |
| **Branch** | `main` ✅ |
| **Root Directory** | `frontend` ⚠️ **IMPORTANT!** |
| **Build Command** | *(DELETE everything, leave EMPTY)* ⚠️ **CRITICAL!** |
| **Publish Directory** | `.` (just a dot) |

### ⚠️ Before You Click "Create Static Site":

**STOP!** You need to deploy the **Backend first**, then update the frontend with the backend URL.

---

## 📋 Complete Deployment Order

### Step 1: Deploy Backend First ⚡

1. **Go back to Render Dashboard**
2. Click **"+ New"** → **"Web Service"** (NOT Static Site)
3. Connect your GitHub repo
4. Configure:
   - **Name**: `ml-classification-backend`
   - **Root Directory**: `backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Click **"Create Web Service"**
6. **Wait 3-5 minutes** → Get URL: `https://ml-classification-backend.onrender.com`
7. **Test**: Visit `https://your-backend-url.onrender.com/health`

### Step 2: Update Frontend Code

Before deploying frontend, update the API URL:

1. Open `frontend/index.html`
2. Find line **272**
3. Change:
   ```html
   <!-- FROM -->
   <input type="text" id="apiUrl" value="http://localhost:8080" ...>
   
   <!-- TO (use your actual backend URL) -->
   <input type="text" id="apiUrl" value="https://ml-classification-backend.onrender.com" ...>
   ```
4. Save and commit:
   ```bash
   git add frontend/index.html
   git commit -m "Update API URL for Render"
   git push origin main
   ```

### Step 3: Deploy Frontend (What You're Doing Now)

1. **Name**: `ml-classification-frontend`
2. **Branch**: `main`
3. **Root Directory**: `frontend` ⚠️
4. **Build Command**: *(EMPTY)* ⚠️
5. **Publish Directory**: `.` ⚠️
6. Click **"Create Static Site"**

---

## ✅ After Both Are Deployed

1. **Backend URL**: `https://____________________.onrender.com`
2. **Frontend URL**: `https://____________________.onrender.com`
3. **Test**: Open frontend URL → Enter values → Get predictions!

---

## 🆘 Quick Fixes

**Build Command Error?**
→ Delete everything in Build Command field, leave it EMPTY

**Publish Directory Error?**
→ Change to `.` (just a dot)

**Frontend can't connect?**
→ Update `frontend/index.html` line 272 with backend URL
→ Commit and push (auto-redeploys)

---

**📖 For detailed guide, see [RENDER_DEPLOYMENT_GUIDE.md](RENDER_DEPLOYMENT_GUIDE.md)**

