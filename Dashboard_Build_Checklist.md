# Interactive Dashboard Build Checklist

## Looker Studio route
1. Import `ApexPlanet_Task3_Analysis.xlsx` into Google Sheets.
2. Keep the `Enriched_Data` sheet as the main dashboard data source.
3. Open Looker Studio and create a new report.
4. Add the Google Sheet as the data source.
5. Add KPI scorecards:
   - SUM(Total_Sales)
   - COUNT_DISTINCT(Order_ID)
   - AVG(Total_Sales)
   - SUM(Quantity)
   - COUNT_DISTINCT(Customer_ID)
6. Add charts:
   - Time series: Order_Date vs SUM(Total_Sales)
   - Bar chart: Category vs SUM(Total_Sales)
   - Bar chart: City vs SUM(Total_Sales)
   - Bar/donut: Segment vs SUM(Monetary)
   - Table: Customer_ID, Segment, Monetary, Frequency, Recency
7. Add filters for Date, Category, City, Gender and Segment.
8. Turn on chart interactions/cross-filtering.
9. Share/publish the dashboard and copy the live link for GitHub.

## Tableau Public route
Use the `Enriched_Data` sheet from `ApexPlanet_Task3_Analysis.xlsx` and build the same two dashboard pages: Executive Overview and Customer Deep Dive.
