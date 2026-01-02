# 🚀 Quick Start Guide

## Prerequisites Check

- [ ] Python 3.8+ installed
- [ ] Google Colab account (or Jupyter Notebook)
- [ ] Web browser

## Step-by-Step Setup (5 minutes)

### 1️⃣ Train Models (2 minutes)

**Option A: Google Colab (Recommended)**
1. Go to [Google Colab](https://colab.research.google.com/)
2. Upload `ml/notebook.ipynb`
3. Upload `ml/dataset.csv` to Colab
4. Run all cells (Runtime → Run All)
5. Download the `.pkl` files generated
6. Copy them to `backend/models/` directory

**Option B: Local Jupyter**
```bash
cd ml
pip install -r requirements.txt
jupyter notebook notebook.ipynb
# Run all cells, then copy .pkl files to backend/models/
```

### 2️⃣ Start Backend (1 minute)

```bash
cd backend
pip install -r requirements.txt
python main.py
```

✅ Backend running at: `http://localhost:8000`

### 3️⃣ Open Frontend (30 seconds)

1. Open `frontend/index.html` in your browser
2. Or use: `python -m http.server 8080` (from frontend directory)

### 4️⃣ Test the Application

1. Enter sample values in the form
2. Click "Get Predictions"
3. See results from both models!

## 🎯 Expected Output

After training, you should see:
- ✅ Models exported to `ml/` directory
- ✅ Models copied to `backend/models/` directory
- ✅ Backend API running on port 8000
- ✅ Frontend accessible in browser

## 🐛 Troubleshooting

**Backend says "Models not loaded"**
→ Make sure you've trained the models and copied `.pkl` files to `backend/models/`

**Frontend can't connect to backend**
→ Check that backend is running on `http://localhost:8000`
→ Update API URL in frontend if using different port

**Import errors**
→ Make sure you've installed all requirements: `pip install -r requirements.txt`

## 📚 Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Deploy to cloud platforms (Render, Railway, Vercel)
- Customize the models or add more features

---

**Happy Coding! 🎉**

