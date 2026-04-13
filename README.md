# 📊 Retail Sales Forecasting & Inventory Optimization System

## 🚀 Overview

This project simulates a real-world retail analytics system that forecasts product demand and optimizes inventory decisions using machine learning.

It combines **data science + business logic** to solve critical retail problems like stockouts and overstocking.

---

## 🎯 Problem Statement

Retail businesses struggle with:

* ❌ Stockouts → lost sales
* ❌ Overstock → high holding cost

This project builds a system to:

* Predict future demand
* Recommend optimal inventory levels

---

## 🧠 Solution Approach

### 🔹 Forecasting

* Lag-based feature engineering
* Random Forest Regressor
* Time-series modeling approach

### 🔹 Inventory Optimization

* Safety Stock calculation
* Reorder Point (ROP)
* Demand variability handling

---

## 🛠️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib
* Streamlit

---

## 📂 Project Structure

```
Retail-Sales-Forecasting/
│
├── data/                     # Dataset
├── src/                      # Core modules
├── outputs/                  # Generated results
├── images/                   # Screenshots
├── app/                      # Streamlit dashboard
│
├── main.py                   # Main pipeline
├── requirements.txt          # Dependencies
└── README.md
```

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py
streamlit run app/app_streamlit.py
```

---

## 📊 Results

* 📉 Model MAE: **~1.47**
* 📦 Inventory Recommendations Generated
* 📈 Accurate Forecast Trends

---

## 📸 Screenshots

### 📈 Forecast vs Actual

![Forecast](images/forecast_plot.png)

### 📊 Dashboard

![Dashboard](images/dashboard.png)

### 💻 Terminal Output

![Terminal](images/terminal_output.png)

### 📄 CSV Output

![CSV](images/csv_output.png)

---

## 💼 Business Impact

* Improves demand planning accuracy
* Reduces stockouts and lost revenue
* Optimizes inventory holding cost

---

## 🔥 Key Highlights

✔ End-to-end ML pipeline
✔ Business-focused solution
✔ Real-world simulation
✔ Interactive dashboard

---

## 🚀 Future Improvements

* Multi-store forecasting
* XGBoost / Prophet models
* Real-time dashboard
* API deployment

---

## 👨‍💻 Author

Vayunandan Mishra
Aspiring Data Scientist / Analyst
