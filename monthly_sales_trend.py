import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/sales_data_cleaned.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df = df.dropna(subset=["Order Date", "Sales"])

monthly = (
    df.assign(Month=df["Order Date"].dt.to_period("M").astype(str))
      .groupby("Month", as_index=False)["Sales"]
      .sum()
      .rename(columns={"Sales": "Total Sales"})
)

monthly["Total Sales"] = monthly["Total Sales"].round(2)
monthly.to_csv("../reports/monthly_sales_summary.csv", index=False)

plt.figure(figsize=(10, 5.5))
plt.plot(monthly["Month"], monthly["Total Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("../charts/monthly_sales_trend.png", dpi=180)
plt.show()
