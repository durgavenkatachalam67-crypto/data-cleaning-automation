# 🧹 Data Cleaning & Reporting Automation

An end-to-end automated data cleaning and reporting workflow built 
with Python that preprocesses raw retail data and generates 
professional Excel and PDF reports with visual summaries.

## 🎯 Objective
Automate data cleaning and reporting workflows by handling missing 
values, duplicates, and inconsistent data — then generate automated 
reports and visual summaries for business insights.

## 🗂️ Dataset
- **Source:** Sample - Superstore.csv
- **Records:** 9,994 rows × 21 columns
- **Domain:** Retail Sales Data (Orders, Customers, Products)

## 🔧 Tech Stack
- Python 3.x
- Pandas, NumPy
- OpenPyXL, XlsxWriter (Excel generation)
- FPDF2 (PDF generation)
- Matplotlib, Seaborn (Visualizations)
- Jupyter Notebook

## 📁 Project Structure
data-cleaning-automation/
├── data/
│   └── raw/                    # Original raw dataset
├── notebooks/
│   └── 01_cleaning.ipynb       # Main automation notebook
├── outputs/
│   ├── cleaned_data.xlsx       # Multi-sheet Excel report
│   ├── report.pdf              # Automated PDF report
│   ├── chart_category.png      # Sales by Category chart
│   └── chart_region.png        # Sales by Region chart
├── src/
│   ├── cleaner.py              # Data cleaning functions
│   ├── excel_exporter.py       # Excel report generation
│   └── reporter.py             # PDF report generation
└── README.md

## ⚙️ How to Run
1. Clone the repository
   git clone https://github.com/your-username/Data-Cleaning-Reporting-Automation.git

2. Create virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install pandas numpy openpyxl xlsxwriter fpdf2 matplotlib seaborn

4. Run the notebook
   notebooks/01_cleaning.ipynb

## 🧹 Data Cleaning Steps
| Step | Action |
|------|--------|
| 1 | Load raw CSV with encoding handling |
| 2 | Remove duplicate records |
| 3 | Handle missing values (fill & drop) |
| 4 | Fix data types (dates, integers) |
| 5 | Standardize inconsistent text (strip, title case) |
| 6 | Remove invalid records (negative sales) |

## 📊 Generated Reports
### Excel Report (4 Sheets)
| Sheet | Content |
|-------|---------|
| Cleaned Data | Full cleaned dataset with formatting |
| Summary Stats | Statistical summary of all columns |
| Sales by Category | Aggregated category-wise sales |
| Sales by Region | Aggregated region-wise sales |

### PDF Report
- Data cleaning summary (rows removed, duplicates, missing values)
- Sales statistics (total, average, max, min)
- Bar chart — Sales by Category
- Pie chart — Sales by Region

## ✅ Key Results
- Automated full cleaning pipeline in one notebook run
- Generated professional Excel report with 4 analytical sheets
- Generated PDF report with charts and cleaning summary
- Reduced manual reporting time to zero

## 🙋 Author
Durga V
B.Tech Information Technology
Sri Krishna College of Engineering and Technology
