import pandas as pd

# Load datasets

orders = pd.read_csv("../data/orders.csv")
users = pd.read_csv("../data/users.csv")

# -----------------------------
# Repeat Order Rate
# -----------------------------

user_orders = (
    orders.groupby("user_id")
    .size()
    .reset_index(name="order_count")
)

repeat_rate = (
    user_orders[user_orders["order_count"] >= 2]
    .shape[0]
    /
    user_orders.shape[0]
) * 100

print(f"\nRepeat Order Rate: {repeat_rate:.2f}%")

# -----------------------------
# Average Order Value
# -----------------------------

aov = orders["amount"].mean()

print(f"Average Order Value: ₹{aov:.2f}")

# -----------------------------
# Monthly Revenue
# -----------------------------

orders["order_date"] = pd.to_datetime(
    orders["order_date"]
)

orders["month"] = (
    orders["order_date"]
    .dt.to_period("M")
)

monthly_revenue = (
    orders.groupby("month")["amount"]
    .sum()
    .reset_index()
)

print("\nMonthly Revenue")

print(monthly_revenue.tail())

# -----------------------------
# Top Restaurants
# -----------------------------

top_restaurants = (
    orders.groupby("restaurant_id")
    .size()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop Restaurants")

print(top_restaurants)

# -----------------------------
# City Analysis
# -----------------------------

merged = orders.merge(
    users,
    on="user_id",
    how="left"
)

city_orders = (
    merged.groupby("city")
    .size()
    .sort_values(ascending=False)
)

print("\nOrders by City")

print(city_orders)

# -----------------------------
# Gold Member Analysis
# -----------------------------

gold_spend = (
    merged.groupby("gold_member")["amount"]
    .mean()
)

print("\nAverage Spend")

print(gold_spend)