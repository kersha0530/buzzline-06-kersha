# buzzline-06-kersha
Simulated Online Sales &amp; E-commerce Streaming Data Project

# 📊 Real-time Sales Analytics with Python & SQLite

## 📂 Repository Overview
This repository contains a real-time **sales transaction streaming project**, where a **Python producer** generates fake sales transactions and stores them in an **SQLite database**. A **consumer script** reads from the database and generates visual insights, including a **heatmap, bar chart, and pie chart**.

### 🔧 **Key Features:**
- **Simulated E-commerce Sales Data**: Generates realistic transactions with timestamps, product categories, regions, and purchase amounts.
- **SQLite Database Integration**: Stores transactions in a structured relational database.
- **Real-time Data Processing**: The consumer script fetches, aggregates, and visualizes sales trends.
- **Multiple Visualizations**:
  - **Heatmap:** Sales by product category
  - **Bar Chart:** Sales count by category
  - **Pie Chart:** Sales distribution

---
## 🚀 **Project Setup**
### **1️. Create and Activate Virtual Environment**
Before running the scripts, set up a virtual environment:
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Activate virtual environment (Mac/Linux)
source venv/bin/activate
```

### **2️. Install Required Dependencies**
Ensure all necessary libraries are installed:
```powershell
pip install pandas matplotlib seaborn
```
---
## 💻 **Project Structure**
```
buzzline-06-kersha/
│── python_producers/
│   ├── sales_producer.py  # Generates and stores sales transactions in SQLite
│
│── python_consumers/
│   ├── sales_consumer.py  # Reads transactions and visualizes trends
│
│── data/
│   ├── sales_data.sqlite  # SQLite database storing transaction records
│
│── utils/
│   ├── db_utils.py        # Utility functions for database operations
│
│
│── README.md              # This file
```
---
##  **How to Run the Scripts**
### **1️. Start the Sales Producer**
Run the producer to continuously generate sales transactions and insert them into SQLite:
```powershell
python python_producers/sales_producer.py
```
This script:
- Generates a **new sales transaction every 2 seconds**.
- Stores transactions in the **sales_data.sqlite** database.

### **2️. Start the Sales Consumer**
Run the consumer to fetch transactions and generate visualizations:
```powershell
python python_consumers/sales_consumer.py
```
This script:
- Reads sales transactions from **SQLite**.
- **Processes data** into structured insights.
- **Displays 3 visualizations:**
  1. **Heatmap** - Sales by product category
  2. **Bar Chart** - Sales count per category
  3. **Pie Chart** - Sales distribution per category

---
## 📊 **Sample Visualizations**
Once the consumer script runs successfully, it will display **three charts**:
1. **Heatmap:** Sales intensity by category (colored grid)
2. **Bar Chart:** Number of transactions per category
3. **Pie Chart:** Proportion of sales across categories

```

📈 **Author:** Kersha Broussard  
📅 **Date:** February 17, 2025  
📊 **License:** MIT License



