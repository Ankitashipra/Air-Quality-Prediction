# Air Quality Prediction  

## Overview  
This project predicts air quality based on sensor data using a **Random Forest model**. It provides an API and a web interface for predictions.  

##  Dataset  
- Source: [Air Quality UCI](https://archive.ics.uci.edu/ml/datasets/Air+Quality)  
- Features: CO, NO2, Temperature, Humidity, etc.  

## Technologies Used  
- Python (Flask, Pandas, Sklearn)  
- Machine Learning (Random Forest)  
- HTML, CSS, JavaScript  
- Git & GitHub
  ## 📊 Results  
## Model Performance  
| Metric               | Value  |  
|----------------------|--------|  
| Training R²          | 0.98   |  
| Testing R²           | 0.91   |  
| Cross-Validation R²  | 0.86   |  

### Key Visualizations  
#### 1. Actual vs Predicted NO2  
![Actual vs Predicted](figure/Figure1:ActualvsPredictedNO2Levels(R²=0.91).png)  
*High accuracy (R²=0.91) in NO2 prediction.*  

#### 2. Feature Importance  
![Feature Importance](figure/Figure4:RandomForestFeatureImportance.png)  
*NOx and CO levels were top predictors.* 

## 🌐 Web Interface  
### Input Form  
![Input Form](figure/Figure8:WebAppInputForm.png)  

### Prediction Output  
![Prediction Result](figure/Figure9:SamplePredictionOutput.png)  
*Sample output with health recommendations.* 
## 📄 API Documentation

**Endpoint**: `POST /predict`

**Input (JSON)**:
```json
{
  "CO(GT)": 2.3,
  "NOx(GT)": 200,
  "Temperature": 25.5
}
```

##  How to Run  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Ankitashipra/Air-Quality-Prediction.git
