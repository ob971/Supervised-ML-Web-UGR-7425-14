# 🔧 Troubleshooting "Failed to Fetch" Error

## ✅ Current Status
- Backend: Running on port 8080 ✅
- Models: Loaded ✅
- Frontend: Running on port 3000 ✅
- `/predict` endpoint: Working ✅

## 🔍 If You See "Failed to Fetch"

### Step 1: Verify Backend is Running
1. Open a new browser tab
2. Visit: http://localhost:8080/health
3. Should show: `{"status":"healthy","models_loaded":true}`

### Step 2: Check API URL in Frontend
1. In the frontend (http://localhost:3000)
2. Look at the "Backend API URL" field at the top
3. Make sure it says: `http://localhost:8080`
4. If different, change it to `http://localhost:8080`

### Step 3: Hard Refresh Browser
1. Press **Ctrl+F5** (or **Ctrl+Shift+R**)
2. This clears cache and reloads the page
3. Try making a prediction again

### Step 4: Check Browser Console
1. Press **F12** to open Developer Tools
2. Click the **Console** tab
3. Look for red error messages
4. Common errors:
   - **CORS error**: Backend CORS settings issue
   - **Network error**: Backend not reachable
   - **404 error**: Wrong URL

### Step 5: Verify Both Servers
**Backend:**
```powershell
# Check if running
netstat -ano | findstr :8080
```

**Frontend:**
```powershell
# Check if running
netstat -ano | findstr :3000
```

### Step 6: Restart Both Servers

**Terminal 1 - Backend:**
```powershell
cd backend
python main.py
```

**Terminal 2 - Frontend:**
```powershell
cd frontend
python -m http.server 3000
```

### Step 7: Test Direct API Call
Open browser console (F12) and run:
```javascript
fetch('http://localhost:8080/predict', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    age: 29,
    glucose: 85,
    bp: 66,
    skin_thickness: 29,
    insulin: 0,
    bmi: 26.6,
    diabetes_pedigree: 0.351,
    pregnancies: 0
  })
})
.then(r => r.json())
.then(console.log)
.catch(console.error)
```

If this works, the issue is with the frontend code.
If this fails, the issue is with the backend or network.

---

## 🎯 Quick Fixes

### Fix 1: Clear Browser Cache
- **Chrome/Edge**: Ctrl+Shift+Delete → Clear cached images and files
- **Firefox**: Ctrl+Shift+Delete → Cache → Clear Now

### Fix 2: Try Different Browser
- Sometimes browser extensions block requests
- Try in incognito/private mode

### Fix 3: Check Firewall
- Windows Firewall might block localhost connections
- Temporarily disable to test

### Fix 4: Verify Ports
- Backend must be on port 8080
- Frontend must be on port 3000
- No other apps using these ports

---

## ✅ Success Indicators

When everything works:
1. ✅ Backend health check returns JSON
2. ✅ Frontend loads without errors
3. ✅ No red errors in browser console
4. ✅ Predictions return results (not errors)
5. ✅ Both models show predictions

---

## 📞 Still Not Working?

1. **Check backend terminal** for error messages
2. **Check browser console** (F12) for JavaScript errors
3. **Verify file paths** - models in `backend/models/`
4. **Restart everything** - close all terminals and restart

---

**Most common fix: Hard refresh (Ctrl+F5) and verify API URL is `http://localhost:8080`**

