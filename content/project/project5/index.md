---
title: Lead Scoring Analysis and Segmentation 
summary: A lead scoring analysis is conducted for an online teaching company with a low client conversion rate. The goals are to reverse this trend by using a machine learning model based on available company data and to categorize customers with an effective segmentation.
tags:
  - Machine Learning
date: 2024-08-21
#external_link: http://github.com
---
*Note: Documentation available on the [GitHub Repository](https://github.com/pabloelt/analysis-and-optimization-of-an-ecommerce-company) is currently in Spanish. It will be soon updated to English.*
{style="color: #aaaaaa"}

{{< toc >}}

## 1. Introduction
{style="color: #BBDEFC"}

The client for this project is an online teaching company that offers a high-value online course designed to train professionals in the data science sector. The company advertises this course on various websites and search engines. When people visit the website—promoted effectively by the marketing department—they may browse the course, fill out a form, or watch related videos. If they provide their email address or phone number through a form, they are classified as a lead. Additionally, the company also acquires leads through referrals from past clients.

Once these leads are acquired, the sales team begins reaching out via calls, emails, and other forms of communication. However, while some leads convert into customers, most do not, leading to inefficiencies that negatively impact the company’s profitability.

Notes:

* This article presents a technical explanation of the development process followed in the project.
* Source code can be found [here](https://github.com/pabloelt/analysis-and-optimization-of-an-ecommerce-company).

---

## 2. Objectives
{style="color: #BBDEFC"}

The main objective is to analyse the historical leads information of the company to propose potential actions that will increase the overall turnover and reverse the low conversion rate at which the company is operating. To achieve this goal, we will create advanced analytical assets such as:

* <text style='color: #BBDEFC; font-weight: normal;'>Predictive lead scoring algorithm:</text> This tool will assist the sales team in identifying potential customers who are most likely to convert into final clients, as well as leads that are not economically viable to pursue.
* <text style='color: #BBDEFC; font-weight: normal;'>Customer segmantation algorithm:</text> It will help to identify the key customer groups interested in the product, enabling the sales team to tailor marketing efforts effectively for each identified segment."

---

## 3. Understanding of the problem
{style="color: #BBDEFC"}


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

{{< figure src="/project3/customerjourney.png" title="Custom journey in an ecommerce company." >}}


### 3.1 Levers
{style="color: #BBDEFC; font-weight: normal"}

The levers for this project are clear and are summarized below:

* <text style='color: #BBDEFC; font-weight: normal;'>Customer journey:</text> How can we optimize each step of the process?
* <text style='color: #BBDEFC; font-weight: normal;'>Customers:</text> How can we use available customer information to optimize our campaigns?
* <text style='color: #BBDEFC; font-weight: normal;'>Products:</text> How can we optimize the product catalog and personalize which products we present to each customer?


### 3.2 KPIs
{style="color: #BBDEFC; font-weight: normal"}

The KPIs that results from the above-mentioned levers are the following:

* <text style='color: #BBDEFC; font-weight: normal;'>Views:</text> Number of views of the products available in the ecommerce website.
* <text style='color: #BBDEFC; font-weight: normal;'>Conversion rate:</text> Number of items that are finally purchased from the views in the ecommerce website.
* <text style='color: #BBDEFC; font-weight: normal;'>Purchase frequency:</text> Number of times a user makes a purchase on the ecommerce website.
* <text style='color: #BBDEFC; font-weight: normal;'>CPA (Cost Per Acquisition):</text> Aggregate cost of acquiring a customer through a marketing campaign.
* <text style='color: #BBDEFC; font-weight: normal;'>AOV (Average Order Value):</text> Average value of customer shopping carts, providing insight into the average amount users spend on the ecommerce site.
* <text style='color: #BBDEFC; font-weight: normal;'>LTV (Lifetime Value):</text> Predicts the average profit from a customer throughout their entire lifetime as a buyer on the ecommerce site.
* <text style='color: #BBDEFC; font-weight: normal;'>Churn rate:</text> Metric indicating the number of customers who no longer purchase services from the ecommerce site.


### 3.3 Entities and Data
{style="color: #BBDEFC; font-weight: normal"}

The most relevant entities from which we can obtain data are summarized below:

* <text style='color: #BBDEFC; font-weight: normal;'>User:</text> User ID.
* <text style='color: #BBDEFC; font-weight: normal;'>Date:</text> Operation date.
* <text style='color: #BBDEFC; font-weight: normal;'>Session:</text> Session ID.
* <text style='color: #BBDEFC; font-weight: normal;'>Event:</text> View, add to cart, remove from cart, purchase.
* <text style='color: #BBDEFC; font-weight: normal;'>Product:</text> Category, product id, price.

---

## 4. Data Quality
{style="color: #BBDEFC"}

In this stage of the project, general data quality correction processes have been applied, such as:

* Data renaming.
* Type correction.
* Proper selection of the most relevant data for the project.
* Analysis of nulls and duplicated registers.
* Analysis of numerical and categorical variables.
* Discretization of variables.
* Creation of new variables.

The entire process can be consulted in detail [here](https://github.com/pabloelt/analysis-and-optimization-of-an-ecommerce-company/blob/main/Notebooks/02_Creacion%20del%20Datamart%20Analitico.ipynb).

---

## 5. Exploratory Data Analysis
{style="color: #BBDEFC"}

The aim of this phase of the project is to identify trends and patterns that can be transformed into insights, providing valuable information for our project. To achieve this, we perform various statistical evaluations and create graphical representations.

In order to guide this process, a series of seed questions are proposed to serve as a basis for the analysis.

### 5.1 Seed questions
{style="color: #BBDEFC; font-weight: normal"}

**Regarding customer journey:**

* <text style='color: #BBDEFC; font-weight: normal;'>Q1:</text> What does a typical shopping process look like?
* <text style='color: #BBDEFC; font-weight: normal;'>Q2:</text> How many products are viewed, added to cart, abandoned and purchased on average per session?
* <text style='color: #BBDEFC; font-weight: normal;'>Q3:</text> How have these metrics been trending in recent months?

**Regarding clients:**

* <text style='color: #BBDEFC; font-weight: normal;'>Q4:</text> How many products does each customer buy?
* <text style='color: #BBDEFC; font-weight: normal;'>Q5:</text> How much does each customer spend on average?
* <text style='color: #BBDEFC; font-weight: normal;'>Q6:</text> Are there ‘good customers’ that need to be identified and treated differently?
* <text style='color: #BBDEFC; font-weight: normal;'>Q7:</text> Do customers repeat purchases in the following months?
* <text style='color: #BBDEFC; font-weight: normal;'>Q8:</text> What is the average LTV of a customer?
* <text style='color: #BBDEFC; font-weight: normal;'>Q9:</text> Can campaigns can be tailored to customer’s value?

**Regarding products:**

* <text style='color: #BBDEFC; font-weight: normal;'>Q10:</text> What are the best-selling products?
* <text style='color: #BBDEFC; font-weight: normal;'>Q11:</text> Are there products that do not sell?
* <text style='color: #BBDEFC; font-weight: normal;'>Q12:</text> Is there a relationship between the price of the product and its sales volume?
* <text style='color: #BBDEFC; font-weight: normal;'>Q13:</text> Are there products that are visited but not purchased?
* <text style='color: #BBDEFC; font-weight: normal;'>Q14:</text> Are there products that are recurrently removed from the cart?
* <text style='color: #BBDEFC; font-weight: normal;'>Q15:</text> Could personalized product recommendations be made for each customer?


### 5.2 Insights
{style="color: #BBDEFC; font-weight: normal"}

Once the exploratory data analysis has been conducted, the following insights have been obtained:

* <text style='color: #BBDEFC; font-weight: normal;'>Insight 1:</text> The conversion rates are very poor.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 2:</text> The average session numbers are low.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 3:</text> The most popular purchasing hours are at 1 am, 8 am, from 11 am to 1 pm, and at 6 pm.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 4:</text> Weekly trends show a peak on the 22nd, possibly due to the start of Black Friday week.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 5:</text> Most customers make only one purchase and spend an average of less than 50€.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 6:</text> 90% of new customers do not make a repeat purchase in the subsequent months.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 7:</text> The average LTV is 42€.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 8:</text> Prime customers are identified though the RFM analysis.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 9:</text> Nearly half of the products have not been purchased in the last five months.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 10:</text> A powerful recommendation system adapted to the user's views is developed.

 A more detailed analysis of this stage can be found [here](https://github.com/pabloelt/analysis-and-optimization-of-an-ecommerce-company/blob/main/Notebooks/03_Analisis%20e%20Insights.ipynb).


---

## 6. Results Communication
{style="color: #BBDEFC"}

In this stage of the project, we are presenting the insights that we have obtained during the exploratory data analysis and the main conclusions for each of them.

<text style='color: #BBDEFC; font-weight: normal;'>The conversion rates are very poor</text>

* 60% from views to cart additions.
* 22% from cart additions to purchases.
* 13% from views to purchases.

{{< figure src="/project3/exhibit_1.png" title="Exhibit 1: Baseline conversion rates." >}}



<text style='color: #BBDEFC; font-weight: normal;'>Average session numbers are low</text>

* 2.2 products are viewed.
* 1.3 products are added to the cart.
* 0.9 products are removed from the cart.
* 0.3 products are purchased.

With these values the average monthly revenue is found to be around 125.000€

{{< figure src="/project3/exhibit_2.png" title="Exhibit 2: Baseline average session numbers." >}}



<text style='color: #BBDEFC; font-weight: normal;'>The most popular purchasing hours are at 1 am, 8 am, from 11 am to 1 pm, and at 6 pm</text>

* This information is highly relevant, particularly for strategies involving paid ads, both for generating traffic and for retargeting efforts.

* Additionally, there appears to be a user subtype that makes purchases at 1 AM. While not occurring frequently, this group tends to spend significantly when they do make purchases.

{{< figure src="/project3/exhibit_3.png" title="Exhibit 3: Hourly analysis of the main events on the ecommerce website." >}}



<text style='color: #BBDEFC; font-weight: normal;'>Weekly trends show a peak on the 22nd, possibly due to the start of Black Friday week</text>

* Weekly analysis during the five months:

{{< figure src="/project3/exhibit_4_1.png" title="Exhibit 4.1: Weekly analysis of the main events on the ecommerce website." >}}

* Daily analysis around the Black Friday campaign:

{{< figure src="/project3/exhibit_4_2.png" title="Exhibit 4.2: Daily analysis of the main events around the Black Friday Campaign." >}}



<text style='color: #BBDEFC; font-weight: normal;'>Most customers make only one purchase and spend an average of less than 50€</text>

* The median purchase currently includes only 5 products, indicating there is significant potential for improvement in this ratio through the implementation of recommendation systems.

{{< figure src="/project3/exhibit_5.png" title="Exhibit 5: Bar plots for the evolution of the spent money and the numbers of items purchased by the customers." >}}



<text style='color: #BBDEFC; font-weight: normal;'>90% of new customers do not make a repeat purchase in the subsequent months</text>

* A customers cohort analysis is performed:

{{< figure src="/project3/exhibit_6.png" title="Exhibit 6: Customers cohort analysis." >}}



<text style='color: #BBDEFC; font-weight: normal;'>The average LTV is 42€</text>

* Implementing CRO actions will increase the LTV, thereby enhancing our strategic advantage.

{{< figure src="/project3/exhibit_7.png" title="Exhibit 7: Metrics for the total spent money by the customers. The median value is adopted since there are some anomalous values." >}}



<text style='color: #BBDEFC; font-weight: normal;'>Prime customers are identified though the RFM analysis</text>

* Thanks to the RFM analysis, we can identify our top-tier customers and tailor more targeted campaigns based on this information.

{{< figure src="/project3/exhibit_8.png" title="Exhibit 8: RFM analysis applied to identify the top-tier customers." >}}



<text style='color: #BBDEFC; font-weight: normal;'>Nearly half of the products have not been purchased in the last five months</text>

* They should be eliminated or, at least, properly investigated.

{{< figure src="/project3/exhibit_9.png" title="Exhibit 9: Pie diagram for the number of purchased products during the last five months." >}}



<text style='color: #BBDEFC; font-weight: normal;'>A powerful recommendation system adapted to the user's views is developed</text>

A basic recommendation system based on the most sold items:

{{< figure src="/project3/exhibit_10_1.png" title="Exhibit 10.1: Basic recommendation system." >}}

The powerful recommendation system optimised for the customers preferences:

{{< figure src="/project3/exhibit_10_2.png" title="Exhibit 10.2: Powerful and optimised recommendation system." >}}

---

## 7. Actionable initiatives
{style="color: #BBDEFC"}

A plan of 10 specific initiatives, organized into five major business levers, has been derived from the exploratory data analysis to break the stagnant trend in the company over the last few months and achieve an overall increase in ecommerce revenues:

<text style='color: #BBDEFC; font-weight: normal;'>Actions to increase the number of views:</text>

1. Review paid campaigns (generation and retargeting) to focus investment during the time slots between 9 am and 1 pm, and between 6 pm and 8 pm.
2. Concentrate investment for the Christmas and post-Christmas period during the Black Friday week.
3. Increase investment to reach the maximum CPA based on the identified LTV.

<text style='color: #BBDEFC; font-weight: normal;'>Actions to increase conversion rates:</text>

4. Preconfigure the homepage with the products identified in the "most viewed" and "most sold" analyses.
5. Work on products with a high cart abandonment rate.
6. Work on products that are frequently viewed but infrequently purchased.

<text style='color: #BBDEFC; font-weight: normal;'>Actions to increase cross-selling:</text>

7. The median purchase is 5 products at the moment. To increase this ratio, implement real-time recommendations using the new recommendation system.

<text style='color: #BBDEFC; font-weight: normal;'>Actions to increase purchase frequency:</text>

8. The 90% of the customers only make a single purchase. Create a periodic newsletter using the new recommendation system to increase visit frequency.
9. Run promotional campaigns targeting the top segments identified in the RFM segmentation.

<text style='color: #BBDEFC; font-weight: normal;'>Actions to improve customer loyalty:</text>

10. Create a loyalty program based on the new RFM segmentation.

---

## 8. Business case implementation
{style="color: #BBDEFC"}

We have also implemented a business case model for a neutral scenario, assuming that the new CRO protocols achieve the following:

* Increase the conversion rate from 13% to 15%.
* Increase the median purchase from 5 to 6 products, representing a 20% increase in this metric.
* Increase the purchase recency from 10% to 12%, representing a 20% increase in this metric.

After one year of applying these protocols, the results are as follows:

* The CRO protocols generated 249300€.
* The cost of implementing the measures was 114000€.
* The resultant profit is 135300€.
* The ROI (Return on Investment) is 118.68%.

The details of this analysis can be consulted [here](https://github.com/pabloelt/analysis-and-optimization-of-an-ecommerce-company/blob/main/Business_Case.xlsx).