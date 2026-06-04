import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import os

# LOAD DATA
input_file = r"C:\Users\fatemeh\OneDrive\Desktop\codes_tutorial_uni\HouseholdPopulationVillage_amar\cleaned.xlsx"
output_folder = r"C:\Users\fatemeh\OneDrive\Desktop\codes_tutorial_uni\HouseholdPopulationVillage_amar"
os.makedirs(output_folder, exist_ok=True)
output_file = os.path.join(output_folder, "population_predictions.xlsx")
df = pd.read_excel(input_file)

#keep only inhabited villages (population > 0)
df = df[df['جمعيت'] > 0].copy()
# Drop rows with missing key columns
df = df.dropna(subset=['نام شهرستان', 'نام بخش', 'نام شهر/دهستان', 'خانوار', 'جمعيت'])

le_county = LabelEncoder()
le_district = LabelEncoder()
le_rural = LabelEncoder()
df['county_code'] = le_county.fit_transform(df['نام شهرستان'])
df['district_code'] = le_district.fit_transform(df['نام بخش'])
df['rural_code'] = le_rural.fit_transform(df['نام شهر/دهستان'])

feature_cols = ['county_code', 'district_code', 'rural_code', 'خانوار']
X = df[feature_cols]
y = df['جمعيت']

# TRAIN / TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# TRAIN MODEL
model = RandomForestRegressor(
    n_estimators=200,
    max_depth=15,
    min_samples_split=5,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)

# EVALUATION
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\n" + "="*50)
print("MODEL PERFORMANCE")
print("="*50)
print(f"Mean Absolute Error (MAE) : {mae:.2f} persons")
print(f"Root Mean Square Error (RMSE): {rmse:.2f} persons")
print(f"R² (coefficient of determination): {r2:.4f}")
print("="*50)

# PREDICT FOR ALL VILLAGES
df['predicted_population'] = model.predict(X)

# SAVE RESULTS
output_columns = [
    'نام شهرستان', 'نام بخش', 'نام شهر/دهستان', 'نام ابادی',
    'خانوار', 'جمعيت', 'predicted_population'
]
df[output_columns].to_excel(output_file, index=False)

print(f"\n✅ Predictions saved to:\n{output_file}")