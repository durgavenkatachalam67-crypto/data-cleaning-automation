import pandas as pd
import numpy as np

def load_raw_data(path=None):
    if path is None:
        path = r'C:\projects\data-cleaning-automation\data\raw\Sample - Superstore.csv'
    df = pd.read_csv(path, encoding='latin-1')
    return df

def clean_data(df):
    report = {}

    # 1. Original shape
    report['original_rows'] = len(df)
    report['original_cols'] = len(df.columns)

    # 2. Remove duplicates
    before = len(df)
    df.drop_duplicates(inplace=True)
    report['duplicates_removed'] = before - len(df)

    # 3. Handle missing values
    report['missing_before'] = df.isnull().sum().to_dict()
    df['Postal Code'] = df['Postal Code'].fillna(0).astype(int)
    df.dropna(inplace=True)
    report['missing_after'] = df.isnull().sum().to_dict()

    # 4. Fix data types
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])

    # 5. Fix inconsistent text
    df['City'] = df['City'].str.strip().str.title()
    df['State'] = df['State'].str.strip().str.title()
    df['Category'] = df['Category'].str.strip()
    df['Sub-Category'] = df['Sub-Category'].str.strip()

    # 6. Remove negative sales
    before = len(df)
    df = df[df['Sales'] > 0]
    report['negative_sales_removed'] = before - len(df)

    # 7. Final shape
    report['cleaned_rows'] = len(df)
    report['cleaned_cols'] = len(df.columns)

    return df, report