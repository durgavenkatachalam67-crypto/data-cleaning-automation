from fpdf import FPDF
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import os

def generate_charts(df):
    charts = []

    # Chart 1 - Sales by Category
    fig, ax = plt.subplots(figsize=(8, 4))
    cat = df.groupby('Category')['Sales'].sum()
    cat.plot(kind='bar', ax=ax, color=['#4472C4','#ED7D31','#A9D18E'])
    ax.set_title('Total Sales by Category')
    ax.set_ylabel('Sales ($)')
    plt.tight_layout()
    path1 = r'C:\projects\data-cleaning-automation\outputs\chart_category.png'
    plt.savefig(path1)
    plt.close()
    charts.append(path1)

    # Chart 2 - Sales by Region
    fig, ax = plt.subplots(figsize=(8, 4))
    reg = df.groupby('Region')['Sales'].sum()
    reg.plot(kind='pie', ax=ax, autopct='%1.1f%%')
    ax.set_title('Sales Distribution by Region')
    ax.set_ylabel('')
    plt.tight_layout()
    path2 = r'C:\projects\data-cleaning-automation\outputs\chart_region.png'
    plt.savefig(path2)
    plt.close()
    charts.append(path2)

    return charts

def generate_pdf_report(df, clean_report, output_path=None):
    if output_path is None:
        output_path = r'C:\projects\data-cleaning-automation\outputs\report.pdf'

    charts = generate_charts(df)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Page 1 - Summary
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 20)
    pdf.cell(0, 12, 'Data Cleaning & Analysis Report', ln=True, align='C')
    pdf.set_font('Helvetica', '', 11)
    pdf.cell(0, 8, 'Dataset: Sample - Superstore.csv', ln=True, align='C')
    pdf.ln(8)

    # Cleaning Summary Box
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(0, 10, 'Data Cleaning Summary', ln=True)
    pdf.set_font('Helvetica', '', 11)

    items = [
        ('Original Rows', clean_report['original_rows']),
        ('Cleaned Rows', clean_report['cleaned_rows']),
        ('Duplicates Removed', clean_report['duplicates_removed']),
        ('Negative Sales Removed', clean_report['negative_sales_removed']),
        ('Total Columns', clean_report['cleaned_cols']),
    ]
    for label, value in items:
        pdf.cell(90, 8, f'  {label}:', border=0)
        pdf.cell(0, 8, str(value), ln=True)

    # Sales Stats
    pdf.ln(5)
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(0, 10, 'Sales Statistics', ln=True)
    pdf.set_font('Helvetica', '', 11)
    stats = [
        ('Total Sales', f"${df['Sales'].sum():,.2f}"),
        ('Average Sales', f"${df['Sales'].mean():,.2f}"),
        ('Max Sale', f"${df['Sales'].max():,.2f}"),
        ('Min Sale', f"${df['Sales'].min():,.2f}"),
        ('Total Orders', str(len(df))),
    ]
    for label, value in stats:
        pdf.cell(90, 8, f'  {label}:', border=0)
        pdf.cell(0, 8, value, ln=True)

    # Page 2 - Charts
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 14)
    pdf.cell(0, 10, 'Visual Summaries', ln=True)
    for chart in charts:
        pdf.image(chart, x=10, w=190)
        pdf.ln(5)

    pdf.output(output_path)
    print(f"✅ PDF report saved: {output_path}")