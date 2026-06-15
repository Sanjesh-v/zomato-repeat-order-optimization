import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

np.random.seed(42)

# ----------------
# USERS
# ----------------

n_users = 10000

users = pd.DataFrame({
    "user_id": [f"U{i:05d}" for i in range(1, n_users + 1)],
    "signup_date": [
        fake.date_between(
            start_date="-2y",
            end_date="today"
        )
        for _ in range(n_users)
    ],
    "city": np.random.choice(
        ["Chennai","Bangalore","Mumbai","Delhi","Hyderabad"],
        n_users
    ),
    "gold_member": np.random.choice(
        ["Yes","No"],
        n_users,
        p=[0.35,0.65]
    )
})

# ----------------
# RESTAURANTS
# ----------------

n_restaurants = 100

restaurants = pd.DataFrame({
    "restaurant_id": [f"R{i:03d}" for i in range(1, n_restaurants + 1)],
    "cuisine": np.random.choice(
        [
            "Indian",
            "Chinese",
            "Italian",
            "South Indian",
            "Fast Food",
            "Desserts"
        ],
        n_restaurants
    ),
    "rating": np.round(
        np.random.uniform(3.5,4.9,n_restaurants),
        1
    )
})

# ----------------
# ORDERS
# ----------------

n_orders = 100000

orders = pd.DataFrame({
    "order_id": [f"O{i:06d}" for i in range(1, n_orders + 1)],
    "user_id": np.random.choice(users["user_id"], n_orders),
    "restaurant_id": np.random.choice(
        restaurants["restaurant_id"],
        n_orders
    ),
    "order_date": [
        fake.date_between(
            start_date="-1y",
            end_date="today"
        )
        for _ in range(n_orders)
    ],
    "amount": np.round(
        np.random.normal(450,120,n_orders),
        0
    )
})

orders["amount"] = orders["amount"].clip(lower=100)
orders["delivery_time"] = np.random.randint(
    20,
    70,
    len(orders)
)

orders["discount_used"] = np.random.choice(
    [0,1],
    len(orders),
    p=[0.7,0.3]
)

orders["platform"] = np.random.choice(
    ["Android","iOS"],
    len(orders)
)

users.to_csv("../data/users.csv", index=False)
restaurants.to_csv("../data/restaurants.csv", index=False)
orders.to_csv("../data/orders.csv", index=False)

print("Datasets Generated Successfully")