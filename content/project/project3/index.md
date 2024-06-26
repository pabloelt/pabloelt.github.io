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

* **RFM Segmentation:** Analyzing customer data based on Recency, Frequency, and Monetary value to identify key customer segments and tailor marketing strategies accordingly.
* **Recommendation System:** Developing a recommendation system to personalize the shopping experience, encouraging higher conversions and increasing the average ticket size.

These tools will help us implement effective CRO actions and drive substantial revenue growth.

---

## 3. Project Design
{style="color: #BBDEFC"}

To establish the levers, a brief explanation about the customer journey is requiered.

The first step is when a user visits the ecommerce website. Typically, they will come from:

* Paid campaigns: Paid ads such as Facebook Ads or Google Ads.
* Organic content: Blog, social media, etc.
* Direct traffic: Knows the URL and enters it directly into the browser.

The second step occurs when the user browses the website and adds a product to the cart.

* They can remove products from the cart, exit without making a purchase, or ultimately place an order.
* A common process is cross-selling, where other products that might interest the user are recommended.

The third step involves customer re-engagement through retargeting or email marketing.

{{< figure src="/project3/customerjourney.png" title="" >}}

Other key metrics for managing this type of business include:

* CPA (Cost Per Acquisition): Aggregate cost of acquiring a customer through a marketing campaign.
* AOV (Average Order Value): Average value of customer shopping carts, providing insight into the average amount users spend on the ecommerce site.
* Purchase frequency: Number of times a user makes a purchase on the ecommerce site.
* LTV (Lifetime Value): Predicts the average profit from a customer throughout their entire lifetime as a buyer on the ecommerce site.
* Churn rate: Metric indicating the number of customers who no longer purchase services from the ecommerce site.











This project has been designed by taking into consideration the following levers, KPIs, and entities from which data have been obtained.

### 3.1 Levers
{style="color: #BBDEFC; font-weight: normal"}

The levers for this project are clear and are summarized below:

* <text style='color: #BBDEFC; font-weight: normal;'>Rental price:</text> The higher the rental price per night, the greater the profitability.
* <text style='color: #BBDEFC; font-weight: normal;'>Occupancy rate:</text> The more days per year a property can be rented, the greater the profitability.
* <text style='color: #BBDEFC; font-weight: normal;'>Purchase price:</text> The cheaper the property can be acquired, the greater the profitability.

### 3.2 KPIs
{style="color: #BBDEFC; font-weight: normal"}

The KPIs that results from the above-mentioned levers are the following:

* <text style='color: #BBDEFC; font-weight: normal;'>KPI 1:</text> We calculate the rental price as the price paid per night in euros based on the data registered by Airbnb
* <text style='color: #BBDEFC; font-weight: normal;'>KPI 2:</text> We calculate the occupancy rate as the number of days per year that the property is rented in percentage.
* <text style='color: #BBDEFC; font-weight: normal;'>KPI 3:</text> We calculate the purchase price of a property by multiplying the number of square meters by the average price per square meter in the area where the property is located. Additionally, we apply a 25% discount to the official price, assuming that our purchasing team can negotiate that.

### 3.3 Entities and Data
{style="color: #BBDEFC; font-weight: normal"}

The real data used in this project is collected from [Airbnb](https://insideairbnb.com/get-the-data/) and [Idealista](https://www.idealista.com/sala-de-prensa/informes-precio-vivienda/) platforms. The most relevant entities from which we can obtain data are summarized below:

* <text style='color: #BBDEFC; font-weight: normal;'>Properties:</text> Location, rental price, room type, reviews, minimun/maximum nights, number of bedrooms, beds, …
* <text style='color: #BBDEFC; font-weight: normal;'>Hosts:</text> Name, id, url, location, verifications, …
* <text style='color: #BBDEFC; font-weight: normal;'>Locations:</text> Neighborhood, district, latitude, longitude, …

---

## 4. Data Quality
{style="color: #BBDEFC"}

In this stage of the project, general data quality correction processes have been applied, such as:

* Data renaming.
* Type correction.
* Proper selection of the most relevant data for the project.
* Analysis of nulls and duplicated registers.
* Analysis of numerical and categorical variables.
* Imputation of nulls through a crosstab analysis.
* Discretization of variables.
* Creation of new variables: square meters estimation, purchase price estimation, ...

The entire process can be consulted in detail [here](https://github.com/pabloelt/real-estate-market-analysis-rental-vacation/blob/main/Notebooks/03_Creacion%20del%20datamart%20analitico.ipynb).

---

## 5. Exploratory Data Analysis
{style="color: #BBDEFC"}

The aim of this phase of the project is to identify trends and patterns that can be transformed into insights, providing valuable information for our project. To achieve this, we perform various statistical evaluations and create graphical representations.

In order to guide this process, a series of seed questions are proposed to serve as a basis for the analysis.

### 5.1 Seed questions
{style="color: #BBDEFC; font-weight: normal"}

**Regarding rental price:**

* <text style='color: #BBDEFC; font-weight: normal;'>Q1:</text> What is the average price and price range, by districts and neighborhoods?
* <text style='color: #BBDEFC; font-weight: normal;'>Q2:</text> What is the ranking of districts and neighborhoods by average rental price?
* <text style='color: #BBDEFC; font-weight: normal;'>Q3:</text> What factors (other than location) determine the rental price?
* <text style='color: #BBDEFC; font-weight: normal;'>Q4:</text> What is the relationship between the size of the property and the price at which it can be rented?
* <text style='color: #BBDEFC; font-weight: normal;'>Q5:</text> How does competition (number of available properties per neighborhood) influence the rental price?
* <text style='color: #BBDEFC; font-weight: normal;'>Q6:</text> How do prices vary by type of rental (whole apartment, private room, shared room)?

**Regarding occupancy rate:**

* <text style='color: #BBDEFC; font-weight: normal;'>Q7:</text> What is the average occupancy rate by district and by neighborhood?
* <text style='color: #BBDEFC; font-weight: normal;'>Q8:</text> How likely is the occupancy rate in each district?
* <text style='color: #BBDEFC; font-weight: normal;'>Q9:</text> What is the ranking of districts and neighborhoods by occupancy rate?
* <text style='color: #BBDEFC; font-weight: normal;'>Q10:</text> What factors (other than location) determine occupancy rate?
* <text style='color: #BBDEFC; font-weight: normal;'>Q11:</text> What is the relationship between property size and occupancy rate?
* <text style='color: #BBDEFC; font-weight: normal;'>Q12:</text> How does competition (number of properties available per district) influence occupancy rate?

**Regarding purchase price:**

* <text style='color: #BBDEFC; font-weight: normal;'>Q13:</text> What is the ranking of price per m2 by district?
* <text style='color: #BBDEFC; font-weight: normal;'>Q14:</text> What is the ranking of property price (m2 * average size) by district?
* <text style='color: #BBDEFC; font-weight: normal;'>Q15:</text> What is the relationship between property price and rental price by district?
* <text style='color: #BBDEFC; font-weight: normal;'>Q17:</text> What is the relationship between property price and occupancy by district?

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