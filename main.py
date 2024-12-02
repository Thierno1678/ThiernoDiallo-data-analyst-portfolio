import pandas as pd

# Define SEC teams list (matching the names in your data)
sec_teams = [
    "Alabama", "Arkansas", "Auburn", 
    "Florida", "Georgia", "Kentucky", 
    "LSU", "Ole Miss", 
    "Mississippi State", "Missouri", 
    "Oklahoma", "South Carolina", 
    "Tennessee", "Texas", 
    "Texas A&M", "Vanderbilt"
]

# Define the function to update the 'Conference' column
def update_conference(row):
    teams = row["Game (teams)"]
    for team in sec_teams:
        if team in teams:
            if pd.isna(row["Conference"]):
                return "SEC"
            elif "SEC" not in row["Conference"]:
                return row["Conference"] + ", SEC"
    return row["Conference"]

# Load the CSV file
df = pd.read_csv("your_file_path.csv")  # Replace 'your_file_path.csv' with the actual path to your CSV file

import pandas as pd

# Update these paths with the actual Excel file names
file_path_2022 = "C:/Users/Thierno/OneDrive/Attachments/CFB seasons/CFB season 2022 - CFB season 2022.xlsx"
file_path_2023 = "C:/Users/Thierno/OneDrive/Attachments/CFB seasons/CFB season 2023 - CFB season 2023.xlsx"
file_path_2024 = "C:/Users/Thierno/OneDrive/Attachments/CFB seasons/CFB season 2024 - CFB season 2024.xlsx"

# Load each Excel file
df_2022 = pd.read_excel(file_path_2022)
df_2023 = pd.read_excel(file_path_2023)
df_2024 = pd.read_excel(file_path_2024)

# Check the data to ensure it's loaded correctly
print(df_2022.head())
print(df_2023.head())
print(df_2024.head())

# Proceed with your data processing...
import pandas as pd

# Update these paths with the actual Excel file names
file_path_2022 = "C:/Users/Thierno/OneDrive/Attachments/CFB seasons/CFB season 2022 - CFB season 2022.xlsx"
file_path_2023 = "C:/Users/Thierno/OneDrive/Attachments/CFB seasons/CFB season 2023 - CFB season 2023.xlsx"
file_path_2024 = "C:/Users/Thierno/OneDrive/Attachments/CFB seasons/CFB season 2024 - CFB season 2024.xlsx"

# Load each Excel file
df_2022 = pd.read_excel(file_path_2022)
df_2023 = pd.read_excel(file_path_2023)
df_2024 = pd.read_excel(file_path_2024)

# Check the data to ensure it's loaded correctly
print(df_2022.head())
print(df_2023.head())
print(df_2024.head())
 
<path-to-your-env>\Scripts\activate     # On Windows
import pandas as pd

# Update this with the path to your 2024 season file
file_path_2024 = "C:/Users/Thierno/OneDrive/Attachments/CFB seasons/CFB season 2024 - CFB season 2024.csv"

# Load the 2024 data
df_2024 = pd.read_csv(file_path_2024)

# List of SEC teams for 2024 season with names exactly as in the data
sec_teams = [
    "Alabama", "Arkansas", "Auburn", "Florida", "Georgia", "Kentucky", 
    "LSU", "Ole Miss", "Mississippi State", "Missouri", "Oklahoma", 
    "South Carolina", "Tennessee", "Texas", "Texas A&M", "Vanderbilt"
]

# Function to update the Conference column
def update_conference(row):
    teams = row['Game (teams)']
    for team in sec_teams:
        if team in teams:
            # If 'Conference' is missing or doesn't include 'SEC', add it
            if pd.isna(row['Conference']):
                return "SEC"
            elif "SEC" not in row['Conference']:
                return row['Conference'] + ", SEC"
    return row['Conference']

# Apply the function to update the 'Conference' column
df_2024['Conference'] = df_2024.apply(update_conference, axis=1)

# Save the updated file
updated_file_path = "C:/Users/Thierno/OneDrive/Attachments/CFB seasons/CFB season 2024 - Updated.csv"
df_2024.to_csv(updated_file_path, index=False)

print(f"Updated 2024 season file saved to {updated_file_path}")
