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



 

Insight 1: Conversion rates are very poor.
      60% from views to cart additions.
      22% from cart additions to purchases.
      13% from views to purchases.

Insight 2: Average session numbers are low
      2.2 products are viewed.
      1.3 products are added to the cart.
      0.9 products are removed from the cart.
      0.3 products are purchased.
      Media facturación mensual: 125000€

Insight 3: Las horas en las que la gente compra más son la 1, las 8, de 11 a 13 y las 18.
      info es muy relevante por ejemplo de cara a paid ads, tanto de generación de tráfico como de retargeting
      Parece haber algún subtipo de usuario que compra a la 1 de la mañana, que aunque no sea muy frecuente sí compra mucho

Insight 4: Tendencia semanal muestra un pico el día 22, posiblemente por el inicio de la semana black friday
      días de Navidad tienen una tendencia decreciente, lo que significa que los consumidores claramente han adelantado sus compras

Insight 5: La mayoría de los clientes solo realiza una compra y se gasta menos de 50€ de media.
      La compra mediana contiene 5 productos. Gran recorrido para mejorar este ratio con sistemas de recomendación.

Insight 6: El 90% de que los nuevos clientes no vuelve a comprar en los meses posteriores.
      Analisis de cohortes

Insight 7: El LTV medio es de 42€.
      Aplicando nuestro margen sobre esa cifra y el % que queremos dedicar a captación nos sale el importe máximo a invertir en CPA.
      Aplicar las acciones de CRO permitirá incrementar el LTV y por tanto también el CPA, siendo una ventaja estratégica muy importante.

Insight 8: Mediante el análisis RFM, podemos identificar los clientes que con mayor probabilidad responderán mejor a nuevas campañas

Insight 9: Casi la mitad de los productos no han tenido ninguna venta en los 5 meses del histórico.
      Eliminarlos del catálogo
      Investigar por qué no están funcionando

Insight 10: sistema de recomendación adaptado a las visualizaciones del usuario
















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


{{< figure src="/project3/exhibit_4_1.png" title="Exhibit 4.1: ." >}}


{{< figure src="/project3/exhibit_4_2.png" title="Exhibit 4.2: ." >}}


{{< figure src="/project3/exhibit_5.png" title="Exhibit 5: ." >}}


{{< figure src="/project3/exhibit_6.png" title="Exhibit 6: ." >}}


{{< figure src="/project3/exhibit_7.png" title="Exhibit 7: ." >}}


{{< figure src="/project3/exhibit_8.png" title="Exhibit 8: ." >}}


{{< figure src="/project3/exhibit_9.png" title="Exhibit 9: ." >}}


{{< figure src="/project3/exhibit_10_1.png" title="Exhibit 10.1: ." >}}


{{< figure src="/project3/exhibit_10_2.png" title="Exhibit 10.2: ." >}}