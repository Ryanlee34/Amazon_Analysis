#  Amazon Product & Review Analysis

###  Overview
This project analyzes Amazon products and reviews using **Python, PostgreSQL, and Power BI**. The goal is to clean raw data, store it in a structured database, and create **interactive visualizations** to answer key business questions.


##  Tech Stack
- **Python** (`pandas`, `sqlalchemy`, `psycopg2`)
- **PostgreSQL** (Database storage & querying)
- **Power BI** (Data visualization)
- **Jupyter Notebook** (EDA & data exploration)


##  Project Workflow
### **1️ Data Cleaning (Python)**
- Loaded raw Amazon dataset.
- Cleaned missing values, duplicates, and formatted columns.
- Saved as `final_cleaned_data.csv`.

### **2️ Database Storage (PostgreSQL)**
- Created **`amazon_analysis`** database.
- Stored cleaned data in a structured **SQL table** (`products`).

### **3️ Exploratory Data Analysis (EDA)**
- Used **Python (Pandas, Matplotlib, Seaborn)** to explore:
  - **Top-rated & lowest-rated products**
  - **Review count distribution**
  - **Discount impact on reviews**

### **4️ Data Visualization (Power BI)**
- Connected Power BI to **PostgreSQL** for interactive analysis.
- **Key Insights Visualized:**
  -  **Top-rated & worst-rated product categories**
  -  **Products with the most reviews**
  -  **Impact of discounts on ratings**
  -  **Most popular product categories**

---

##  How to Run the Project
### ** 1. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **2. Run Data Cleaning
```sh
python scripts/main.py
```

### **3. Load Data into PostegreSQL
- **Ensure PostgreSQL is running**
- **Run main.py to insert cleaned data into the database**

### **4. Open Power BI & Connect to PostegreSQL
- **Open Power BI Desktop**
- **Click Data -> BI Desktop**
- **Enter your database credentials (host, port, database name, username, password)**
- **Load data and start building visualizations**

### **Future Enhancements
- **Deploy database on AWS RDS for scalability**
- **Automate ETL pipeline using Apache Airflow**
- **Build alternative dashboards using Streamlit or Dash**
- **Train ML models to predict review sentiment**

### **Final Deliverables
- **Python scripts (data cleaning, ETL, SQL queries)**
- **PostgreSQL database (normalized schema)**
- **Power BI dashboard**
- **Project documentation**