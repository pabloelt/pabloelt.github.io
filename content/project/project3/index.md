---
title: Analysis and Optimization of an Ecommerce Company 
summary: A comprehensive Conversion Rate Optimization (CRO) plan is developed to reverse the stagnant trend in an ecommerce company and drive a significant increase in its revenues. This plan consists of 10 specific initiatives, categorized into five key business levers.
tags:
  - Discovery Projects
date: 2024-06-24
#external_link: http://github.com
---
*Note: Documentation available on the [GitHub Repository](https://github.com/pabloelt/analysis-and-optimization-of-an-ecommerce-company) is currently in Spanish. It will be soon updated to English.*
{style="color: #aaaaaa"}

{{< toc >}}

## 1. Introduction
{style="color: #BBDEFC"}

TThe client for this project is a cosmetics ecommerce company based in Russia. They have experienced flat growth over the past few months and have hired us to analyze their transactional data and implement Conversion Rate Optimization (CRO) actions to reverse this situation.

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

{{< figure src="/project3/customerjourney.png" title="" >}}


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

* Users.
* Customers.
* Sessions.
* Events (view, add to cart, remove from cart, purchase).
* Products.

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

* <text style='color: #BBDEFC; font-weight: normal;'>Insight 1:</text> Ten neighborhoods with a high investment potential have been identified.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 2:</text> It is recommended to search for two-bedroom properties that can accommodate 4 guests.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 3:</text> It is recommended to search for properties in one of the identified neighborhoods that are not necessarily close to points of interest.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 4:</text> A new business model based on rentals for specific moments of high sporting interest should be explored.

 A more detailed analysis of this stage can be found [here](https://github.com/pabloelt/real-estate-market-analysis-rental-vacation/blob/main/Notebooks/05_Analisis%20e%20insights.ipynb).

---

## 6. Results Communication
{style="color: #BBDEFC"}

In this stage of the project, we are presenting the insights that we have obtained during the exploratory data analysis and the main conclusions for each of them.


<text style='color: #BBDEFC; font-weight: normal;'>Ten neighborhoods with a high investment potential have been identified</text>

* They can be segmented into 4 groups depending on the type, quality, and property location.
* These 4 groups, which have been identified, are the following:
  * *Low cost Investment*: Simancas, Ambroz, Marroquina, San Juan Bautista.
  * *Medium cost investment*: El Plantio, Valdemarín, Valdefuentes.
  * *Medium-high cost investment*: Jerónimos, Fuentela reina.
  * *High cost investment*: Recoletos.

{{< figure src="/project3/exhibit_1.png" title="Exhibit 1: ." >}}


{{< figure src="/project3/exhibit_2.png" title="Exhibit 2: ." >}}


{{< figure src="/project3/exhibit_3.png" title="Exhibit 3: ." >}}


{{< figure src="/project3/exhibit_4.png" title="Exhibit 4: ." >}}


{{< figure src="/project3/exhibit_5.png" title="Exhibit 5: ." >}}


{{< figure src="/project3/exhibit_6.png" title="Exhibit 6: ." >}}


{{< figure src="/project3/exhibit_7.png" title="Exhibit 7: ." >}}


{{< figure src="/project3/exhibit_8.png" title="Exhibit 8: ." >}}


{{< figure src="/project3/exhibit_9.png" title="Exhibit 9: ." >}}