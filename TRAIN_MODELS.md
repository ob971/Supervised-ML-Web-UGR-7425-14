# 🎯 How to Train Models - Quick Guide

## Current Status
✅ Backend is running on port 8080  
❌ Models are not trained yet (this is why you see the error)

## Solution: Train the Models

You have **2 options** to train the models:

---

### Option 1: Google Colab (Recommended - Easiest) ⭐

1. **Go to Google Colab**: https://colab.research.google.com/

2. **Upload the notebook**:
   - Click "File" → "Upload notebook"
   - Upload `ml/notebook.ipynb`

3. **Upload the dataset** (IMPORTANT - No Google Drive needed!):
   - In Colab, click the **📁 folder icon** in the left sidebar (Files tab)
   - Click the **📤 Upload** button
   - Upload `ml/dataset.csv`
   - Wait for upload to complete
   - **Skip any cells that try to mount Google Drive** - you don't need them!

4. **Run all cells**:
   - Click "Runtime" → "Run all"
   - Wait for all cells to complete (2-3 minutes)

5. **Download the models**:
   - After completion, you'll see 3 files created:
     - `logistic_model.pkl`
     - `decision_tree.pkl`
     - `scaler.pkl`
   - Download these files

6. **Copy models to backend**:
   - Copy all 3 `.pkl` files to `backend/models/` directory
   - Your folder structure should be:
     ```
     backend/
       models/
         logistic_model.pkl
         decision_tree.pkl
         scaler.pkl
     ```

7. **Restart the backend**:
   - Stop the current backend (Ctrl+C in terminal)
   - Run: `cd backend && python main.py`
   - The models will now load automatically!

---

### Option 2: Local Jupyter Notebook

1. **Install dependencies**:
   ```bash
   cd ml
   pip install -r requirements.txt
   ```

2. **Start Jupyter**:
   ```bash
   jupyter notebook notebook.ipynb
   ```

3. **Run all cells**:
   - In Jupyter, click "Cell" → "Run All"
   - Wait for completion

4. **Copy models**:
   - The notebook automatically copies models to `backend/models/`
   - If not, manually copy the 3 `.pkl` files from `ml/` to `backend/models/`

5. **Restart backend**:
   - Stop and restart: `cd backend && python main.py`

---

## Verify Models Are Loaded

After training and copying models, check:

1. **Backend health**: http://localhost:8080/health
   - Should show: `"models_loaded": true`

2. **Frontend**: Refresh the page
   - Error should disappear
   - You can now make predictions!

---

## Quick Test

Once models are loaded, test with these sample values:
- Age: 29
- Glucose: 85
- BP: 66
- Skin Thickness: 29
- Insulin: 0
- BMI: 26.6
- Diabetes Pedigree: 0.351
- Pregnancies: 0

---

## Troubleshooting

**Models still not loading?**
- ✅ Check files exist: `backend/models/logistic_model.pkl`
- ✅ Check file names are exact (case-sensitive)
- ✅ Restart backend after copying models
- ✅ Check backend logs for errors

**Need help?**
- Check the full notebook: `ml/notebook.ipynb`
- Review README.md for detailed instructions

---

**Time to train: ~3-5 minutes** ⏱️

