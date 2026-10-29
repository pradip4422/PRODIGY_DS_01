
import pandas as pd
import matplotlib.pyplot as plt

# Load the World Bank population dataset
file_path = "API_SP.POP.TOTL_DS2_en_csv_v2_5254.csv"

# World Bank CSV has metadata rows at the beginning
df = pd.read_csv(file_path, skiprows=4)

# Select the latest available year
year_columns = [
    col for col in df.columns
    if str(col).isdigit()
]

latest_year = year_columns[-1]

# Prepare data for the bar chart
df[latest_year] = pd.to_numeric(
    df[latest_year], errors="coerce"
)

data = df[["Country Name", latest_year]].dropna()

# Select the 10 most populated countries
top_10 = data.nlargest(10, latest_year)

# Display the data
print("Top 10 Countries by Population")
print(top_10.to_string(index=False))
print("\nYear:", latest_year)

# Create the bar chart
plt.figure(figsize=(12, 6))
plt.bar(top_10["Country Name"], top_10[latest_year])

plt.title(f"Top 10 Countries by Population ({latest_year})")
plt.xlabel("Country")
plt.ylabel("Population")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

# Save and display the chart
plt.savefig("population_bar_chart.png", dpi=300)
plt.show()

print("\nChart saved as population_bar_chart.png")
