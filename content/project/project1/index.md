---
title: Real Estate Market's Analysis for rental vacation
summary: The available public AirBnb data is analysed to find insights that can help to understand the characteristics of the vacation rental market in Madrid (Spain) and guide the team’s research work in terms of rental prices, occupancy levels and purchase prices.
tags: 
  - Discovery Projects
date: 2024-06-01
#external_link: http://github.com
---

*Note: Documentation available on the [GitHub Repository](https://github.com/pabloelt/real-estate-market-analysis-rental-vacation) is currently in Spanish. It will be soon updated to English.*
{style="color: #aaaaaa"}

{{< toc >}}

## 1. Introduction
{style="color: #BBDEFC"}

The client for this project is a real estate company that invests in large cities by purchasing properties to rent out as vacation apartments. The managers have decided to invest in Madrid and are interested in analyzing publicly available data from the sector leader, Airbnb, to identify the types of properties with the greatest commercial potential for vacation rentals.

As the main deliverable, the management expects to receive a detailed typology of properties that the valuation team should target among the existing opportunities in the city, as well as the primary neighborhoods or geographic areas to focus on.

Notes:

* This article presents a technical explanation of the development process followed in the project.
* Source code can be found [here](https://github.com/pabloelt/real-estate-market-analysis-rental-vacation).

---

## 2. Objectives
{style="color: #BBDEFC"}

The main objective is to identify the property profiles with the highest potential in the vacation rental market. This can guide the valuation team on where to start looking for such opportunities and highlight the key neighborhoods and geographical areas, which are most promising to focus on.

This analysis is primarily conducted in terms of rental prices, occupancy levels, and purchase prices.

---

## 3. Project Design
{style="color: #BBDEFC"}

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

* <text style='color: #BBDEFC; font-weight: normal;'>Rental price:</text> It is calculated as the price paid per night in euros based on the data registered by Airbnb.
* <text style='color: #BBDEFC; font-weight: normal;'>Occupancy rate:</text> It is calculated as the number of days per year that the property is rented in percentage.
* <text style='color: #BBDEFC; font-weight: normal;'>Property purchase price:</text> It is calculated by multiplying the number of square meters by the average price per square meter in the area where the property is located. Additionally, we apply a 25% discount to the official price, assuming that our purchasing team can negotiate that.

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

{{< figure src="/project1/exhibit_1.png" title="Exhibit 1: Relation between rental and purchase price for each neighborhood." >}}

<text style='color: #BBDEFC; font-weight: normal;'>It is recommended to search for two-bedroom properties that can accommodate 4 guests</text>

* The number of guests that maximize the rental price while minimizing the property's purchase price is 4.

{{< figure src="/project1/exhibit_2.png" title="Exhibit 2: Optimal number of guests based on the rental and purchase price." >}}

<text style='color: #BBDEFC; font-weight: normal;'>It is recommended to search for properties in one of the identified neighborhoods that are not necessarily close to points of interest</text>

* These properties are expected to have a lower purchase price.
* It seems that proximity to points of interest does not have a particular impact on rental prices.

{{< figure src="/project1/exhibit_3.png" title="Exhibit 3: Relation between the purchase price and the distance to the PoI (Puerta del Sol)." >}}

<text style='color: #BBDEFC; font-weight: normal;'>A new business model based on rentals for specific moments of high sporting interest should be explored</text>

* It is advisable to look for opportunities in the San Blas neighborhood.
* These properties present a particularly high cost-income ratio per night.

{{< figure src="/project1/exhibit_4.png" title="Exhibit 4: Relation between rental and purchase price for each district." >}}

* There are still many rentals that are not exploiting this potential.

{{< figure src="/project1/exhibit_5.png" title="Exhibit 5: Rental price map in San Blas neighborhood. Red dots indicate properties with high rental prices." >}}