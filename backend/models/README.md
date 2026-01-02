# Models Directory

This directory should contain the trained model files:

- `logistic_model.pkl` - Trained Logistic Regression model
- `decision_tree.pkl` - Trained Decision Tree model  
- `scaler.pkl` - Feature scaler for preprocessing

## How to Generate Models

1. Run the `ml/notebook.ipynb` in Google Colab or Jupyter
2. The notebook will automatically copy the models to this directory
3. Or manually copy the `.pkl` files from `ml/` to `backend/models/`

## Note

The backend will not start properly without these model files. Make sure to train the models first using the notebook!

