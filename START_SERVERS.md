# 🚀 How to Start the Application

## ⚠️ Important: Don't Open HTML File Directly!

**Problem**: If you open `frontend/index.html` directly in your browser (double-clicking it), you'll get a **"Failed to fetch"** error because browsers block `file://` protocol from accessing `localhost` APIs.

**Solution**: Always use a web server to serve the frontend!

---

## ✅ Correct Way to Run the Application

### Step 1: Start Backend (Terminal 1)

```bash
cd backend
python main.py
```

**Or using uvicorn directly:**
```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8080
```

✅ Backend will be at: **http://localhost:8080**

---

### Step 2: Start Frontend Server (Terminal 2)

**Option A: Python HTTP Server (Recommended)**
```bash
cd frontend
python -m http.server 3000
```

**Option B: Using Node.js (if you have it)**
```bash
cd frontend
npx http-server -p 3000
```

✅ Frontend will be at: **http://localhost:3000**

---

### Step 3: Open in Browser

**Open this URL in your browser:**
```
http://localhost:3000
```

**NOT** `file:///C:/Users/.../frontend/index.html` ❌

---

## 🎯 Quick Start Commands

### Windows PowerShell:
```powershell
# Terminal 1 - Backend
cd backend; python main.py

# Terminal 2 - Frontend  
cd frontend; python -m http.server 3000
```

### Linux/Mac:
```bash
# Terminal 1 - Backend
cd backend && python main.py

# Terminal 2 - Frontend
cd frontend && python -m http.server 3000
```

---

## ✅ Verify Everything is Running

1. **Backend Health**: http://localhost:8080/health
   - Should return JSON with status

2. **Backend API Docs**: http://localhost:8080/docs
   - Should show Swagger UI

3. **Frontend**: http://localhost:3000
   - Should show the ML Classification App interface

---

## 🔧 Troubleshooting

### "Failed to fetch" Error

**Cause**: Opening HTML file directly instead of using a web server

**Fix**: 
1. Stop opening the file directly
2. Use `python -m http.server` as shown above
3. Open `http://localhost:3000` in browser

### Port Already in Use

**Error**: `Address already in use`

**Fix**: Use a different port:
```bash
# Frontend on different port
python -m http.server 3001

# Or backend on different port
uvicorn main:app --port 8081
```

Then update the API URL in the frontend.

### Backend Not Responding

**Check**:
1. Is backend running? Visit http://localhost:8080/health
2. Check terminal for errors
3. Verify port 8080 is not blocked by firewall

---

## 📝 Summary

✅ **Backend**: `cd backend && python main.py` → http://localhost:8080  
✅ **Frontend**: `cd frontend && python -m http.server 3000` → http://localhost:3000  
✅ **Browser**: Open http://localhost:3000 (NOT the HTML file directly!)

---

**Remember**: Always use a web server for the frontend! 🎯

