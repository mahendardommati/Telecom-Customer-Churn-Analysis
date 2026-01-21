
# 📊 Telecom Customer Churn Analysis – Power BI Dashboard


# 📌 Project Overview

Customer churn is a major challenge in the telecom industry. This project focuses on analyzing customer churn data and predicting churn using Machine Learning, along with business insights through Power BI dashboards.

The project is implemented end-to-end, covering:

Data preprocessing

Feature engineering

Model training & evaluation

Web deployment using Flask

Business analysis using Power BI

# 🎯 Objective

Understand customer churn behavior

Identify high-risk customer segments

Build a churn prediction ML model

Deploy the model with a web dashboard

Provide actionable business recommendations

# 🗂 Dataset Information

  Dataset Name: Telco Customer Churn

  Source: IBM Sample Dataset

  Total Records: 7,043 customers

  Total Columns: 21

  Target Variable: Churn (Yes / No)

# 🛠 Tools & Technologies Used

🔹 Programming & ML

Python

Pandas, NumPy

Scikit-learn

Random Forest Classifier

🔹 Web & Deployment

Flask

HTML, CSS

🔹 Visualization & BI

Power BI

DAX

🔹 Development Environment

PyCharm

Git & GitHub

📁 Project Structure
Telco_Customer_Churn_Project/
│
├── main.py
├── app.py
├── model.pkl
├── save_model.py
│
├── src/
│   ├── missing_values.py
│   ├── encoding.py
│   ├── transformation.py
│   ├── outliers.py
│   ├── feature_selection.py
│   ├── model_training.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/style.css
│   └── images/
│       ├── jio.png
│       ├── airtel.png
│       ├── vi.png
│       └── bsnl.png
│
├── WA_Fn-UseC_-Telco-Customer-Churn.csv
└── README.md

🔄 Project Workflow
Data Loading
   ↓
Missing Value Handling
   ↓
Categorical Encoding
   ↓
Feature Engineering
   ↓
Train-Test Split
   ↓
Model Training (Random Forest)
   ↓
Model Evaluation
   ↓
Model Saving
   ↓
Flask Deployment

🧹 Data Preprocessing

Handled missing values using median (numerical) and mode (categorical)

Encoded categorical features using Label Encoding

Managed outliers using statistical techniques

Selected relevant features for modeling

🤖 Machine Learning Model

Algorithm Used: Random Forest Classifier

Reason: Handles non-linearity, robust to overfitting, performs well on mixed data

Evaluation Metric: Accuracy

✅ Model Accuracy
Accuracy: ~79.7%

🌐 Web Application (Flask)

Interactive dashboard for churn prediction

User inputs customer details

Predicts whether customer will churn or not

Clean UI with telecom provider selection (Jio, Airtel, VI, BSNL)

📊 Power BI Dashboard Highlights
🔹 KPIs

Total Customers: 7,043

Churned Customers: 1,869

Average Monthly Charges: 64.76

🔹 Key Insights

Month-to-month contracts have highest churn

Short-tenure customers churn more

Higher monthly charges increase churn probability

Fiber optic customers show higher churn

💡 Business Recommendations

Encourage long-term contracts with offers

Provide discounts to new customers

Improve fiber optic service quality

Promote auto-payment options

▶️ How to Run the Project
1️⃣ Clone the repository
git clone https://github.com/your-username/Telco_Customer_Churn_Project.git
cd Telco_Customer_Churn_Project

2️⃣ Create virtual environment & install dependencies
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

3️⃣ Train the model
python main.py

4️⃣ Run Flask app
python app.py


Open browser:

http://127.0.0.1:5000/

📌 Future Enhancements

Add XGBoost model

Improve feature selection

Add confidence score in predictions

Deploy on cloud (AWS / Render / Heroku)

# 📌 Conclusion

This Power BI dashboard transforms raw customer data into meaningful insights.
By identifying churn drivers, businesses can take preventive actions to reduce customer loss and improve profitability.

# 📷 Dashboard Preview
<img width="1153" height="749" alt="image" src="https://github.com/user-attachments/assets/53a49228-c388-482a-86ad-caa0bd60cbce" />



