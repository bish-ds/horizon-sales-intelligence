<div align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/3308/3308395.png" width="100" />

  # 📈 Horizon: USA Regional Sales Intelligence

  <p align="center">
    <strong>Empowering data-driven decisions through advanced analytics and dynamic visualization.</strong>
  </p>
  
  [![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
  [![Streamlit](https://img.shields.io/badge/Streamlit-1.42+-red.svg)](https://streamlit.io/)
  [![Pandas](https://img.shields.io/badge/Pandas-2.2+-150458.svg)](https://pandas.pydata.org/)
  [![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow.svg)](https://powerbi.microsoft.com/)
</div>

---

## 🌟 Overview
**Horizon** is an end-to-end data analytics and business intelligence project focused on Acme Co.’s 2014–2018 USA sales data. The goal is to derive actionable insights that optimize pricing strategies, improve sales performance, and minimize concentration risk across products, channels, and regions.

This repository features an extensive Exploratory Data Analysis (EDA) process, an interactive **Streamlit Web Application**, and a robust **Power BI Dashboard** that together provide a comprehensive view of revenue and profit drivers.

## ✨ Key Features
- **Exploratory Data Analysis (EDA):** A detailed Jupyter Notebook (`EDA_Regional_Sales_Analysis.ipynb`) handling data profiling, cleaning, outlier detection, and correlation analysis.
- **Interactive Web App:** A deployable Streamlit dashboard (`app.py`) allowing dynamic filtering by region and sales channel, providing real-time top-level metrics and interactive Plotly visualizations.
- **Power BI Dashboard:** A sophisticated `.pbix` report providing deep-dive BI capabilities for enterprise reporting.
- **Executive Presentation:** A crafted PowerPoint presentation summarizing strategic findings and methodologies.

## 📂 Repository Structure
- 📁 **`Background/`** - Project contextual information.
- 📓 **`EDA_Regional_Sales_Analysis.ipynb`** - Comprehensive Jupyter Notebook with data wrangling and initial insights.
- 📊 **`SALES REPORT.pbix`** - Power BI dashboard file.
- 📈 **`PPT --- Regional Sales Analysis.pptx`** - Executive presentation of findings.
- 🌐 **`app.py`** - Streamlit web application source code.
- 📦 **`requirements.txt`** - Python dependencies for the Streamlit app.
- 📄 **`Regional Sales Dataset.xlsx`** - Raw sales data.
- 📄 **`Sales_data(EDA Exported).csv`** - Cleaned dataset exported from EDA, powering the web app.

## 🚀 Quick Start: Running the Web App Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/bish-ds/horizon-sales-intelligence.git
   cd horizon-sales-intelligence
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit Dashboard:**
   ```bash
   streamlit run app.py
   ```

## 🌐 Live Deployment
This project is structured for immediate deployment on **Streamlit Community Cloud**.
1. Log in to [Streamlit Community Cloud](https://streamlit.io/cloud).
2. Connect your GitHub account and select this repository.
3. Set the Main file path to `app.py` and click **Deploy**.

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! 
Feel free to check out the [issues page](../../issues).

1. Star the repository if you find it useful.
2. Fork the project.
3. Create your feature branch (`git checkout -b feature/AmazingFeature`).
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
5. Push to the branch (`git push origin feature/AmazingFeature`).
6. Open a Pull Request.

## 📬 Contact
For inquiries or collaboration opportunities, please reach out via GitHub.

---
<div align="center">
  <i>Developed with ❤️ for Data Analytics.</i>
</div>
