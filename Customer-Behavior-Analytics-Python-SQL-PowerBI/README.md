# Customer Behaviour Analysis Dashboard

## 📌 Project Overview
This project focuses on analyzing customer shopping behavior using Python, SQL, and Power BI.  
The objective is to clean and transform raw transactional data, perform exploratory and business-driven analysis, and present insights through an interactive dashboard.

---

## 🛠 Tech Stack
- **Python**: Pandas, NumPy
- **Database**: PostgreSQL
- **Visualization**: Power BI
- **Connectivity**: SQLAlchemy, psycopg2

---

## 📂 Dataset Description
The dataset contains customer-level shopping information including:
- Demographics (Age, Gender)
- Purchase behavior (Amount, Frequency, Previous Purchases)
- Product details (Category, Item Purchased)
- Subscription & discount indicators
- Review ratings and shipping types

---

## 🔄 Data Processing (Python)
Key steps performed using Pandas:
- Column standardization (lowercase, snake_case)
- Missing value imputation using **median per category**
- Feature engineering:
  - Age groups using quantile-based binning
  - Purchase frequency converted into days
- Data validation and cleanup
- Export of cleaned data to PostgreSQL

---

## 🗄 Database Integration
- Created PostgreSQL database and table
- Loaded processed data using `to_sql`
- Enabled SQL-based analytical queries for business insights

---

## 📊 SQL Analysis Performed
Key business questions answered:
1. Total revenue by gender
2. High-spending customers who used discounts
3. Top 5 products by average review rating
4. Purchase behavior by shipping type
5. Spending comparison between subscribers and non-subscribers
6. Subscription trends among repeat buyers
7. Revenue contribution by age group
8. Top products within each category

---

## 📈 Power BI Dashboard
The dashboard includes:
- KPI cards (Total Customers, Avg Purchase, Avg Rating)
- Sales & revenue by category
- Subscription impact analysis
- Age-group-wise revenue
- Interactive slicers for gender, category, shipping type, and subscription status

---

## 🎯 Key Insights
- Subscribed customers contribute higher average spend
- Clothing category generates the highest revenue
- Young and middle-aged customers drive maximum sales
- Express and Standard shipping show distinct spending patterns

---

## 📌 Conclusion
This project demonstrates an end-to-end analytics workflow, from raw data cleaning to business storytelling through dashboards.  
It reflects practical skills required for entry-level to junior data analyst roles.

---

## 📎 Future Enhancements
- Predictive modeling for customer churn
- RFM segmentation
- Automated data pipeline

---

## 👤 Author
**Deepak**  
Data Analyst  
