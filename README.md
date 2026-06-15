# 🍽️ Zomato Repeat Order Optimization

> Product Management Case Study focused on improving customer retention and repeat purchases through data-driven product strategy.

---

# 📌 Executive Summary

Food delivery platforms operate in a highly competitive market where retaining existing customers is significantly cheaper than acquiring new ones.

This project investigates why users fail to place repeat orders on Zomato and proposes a product solution designed to improve retention, engagement, and revenue.

After conducting user research, funnel analysis, and metric evaluation, the project identifies **decision fatigue** as a major friction point and proposes a **Smart Reorder Hub** to streamline repeat purchases.

### Business Goal

Increase Repeat Order Rate from **42% → 48%** within six months.

### Expected Impact

- +6% Repeat Order Rate
- +13% Revenue
- +8% User Retention
- Reduced Time-to-Order

---

# 🎯 Problem Statement

Many users revisit food delivery platforms but do not complete repeat purchases despite having strong preferences for previously ordered restaurants and meals.

Analysis indicates that users spend excessive time browsing through restaurants before making a purchase decision.

This creates:

- Decision fatigue
- Lower conversion rates
- Reduced ordering frequency
- Lower customer lifetime value

### Key Question

**How might Zomato increase repeat ordering behavior while reducing user effort during meal selection?**

---

# 🔍 User Research

## Research Approach

### Quantitative Analysis

- Order frequency
- Repeat purchase behavior
- Revenue per user
- Retention metrics
- Restaurant preferences

### Qualitative Analysis

User interviews were conducted across:

#### Frequent Users

Goals:

- Understand loyalty drivers
- Identify repeat purchase triggers
- Discover favorite restaurant patterns

#### Churned Users

Goals:

- Identify drop-off reasons
- Understand switching behavior
- Discover unmet needs

---

## Key Insights

### Insight 1

Users repeatedly order from familiar restaurants.

### Insight 2

Restaurant discovery often takes longer than actual checkout.

### Insight 3

Users frequently abandon sessions due to excessive browsing.

### Insight 4

Most repeat purchases occur within previously visited restaurants.

---

# 📊 Funnel Analysis

Current User Journey

```text
App Open
   ↓
Restaurant View
   ↓
Add To Cart
   ↓
Checkout
   ↓
Order Placed
   ↓
Repeat Order
```

## Major Drop-Off

The largest conversion loss occurs between:

```text
Restaurant View → Add To Cart
```

### Root Cause

Users struggle to quickly decide what to order despite having historical ordering preferences.

---

# 💡 Product Solution

## Smart Reorder Hub

A personalized homepage section enabling users to quickly reorder meals they already enjoy.

### Features

### Order Again

One-click reorder from previous purchases.

### Favorite Restaurants

Personalized restaurant shortcuts.

### Smart Recommendations

Suggestions based on:

- Time of day
- Previous purchases
- Cuisine preferences

### Personalized Ranking

Most frequently ordered restaurants appear first.

---

# 🧠 Product Prioritization

The RICE framework was used to evaluate potential solutions.

| Feature | Reach | Impact | Confidence | Effort |
|----------|--------|---------|------------|---------|
| Smart Reorder Hub | High | High | High | Low |
| Loyalty Program | High | Medium | High | Medium |
| Meal Planner | Medium | Medium | Medium | High |
| AI Suggestions | Medium | High | Medium | High |

### Selected Solution

✅ Smart Reorder Hub

Reason:

Highest projected impact with lowest implementation effort.

---

# 🧪 Experiment Design

## Hypothesis

Users exposed to the Smart Reorder Hub will place repeat orders more frequently than users using the current homepage.

## Experiment

### Control Group

Current homepage experience.

### Treatment Group

Homepage with Smart Reorder Hub.

---

## Success Metrics

### Primary Metric

Repeat Order Rate

### Secondary Metrics

- Orders Per User
- Revenue Per User
- Cart Conversion Rate
- Session Duration

### Guardrail Metrics

- Checkout Failures
- Customer Support Tickets
- Application Crash Rate

---

# 📈 Dashboard Overview

A 5-page Power BI dashboard was developed to evaluate business performance and product impact.

## Page 1 — Executive Overview

Tracks:

- Revenue
- Orders
- Average Order Value
- Revenue Per User

---

## Page 2 — Funnel Analysis

Tracks:

- Conversion Rates
- User Drop-Off
- Funnel Efficiency

---

## Page 3 — Retention Dashboard

Tracks:

- Monthly Active Users
- Repeat Purchase Rate
- User Retention

---

## Page 4 — Restaurant Insights

Tracks:

- Top Restaurants
- Cuisine Preferences
- City-Level Demand

---

## Page 5 — Feature Impact Simulator

Compares:

- Before Implementation
- After Implementation

for key business metrics.

---

# 📏 Key Product Metrics

## Acquisition

- New Users
- App Installs

## Engagement

- DAU
- MAU
- Session Duration

## Conversion

- Add-to-Cart Rate
- Checkout Rate
- Order Conversion Rate

## Retention

- Day 7 Retention
- Day 30 Retention
- Repeat Order Rate

## Revenue

- Average Order Value
- Revenue Per User
- Customer Lifetime Value

---

# 🛠️ Tech Stack

### Product Management

- User Research
- Product Strategy
- Roadmapping
- A/B Testing
- KPI Definition

### Analytics

- Python
- Pandas
- NumPy
- SQL

### Visualization

- Power BI

---

# 📂 Project Structure

```text
zomato-repeat-order-optimization/
│
├── data/
├── sql/
├── src/
├── docs/
├── dashboard/
└── README.md
```

---

# 🚀 Business Impact

By reducing decision fatigue and simplifying repeat purchases, the proposed solution is expected to:

- Increase Repeat Order Rate by 6%
- Improve Customer Retention by 8%
- Increase Revenue by 13%
- Reduce Ordering Friction

The project demonstrates a complete Product Management workflow from problem discovery to solution validation and business impact estimation.

---

# 👨‍💻 Author

**V Sanjesh**

Product Management Portfolio Project

Focused Areas:

- Product Strategy
- Growth
- Analytics
- User Experience
- Experimentation