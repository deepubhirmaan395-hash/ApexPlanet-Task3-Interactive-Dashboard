import pandas as pd

df = pd.read_excel("ApexPlanet_Task1_Cleaned_Dataset.xlsx")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("Shape:", df.shape)
print("Total Revenue:", df["Total_Sales"].sum())
print("Total Orders:", df["Order_ID"].nunique())
print("Average Order Value:", df["Total_Sales"].mean())
print("Units Sold:", df["Quantity"].sum())
print("Unique Customers:", df["Customer_ID"].nunique())

monthly = df.groupby(df["Order_Date"].dt.to_period("M"))["Total_Sales"].sum()
print("\nMonthly Sales:")
print(monthly)

category = df.groupby("Category")["Total_Sales"].sum().sort_values(ascending=False)
print("\nSales by Category:")
print(category)

reference_date = df["Order_Date"].max() + pd.Timedelta(days=1)
customer = df.groupby("Customer_ID").agg(
    Last_Order=("Order_Date", "max"),
    Frequency=("Order_ID", "nunique"),
    Monetary=("Total_Sales", "sum")
).reset_index()

customer["Recency"] = (reference_date - customer["Last_Order"]).dt.days

customer["R_Score"] = pd.qcut(
    customer["Recency"].rank(method="first"), 5, labels=[5,4,3,2,1]
).astype(int)
customer["F_Score"] = pd.qcut(
    customer["Frequency"].rank(method="first"), 5, labels=[1,2,3,4,5]
).astype(int)
customer["M_Score"] = pd.qcut(
    customer["Monetary"].rank(method="first"), 5, labels=[1,2,3,4,5]
).astype(int)

customer["RFM_Score"] = (
    customer["R_Score"] + customer["F_Score"] + customer["M_Score"]
)

customer["Segment"] = pd.cut(
    customer["RFM_Score"],
    bins=[0,5,8,11,13,15],
    labels=["At Risk","Needs Attention","Potential","Loyal","Champions"],
    include_lowest=True
)

customer.to_csv("customer_segments.csv", index=False)
print("\nSegment summary:")
print(customer.groupby("Segment", observed=False)["Monetary"].agg(["count","sum","mean"]))
