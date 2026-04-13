# ================================
# IMPORT LIBRARIES
# ================================
import os
import pandas as pd
from sklearn.metrics import mean_absolute_error

from src.data_preprocessing import load_data
from src.feature_engineering import create_features
from src.model import train_model
from src.inventory import calculate_inventory
from src.visualization import plot_sales


# ================================
# STEP 1: LOAD DATA
# ================================
print("\n📥 Loading data...")
df = load_data("data/retail_timeseries.csv")

print("Data Loaded Successfully!")
print(df.head())


# ================================
# STEP 2: FEATURE ENGINEERING
# ================================
print("\n⚙️ Creating features...")
df = create_features(df)

print("Feature Engineering Completed!")
print(df.head())


# ================================
# STEP 3: PREPARE DATA
# ================================
features = ["lag_1", "lag_7", "rolling_mean_3", "day_of_week"]

X = df[features]
y = df["qty_sold"]

# Check missing values
print("\n🔍 Checking missing values:")
print(X.isnull().sum())


# ================================
# STEP 4: TRAIN MODEL
# ================================
print("\n🤖 Training model...")
model = train_model(X, y)

print("Model Training Completed!")


# ================================
# STEP 5: PREDICTIONS
# ================================
print("\n📈 Generating predictions...")
predictions = model.predict(X)


# ================================
# STEP 6: MODEL EVALUATION
# ================================
mae = mean_absolute_error(y, predictions)
print(f"\n📊 Model Performance:")
print(f"MAE: {mae:.2f}")


# ================================
# STEP 7: INVENTORY OPTIMIZATION
# ================================
print("\n📦 Calculating inventory recommendations...")

inventory_result = calculate_inventory(predictions)

print("\n✅ Inventory Recommendation:")
print(inventory_result)


# ================================
# STEP 8: CREATE OUTPUT FOLDER
# ================================
os.makedirs("outputs", exist_ok=True)


# ================================
# STEP 9: SAVE RESULTS
# ================================

# Save forecast results
output_df = df.copy()
output_df["predictions"] = predictions

output_df.to_csv("outputs/forecast_results.csv", index=False)

# Save inventory results
inv_df = pd.DataFrame([inventory_result])
inv_df.to_csv("outputs/inventory_results.csv", index=False)

print("\n💾 Results saved successfully in 'outputs/' folder!")


# ================================
# STEP 10: VISUALIZATION
# ================================
print("\n📊 Generating visualization...")

plot_sales(df, predictions)

print("\n🎉 PROJECT EXECUTED SUCCESSFULLY!")