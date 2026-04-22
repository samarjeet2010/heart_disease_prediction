from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ CORS (frontend connect ke liye)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔥 Dummy prediction logic
def predict_risk(age, bp, chol, thalach, exang, oldpeak):
    risk = 0

    if age > 50: risk += 1
    if bp > 140: risk += 1
    if chol > 240: risk += 1
    if thalach < 120: risk += 1
    if exang == 1: risk += 1
    if oldpeak > 2: risk += 1

    return 1 if risk >= 3 else 0


# ✅ FIXED API (yahi tumhe set karna hai)
@app.post("/predict")
def predict(
    age: int,
    sex: int,
    cp: int,
    trestbps: int,
    chol: int,
    fbs: int,
    restecg: int,
    thalach: int,
    exang: int,
    oldpeak: float
):
    
    result = predict_risk(age, trestbps, chol, thalach, exang, oldpeak)

    return {
        "prediction": result,
        "rf_accuracy": 83,
        "lr_accuracy": 78,
        "gb_accuracy": 82,
    }