# 🤖 ML Classification Application

**End-to-End Machine Learning Classification System Using Logistic Regression and Decision Tree**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)

## 🎯 Overview

This project demonstrates a complete end-to-end machine learning classification system that:

1. **Trains** two classification models (Logistic Regression & Decision Tree) on a binary classification dataset
2. **Evaluates** model performance using accuracy, precision, recall, and F1-score
3. **Serves** predictions via a RESTful API (FastAPI)
4. **Provides** an interactive web interface for real-time predictions
5. **Deploys** the application to cloud platforms

### One-Line Summary

> "This project demonstrates an end-to-end machine learning system using Logistic Regression and Decision Tree models, integrated into a deployed web application."

## ✨ Features

- ✅ **Complete ML Pipeline**: Data loading, cleaning, preprocessing, training, and evaluation
- ✅ **Dual Model System**: Logistic Regression and Decision Tree classifiers
- ✅ **Comprehensive Evaluation**: Accuracy, Precision, Recall, F1-Score metrics
- ✅ **RESTful API**: FastAPI backend with input validation and error handling
- ✅ **Interactive Frontend**: Modern, responsive web interface
- ✅ **Model Comparison**: Side-by-side comparison of both models
- ✅ **Confidence Scores**: Probability/confidence output for predictions
- ✅ **Cloud Ready**: Deployment configurations for Render/Railway and Vercel

## 📁 Project Structure

```
ml-classification-app/
│
├── ml/                          # Machine Learning Pipeline
│   ├── notebook.ipynb          # Google Colab notebook with complete ML pipeline
│   ├── dataset.csv             # Training dataset
│   ├── logistic_model.pkl      # Trained Logistic Regression model
│   ├── decision_tree.pkl       # Trained Decision Tree model
│   ├── scaler.pkl              # Feature scaler (for Logistic Regression)
│   └── requirements.txt        # Python dependencies for ML environment
│
├── backend/                     # FastAPI Backend
│   ├── main.py                 # FastAPI application with prediction endpoints
│   ├── models/                 # Model files (copied from ml/)
│   │   ├── logistic_model.pkl
│   │   ├── decision_tree.pkl
│   │   └── scaler.pkl
│   └── requirements.txt        # Python dependencies for backend
│
├── frontend/                    # Frontend Application
│   └── index.html              # Interactive web interface
│
├── README.md                    # This file
└── .gitignore                  # Git ignore rules
```

## 🔧 Prerequisites

- **Python 3.8+** (for ML pipeline and backend)
- **Google Colab** or **Jupyter Notebook** (for running the ML notebook)
- **Web Browser** (for frontend)
- **Git** (for version control)

## 🚀 Setup Instructions

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
cd ml-classification-app
```

### Step 2: Train the Models

#### Option A: Using Google Colab (Recommended)

1. Upload `ml/notebook.ipynb` to Google Colab
2. Upload `ml/dataset.csv` to the same Colab session
3. Run all cells in the notebook
4. The notebook will:
   - Load and clean the data
   - Train both models
   - Evaluate performance
   - Export models as `.pkl` files
   - Copy models to `backend/models/` directory

#### Option B: Using Local Jupyter

```bash
# Install ML dependencies
cd ml
pip install -r requirements.txt

# Run the notebook
jupyter notebook notebook.ipynb
```

After training, ensure the following files exist:
- `ml/logistic_model.pkl`
- `ml/decision_tree.pkl`
- `ml/scaler.pkl`
- `backend/models/logistic_model.pkl`
- `backend/models/decision_tree.pkl`
- `backend/models/scaler.pkl`

### Step 3: Setup Backend

```bash
# Navigate to backend directory
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 4: Run the Backend

```bash
# From the backend directory
python main.py

# Or using uvicorn directly
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at: `http://localhost:8000`

- API Documentation: `http://localhost:8000/docs`
- Health Check: `http://localhost:8000/health`

### Step 5: Open Frontend

1. Open `frontend/index.html` in your web browser
2. Or use a local server:

```bash
# Using Python
cd frontend
python -m http.server 8080

# Then open: http://localhost:8080
```

3. Update the API URL in the frontend if needed (default: `http://localhost:8000`)

## 💻 Usage

### Using the Web Interface

1. Open the frontend (`frontend/index.html`)
2. Enter feature values:
   - Age
   - Glucose Level
   - Blood Pressure
   - Skin Thickness
   - Insulin Level
   - BMI
   - Diabetes Pedigree Function
   - Number of Pregnancies
3. Click "Get Predictions"
4. View predictions from both models with confidence scores

### Using the API Directly

#### Single Prediction

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 29,
    "glucose": 85,
    "bp": 66,
    "skin_thickness": 29,
    "insulin": 0,
    "bmi": 26.6,
    "diabetes_pedigree": 0.351,
    "pregnancies": 0
  }'
```

#### Response Example

```json
{
  "logistic_regression": {
    "prediction": 0,
    "probability": 0.8234,
    "model_name": "Logistic Regression"
  },
  "decision_tree": {
    "prediction": 0,
    "probability": 0.8567,
    "model_name": "Decision Tree"
  },
  "input_features": {
    "age": 29,
    "glucose": 85,
    "bp": 66,
    "skin_thickness": 29,
    "insulin": 0,
    "bmi": 26.6,
    "diabetes_pedigree": 0.351,
    "pregnancies": 0
  }
}
```

## 📚 API Documentation

### Endpoints

#### `GET /`
- **Description**: Root endpoint with API information
- **Response**: API metadata and available endpoints

#### `GET /health`
- **Description**: Health check endpoint
- **Response**: Status of API and loaded models

#### `POST /predict`
- **Description**: Get predictions from both models
- **Request Body**: JSON with feature values
- **Response**: Predictions from both models with probabilities

#### `POST /predict/batch`
- **Description**: Batch prediction for multiple inputs
- **Request Body**: Array of feature objects
- **Response**: Array of prediction results

### Interactive API Docs

Visit `http://localhost:8000/docs` for interactive Swagger documentation.

## ☁️ Deployment

**📖 For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)**

### Quick Deployment Summary

#### Backend (Render/Railway/Heroku)

1. **Ensure models are trained** and `.pkl` files are in `backend/models/`
2. **Push code to GitHub**
3. **Deploy to platform**:
   - **Render**: Create Web Service, set build/start commands
   - **Railway**: Auto-detects Python, set root directory to `backend`
   - **Heroku**: Uses `Procfile` (already included)
4. **Get backend URL** (e.g., `https://your-app.onrender.com`)

#### Frontend (Vercel/Netlify)

1. **Update API URL** in `frontend/index.html` (or keep configurable)
2. **Push code to GitHub**
3. **Deploy to platform**:
   - **Vercel**: Import repo, set root directory to `frontend`
   - **Netlify**: Import repo, set base directory to `frontend`
4. **Get frontend URL** (e.g., `https://your-app.vercel.app`)

### Deployment Files Included

- ✅ `backend/Procfile` - For Heroku deployment
- ✅ `backend/runtime.txt` - Python version specification
- ✅ `render.yaml` - Render configuration (optional)

**For step-by-step instructions with screenshots and troubleshooting, see [DEPLOYMENT.md](DEPLOYMENT.md)**

## 📊 Model Performance

After training, the notebook will display:

- **Accuracy**: Overall correctness
- **Precision**: True positives / (True positives + False positives)
- **Recall**: True positives / (True positives + False negatives)
- **F1-Score**: Harmonic mean of precision and recall
- **Confusion Matrix**: Detailed classification results
- **Model Comparison**: Side-by-side performance metrics

## 🛠️ Technologies Used

### Machine Learning
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **scikit-learn**: Machine learning algorithms
- **joblib**: Model serialization
- **matplotlib/seaborn**: Data visualization

### Backend
- **FastAPI**: Modern, fast web framework
- **uvicorn**: ASGI server
- **pydantic**: Data validation
- **python-multipart**: Form data handling

### Frontend
- **HTML5**: Structure
- **CSS3**: Styling (with gradients and animations)
- **JavaScript (ES6+)**: Interactivity and API communication

## 📝 Notes

- The dataset used is a binary classification dataset suitable for medical predictions
- Models are trained with a 80/20 train-test split
- Feature scaling is applied for Logistic Regression (StandardScaler)
- Decision Tree doesn't require scaling
- Both models are exported using `joblib` for efficient loading

## 🔒 Security Considerations

For production deployment:

1. **CORS**: Update `allow_origins` in `backend/main.py` to specific frontend URL
2. **Input Validation**: Already implemented using Pydantic
3. **Rate Limiting**: Consider adding rate limiting for production
4. **Authentication**: Add API keys or authentication if needed
5. **HTTPS**: Always use HTTPS in production

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

Your Name - [Your GitHub](https://github.com/yourusername)

## 🙏 Acknowledgments

- scikit-learn team for excellent ML library
- FastAPI team for the amazing framework
- All contributors and open-source community

---

**⭐ If you find this project helpful, please give it a star!**

"# Supervised-ML-Web-UGR-7425-14" 
