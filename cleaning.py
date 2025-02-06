import pandas as pd

# Define file paths
input_file = "/Users/deborahloring/Documents/EBR_Building_Permits.csv"
output_file = "/Users/deborahloring/Documents/EBR_Building_Permits_cleaned.csv"

# Load the CSV
df = pd.read_csv(input_file)

# Standardize column names (strip spaces, convert to uppercase)
df.columns = df.columns.str.strip().str.upper()

# Define categorical and numerical columns
categorical_cols = [
    'PERMIT TYPE', 'DESIGNATION', 'PROJECT DESCRIPTION', 'LOT NUMBER',
    'SUBDIVISION', 'CITY', 'STATE', 'PARISH NAME', 'OWNER NAME', 
    'APPLICANT NAME', 'CONTRACTOR NAME'
]

numerical_cols = ['ZIP', 'SQUARE FOOTAGE', 'PROJECT VALUE', 'PERMIT FEE']

# Convert date columns to datetime
df['CREATION DATE'] = pd.to_datetime(df['CREATION DATE'], errors='coerce')
df['ISSUED DATE'] = pd.to_datetime(df['ISSUED DATE'], errors='coerce')

# Handle missing values
df[categorical_cols] = df[categorical_cols].fillna('Unknown')
df[numerical_cols] = df[numerical_cols].fillna(0)

# Standardize text format (strip spaces, convert to title case)
df[categorical_cols] = df[categorical_cols].apply(lambda x: x.str.strip().str.title())

# Drop irrelevant columns
df_cleaned = df.drop(columns=['INTERNAL ID', 'CONTRACTOR ADDRESS'])

# Save cleaned data
df_cleaned.to_csv(output_file, index=False)

print(f"Cleaned CSV saved to: {output_file}")