

#  Customer Purchase Behavior Analysis

### Product Data Analytics Case Study (Instacart)

---

## 📊 Dashboard

![Customer Purchase Behavior Dashboard](./Customer%20Purchase%20Behavior%20Analysis.png)

---

## Project Overview

This project analyzes customer purchasing behavior using the Instacart dataset with a focus on **product analytics and user behavior insights**.

The goal was to:

* Identify key behavioral patterns in ordering
* Understand product demand and loyalty
* Measure engagement through reorder behavior
* Design a dashboard for decision-making

This project simulates a real-world **Product Data Analyst workflow**, combining:

* Data extraction (SQL)
* Data processing (Python)
* Insight generation
* UX-focused data visualization (Tableau)

---

## Business Questions

* When are users most active?
* What products drive the highest demand?
* Which categories generate repeat purchases?
* How strong is customer loyalty?
* Which products have the highest retention potential?

---

## Dataset

Source: **Instacart Market Basket Analysis**

### Tables used:

* `orders` — user orders with timestamps
* `products` — product catalog
* `departments` — product categories
* `order_products_prior` & `train` — purchase history

---

## Data Cleaning & Preparation

### Key steps:

* Merged datasets into a unified `master_table`
* Filtered dataset (~300K rows per table for performance)
* Handled missing values (`days_since_prior_order`)
* Standardized column types
* Validated joins between entities

### Final structure:

Each row = **one product within one order**

---

## Data Processing

### Stack:

* PostgreSQL
* Python (pandas, SQLAlchemy)
* SQL

---

## Metrics & SQL Analysis

### Core Product Metrics

```sql
-- Total Orders
SELECT COUNT(DISTINCT order_id)

-- Total Users
SELECT COUNT(DISTINCT user_id)

-- Avg Products per Order
SELECT AVG(product_count)
FROM (
    SELECT order_id, COUNT(product_id)
    FROM master_table
    GROUP BY order_id
) t;
```

---

### Behavioral Metrics

* Orders by hour
* Orders by weekday
* Reorder rate
* Reorder rate by department
* Top products
* Most loyal product (high reorder rate + sufficient volume)

---

## 📈 Key Insights

---

### Peak Usage Behavior

* Peak hours: **10:00 – 16:00**
* Lowest activity: **00:00 – 06:00**

**Product Insight:**
Users interact with the product during daytime → likely tied to planning meals or daily routines.

**Actionable Idea:**

* Schedule promotions & notifications during peak hours
* Optimize delivery slots for midday demand

---

### Weekly Behavior Patterns

* Highest demand: **Sunday (~51K orders)**
* Second peak: **Monday (~50K orders)**

**Product Insight:**

* Weekend = bulk shopping behavior
* Monday = replenishment cycle

**Actionable Idea:**

* Launch weekend campaigns (bundles, discounts)
* Use Monday for retention nudges

---

### Product Demand

Top products:

* Banana
* Organic Bananas
* Organic Strawberries
* Spinach
* Avocado

**Product Insight:**

* Strong dominance of **fresh produce**
* High demand for **organic products**

**Actionable Idea:**

* Prioritize fresh category in UI
* Highlight organic filters
* Bundle popular items

---

### Customer Retention & Loyalty

* Overall reorder rate: **~59%**

**Product Insight:**

* High repeat behavior → habit-driven usage
* Indicates strong product-market fit

**Actionable Idea:**

* Implement “Buy Again” features
* Personalized recommendations based on reorder history

---

### Category-Level Retention

Top departments:

* Dairy & Eggs (~67%)
* Beverages (~65%)
* Produce (~65%)

Lowest:

* Personal Care (~32%)
* Pantry (~34%)

**Product Insight:**

* Essentials = high retention
* Occasional items = low engagement

**Actionable Idea:**

* Focus retention strategies on high-frequency categories
* Use recommendations to boost low-frequency categories

---

### Most Loyal Product

* **Plain Soymilk Creamer**
* Reorder rate: **~89%**

**Product Insight:**

* Small niche but extremely loyal segment
* Indicates strong product stickiness

**Actionable Idea:**

* Identify similar products (high reorder rate)
* Promote them via personalization

---

## UX & Dashboard Design

### Design Principles:

* KPI-first layout → quick overview
* Logical grouping:

  * Behavior (time/day)
  * Products
  * Retention
* Clean visual hierarchy
* Low cognitive load

### Goal:

Enable stakeholders to quickly answer:

* When do users order?
* What do they buy?
* What drives retention?

---

## Outcome

This project demonstrates:

* End-to-end data workflow (raw → insights)
* Product thinking in analytics
* Ability to translate data into business actions
* Dashboard design for decision-making

---

## Tech Stack

* Python (pandas, SQLAlchemy)
* PostgreSQL
* SQL
* Tableau
* Git / GitHub

---

## Future Improvements

* Cohort analysis (retention over time)
* User segmentation (power users vs casual)
* Recommendation system prototype
* A/B testing scenarios for promotions

