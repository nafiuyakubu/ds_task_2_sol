# This project is a toy project for training and quality assurance purposes

# Task 2

We want to test your ability to research and solve a problem.

Steps:

1. Import sales_data_sample.csv into panda and create a dataframe
2. Make a flask api that we can ask natural language question and we can give back a human answer based on the data in your dataframe. You decide which algorithm you would you and explain why. If your logic can't answer complex query, we consider this done incorrectly.

Test Cases:
What is my top earning sale item?

Which city has my best sales?

Sales Performance Analysis: Find the top 5 products with the highest total sales in the last quarter of 2003, but only for orders that were shipped and had a minimum order quantity of 40 units.

Customer Segmentation Query: Identify customers who placed more than 3 orders above $5000 each in 2003, but only include those from the USA or France.

Product Demand Fluctuation: Determine which month in 2003 had the highest average order quantity for a specific product, but only consider months where the total sales exceeded $100,000 and the product price was above $80.

Regional Sales Comparison: Compare the average order value between two specific states (e.g., CA and NY) in 2003, but only for orders that were shipped and had at least 20 units ordered.

Order Fulfillment Efficiency: For orders placed in the first half of 2003, find out which country had the highest proportion of orders shipped within 30 days of order placement, but only include countries with more than 50 total orders.

Sales Trend Analysis: Identify if there was a month in 2003 where sales for a particular product category increased by more than 25% compared to the previous month, but only if the average price of the product was below $100 during that month.


3. I want you to make a simple filtering flask api that given an order, you can tell if customer is male or female. So pass in the order id and get gender back. Cannot use openai for this. You need to figure it out or find an algorithm that works.

4. I want you to make a simple recommendation engine where user can pass in a month to the flask api and get back a recommendation for a trend happening or anomaly in that month. You need to figure it out or find an algorithm that works.
