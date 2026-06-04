# Population Analysis and Forecast for Yazd Province (Iran)

This project analyzes village‑level population data from the **Statistical Centre of Iran (amar.org.ir)** for Yazd province.  
It builds a machine learning model to predict the population of villages based on administrative location and number of households, and presents insights through a Power BI dashboard.


---

## 📊 Data description

- **Source**: [Statistical Centre of Iran](https://www.amar.org.ir/) – Census of households and population (2016).
- **Scope**: Villages in Yazd province (including townships, districts, rural districts).
- **Key columns**:
  - `نام شهرستان` (County), `نام بخش` (District), `نام شهر/دهستان` (Rural District), `نام ابادی` (Village)
  - `خانوار` (Number of households)
  - `جمعيت` (Population)
  - `مرد`, `زن` (Male, Female population)
- **Note**: Villages with ≤3 households have population masked as `*` for confidentiality (excluded from training).

---

## 🔍 Methodology

### 1. Data preparation
- Loaded `cleaned.xlsx` (pre‑filtered to inhabited villages: population > 0).
- Dropped rows with missing key location fields.
- Removed villages with `*` (masked data) – they are not used for training/prediction.

### 2. Feature engineering
- Converted categorical location columns (`شهرستان`, `بخش`, `شهر/دهستان`) into numerical codes using `LabelEncoder`.
- Used **number of households** as a direct numeric feature.
- **Target variable**: `جمعيت` (population).

### 3. Model
- **Random Forest Regressor** (200 trees, max depth 15, min samples split 5) – chosen for its ability to capture non‑linear relationships without overfitting.
- Train / test split: 80% / 20% (random state 42).

### 4. Evaluation
- **Mean Absolute Error (MAE)**
- **Root Mean Squared Error (RMSE)**
- **R² (coefficient of determination)**

### 5. Predictions
- The trained model predicts population for **all villages** (including those in the training set) – stored in `population_predictions.xlsx`.

### 6. Visualisation (Power BI)
- Dashboard includes:
  - Geographic distribution of population (map)
  - Top villages by population / households
  - Actual vs. predicted population scatter plot
  - Slicers for county, district, and rural district

---

## 📈 Model performance (example)

After running `population_ml.py`, you will see output in new excel file.

## 🚀 How to run

1. **Install dependencies**  
   ```bash
   pip install -r requirements.txt

python population_ml.py
