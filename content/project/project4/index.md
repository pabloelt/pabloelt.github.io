---
title: Dream Resort Hotels Dynamic Dashboard
summary: An interactive and dynamic dashboard has been developed for a hotel group. The main KPIs, including turnover, ADR, number of reservations, occupancy rate, RevPAR, and cancellation rate, are visualized in the dashboard along with other relevant metrics.
tags:
  - Dashboards
date: 2024-07-02
#external_link: http://github.com
---
*Note: Documentation available on the [GitHub Repository](https://github.com/pabloelt/analysis-and-optimization-of-an-ecommerce-company) is currently in Spanish. It will be soon updated to English.*
{style="color: #aaaaaa"}

{{< toc >}}

## 1. Introduction
{style="color: #BBDEFC"}

The client for this project is a cosmetics ecommerce company based in Russia. They have experienced flat growth over the past few months and have hired us to analyze their transactional data and implement Conversion Rate Optimization (CRO) actions to reverse this situation.

Notes:

* This article presents a technical explanation of the development process followed in the project.
* Source code can be found [here](https://github.com/pabloelt/analysis-and-optimization-of-an-ecommerce-company).

---

## 2. Objectives
{style="color: #BBDEFC"}

The main objective is to analyze the transactional data to identify potential CRO actions that can increase visits, conversions, and average ticket size, thereby boosting the overall revenue of the ecommerce company. To achieve this goal, we will create advanced analytical assets such as:

* <text style='color: #BBDEFC; font-weight: normal;'>RFM Segmentation:</text> Analyzing customer data based on Recency, Frequency, and Monetary value to identify key customer segments and tailor marketing strategies accordingly.
* <text style='color: #BBDEFC; font-weight: normal;'>Recommendation System:</text> Developing a recommendation system to personalize the shopping experience, encouraging higher conversions and increasing the average ticket size.

These tools will help us implement effective CRO actions and drive substantial revenue growth.

---

## 3. Project Design
{style="color: #BBDEFC"}

To establish the levers, a brief explanation about the customer journey is requiered. The first step is when a user visits the ecommerce website. Typically, they will come from:

* <text style='color: #BBDEFC; font-weight: normal;'>Paid campaigns:</text> Paid ads such as Facebook Ads or Google Ads.
* <text style='color: #BBDEFC; font-weight: normal;'>Organic content:</text> Blog, social media, etc.
* <text style='color: #BBDEFC; font-weight: normal;'>Direct traffic:</text> Knows the URL and enters it directly into the browser.

The second step occurs when the user browses the website and adds a product to the cart.

* They can remove products from the cart, exit without making a purchase, or ultimately place an order.
* A common process is cross-selling, where other products that might interest the user are recommended.

The third step involves customer re-engagement through retargeting or email marketing.

{{< figure src="/project4/dashboard_desktop.png" title="" >}}

{{< figure src="/project4/dashboard_tablet.png" title="" >}}

{{< figure src="/project4/dashboard_phone.png" title="" >}}


