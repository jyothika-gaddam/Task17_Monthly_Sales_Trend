# Task 17 – Monthly Sales Trend

## Objective
Summarize sales by month and visualize the sales trend using a monthly table and line chart.

## Tools
- Excel / Google Sheets
- Python (Pandas, Matplotlib)

## Dataset
Sales_Dashboard_Data_200_Rows.csv was used as the source dataset. The analysis uses the `Order Date` and `Sales` columns.

## Steps Performed
1. Converted `Order Date` to a proper date format.
2. Removed rows where the date or sales value was missing.
3. Grouped sales by calendar month.
4. Calculated total sales for each month.
5. Sorted months chronologically.
6. Created a line chart to visualize the trend.

## Deliverables
- `data/sales_data_cleaned.csv` – cleaned source data
- `reports/monthly_sales_summary.csv` – monthly sales table
- `charts/monthly_sales_trend.png` – line chart
- `notebooks/monthly_sales_trend.py` – reproducible Python analysis
- `reports/monthly_sales_trend_report.md` – short report

## Key Results
- Total sales analyzed: 11,852,061.50
- Highest-sales month: 2025-03 (3,839,169.50)
- Lowest-sales month: 2025-04 (1,410,274.50)

## Interview Questions
**1. What is the best chart for time trends?**  
A line chart is commonly used because it clearly shows movement and changes over time.

**2. Why is date formatting important?**  
Correct date values allow chronological sorting and reliable grouping by month, quarter, or year.

**3. What is the main insight from this analysis?**  
The monthly table and line chart show how sales change from month to month and make higher- and lower-sales periods easy to identify.
