import pandas as pd

def export_to_excel(df, output_path=None):
    if output_path is None:
        output_path = r'C:\projects\data-cleaning-automation\outputs\cleaned_data.xlsx'

    with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
        # Sheet 1 - Cleaned Data
        df.to_excel(writer, sheet_name='Cleaned Data', index=False)

        # Sheet 2 - Summary Stats
        summary = df.describe().round(2)
        summary.to_excel(writer, sheet_name='Summary Stats')

        # Sheet 3 - Sales by Category
        cat_sales = df.groupby('Category')['Sales'].sum().reset_index()
        cat_sales.to_excel(writer, sheet_name='Sales by Category', index=False)

        # Sheet 4 - Sales by Region
        region_sales = df.groupby('Region')['Sales'].sum().reset_index()
        region_sales.to_excel(writer, sheet_name='Sales by Region', index=False)

        # Formatting
        workbook = writer.book
        header_fmt = workbook.add_format({
            'bold': True, 'bg_color': '#4472C4',
            'font_color': 'white', 'border': 1
        })
        worksheet = writer.sheets['Cleaned Data']
        for col_num, col_name in enumerate(df.columns):
            worksheet.write(0, col_num, col_name, header_fmt)
            worksheet.set_column(col_num, col_num, 15)

    print(f"✅ Excel report saved: {output_path}")