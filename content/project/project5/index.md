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

Nowadays, there are basically two main methodologies that a company can apply in order to get a final client. These are outbound and inbound marketing models. Outbound marketing is known for using traditional methods to reach potential buyers, such as advertisements, events, product samples, and phone calls. In contrast, inbound marketing focuses on attracting consumers to the company, encouraging them to seek out more information about a product or service on their own.

Outbound strategies are often seen as more aggressive, requiring consistent and repeated efforts from sellers. In inbound marketing, however, sellers typically engage only after the customer has made the first move.

Inbound marketing guarantees that when executed properly, the company will reach a more targeted audience with higher buying potential. As a result, investing in inbound marketing is more economical, often yielding a higher return on investment.

{{< figure src="/project5/inbound_model.png" title="Inbound marketing strategy." >}}

One of the challenges associated with inbound marketing is that the number of generated leads exceeds the capacity of the sales channels, leading to several issues:

* Conflicts between marketing and sales departments: The marketing department expects a higher conversion rate from the large pool of leads, while the sales department is frustrated by the low quality of these leads, feeling they are wasting valuable time.
* Saturation of the sales channels: The sales team can only handle a limited number of leads effectively.
* Low conversion rate: As a result, the company's performance is significantly below potential, which could be improved with proper lead management based on Machine Learning optimization.

For all the reasons mentioned above, it is essential to implement some form of lead prioritization to achieve higher conversion rates. The assets we are developing for the company—specifically the predictive lead scoring and customer segmentation algorithms—are designed to address this need. These tools will enable the company to identify the highest-quality leads and recognize key customer segments, thereby refining their approach strategy for each group.

---

## 4. Project Design
{style="color: #BBDEFC"}

### 4.1 Methodology
{style="color: #BBDEFC; font-weight: normal"}

The project has been designed with a multi-step methodology, which is summarized in the figure bellow.

{{< figure src="/project5/methodology.png" title="Project methodology." >}}

The process for this project consists of two main stages: the development phase and the production phase.

The development phase begins with the set up and data importation, followed by a thorough data quality review. Next, an exploratory data analysis is conducted to uncover key insights. The variable transformation step involves selecting the most relevant variables that impact the problem and applying the necessary transformations. Following this, models are implemented for both the predictive and segmentation algorithms. During the evaluation process, all metrics are thoroughly tested.

In the production phase, the models are prepared for deployment, ensuring that the code is optimized for production. Additionally, a retraining script is created during this stage to facilitate future updates.

### 4.2 Levers
{style="color: #BBDEFC; font-weight: normal"}

The main levers for this project are summarized below:

* <text style='color: #BBDEFC; font-weight: normal;'>Leads:</text> Understanding general information about the leads the company receives is crucial for optimizing future marketing campaigns.
* <text style='color: #BBDEFC; font-weight: normal;'>Conversion rate:</text> This metric indicates the ratio at which leads convert into customers. Our goal is to maximize this metric to boost the company’s profits.
* <text style='color: #BBDEFC; font-weight: normal;'>Commercial channels optimization:</text> The sales department has various channels for communicating with leads, including phone calls, SMS, emails, web chat, and a subcontracted lead management company. Optimizing these channels is key to improving overall efficiency.


### 4.3 KPIs
{style="color: #BBDEFC; font-weight: normal"}

The KPIs that results from the above-mentioned levers are the following:

* <text style='color: #BBDEFC; font-weight: normal;'>Lead-to-customer conversion rate (CR):</text> Ratio at which leads convert into customers. It is defined as:
{{< math >}}
$$
CR[\%] = \frac{N_C}{N_L}\cdot 100,
$$
{{< /math >}}
where {{< math >}}$N_C${{< /math >}} and {{< math >}}$N_L${{< /math >}} are de number of final customers and leads, respectively.
* <text style='color: #BBDEFC; font-weight: normal;'>Sales department workload:</text> Number of potential customers to be managed by the sales team.
* <text style='color: #BBDEFC; font-weight: normal;'>Lost investment in unconverted lead management:</text> Cost of commercial efforts directed toward potential customers who ultimately do not purchase the company’s product.
* <text style='color: #BBDEFC; font-weight: normal;'>Sales profit (SP):</text> Net profit obtained from the sales of the online course. It is defined as:
{{< math >}}
$$
SP[$] = \left( Price_{prod} - Cost_{leads \ conv} \right) \cdot N_C - Cost_{leads \ not \ conv},
$$
{{< /math >}}
where {{< math >}}$Price_{prod}${{< /math >}} is the price of the online course, {{< math >}}$Cost_{leads \ conv}${{< /math >}} is the cost per lead arising from commercial and marketing actions, and {{< math >}}$Cost_{leads \ not \ conv}${{< /math >}} is the lost investment in unconverted lead management.

### 4.4 Entities and Data
{style="color: #BBDEFC; font-weight: normal"}

The most relevant entities from which we can obtain data are summarized below:

* <text style='color: #BBDEFC; font-weight: normal;'>Leads:</text> Leads historical data is provided by the client in a *.csv* file, which contains information about 37 different features for 9240 different leads.
* <text style='color: #BBDEFC; font-weight: normal;'>Product:</text> The product that the company is trying to sell is a high-value online course design to train proffesionals in the data science sector. Its price is 49.99$.
* <text style='color: #BBDEFC; font-weight: normal;'>Commercial channels:</text> The main commercial channels are phone calls, sms, emails, web chat, ad campaings, and a subcontracted lead management company. The lead management average cost is estimated at 3.50$ per lead.

---

## 5. Data Quality
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

## 6. Exploratory Data Analysis
{style="color: #BBDEFC"}

The aim of this phase of the project is to identify trends and patterns that can be transformed into insights, providing valuable information for our project. To achieve this, we perform various statistical evaluations and create graphical representations.

In order to guide this process, a series of seed questions are proposed to serve as a basis for the analysis.

### 6.1 Seed questions
{style="color: #BBDEFC; font-weight: normal"}

**Regarding Leads:**

* <text style='color: #BBDEFC; font-weight: normal;'>Q1:</text> What are the main demographic profiles in the company’s lead database?

**Regarding Conversion Rate:**

* <text style='color: #BBDEFC; font-weight: normal;'>Q2:</text> What is the current lead-to-customer conversion rate?
* <text style='color: #BBDEFC; font-weight: normal;'>Q3:</text> What factors have the most significant impact on lead-to-customer conversion?

**Regarding Commercial and Marketing Channels:**

* <text style='color: #BBDEFC; font-weight: normal;'>Q4:</text> How are the company’s commercial and marketing channels performing?
* <text style='color: #BBDEFC; font-weight: normal;'>Q5:</text> From which sources is the company attracting potential customers? Which sources are the most promising?
* <text style='color: #BBDEFC; font-weight: normal;'>Q6:</text> Which demographic profile should be the primary focus of marketing efforts?
* <text style='color: #BBDEFC; font-weight: normal;'>Q7:</text> What percentage of leads are open to receiving communications via email or phone calls?
* <text style='color: #BBDEFC; font-weight: normal;'>Q8:</text> How effective have the company’s advertising campaigns been?
* <text style='color: #BBDEFC; font-weight: normal;'>Q9:</text> How well is the current lead magnet performing?

### 6.2 Some results obtained through the EDA
{style="color: #BBDEFC; font-weight: normal"}

These are some of the results that we have obtained by performing the exploratory Data Analysis (EDA) for both categorical and numerical variables that are present in the dataset.

{{< figure src="/project5/exhibit_1.png" title="Exhibit 1. Exploratory Data Analysis: Occupation, lead source and last activity." >}}

{{< figure src="/project5/exhibit_2.png" title="Exhibit 2. Exploratory Data Analysis: Numerical variables." >}}

 A more detailed analysis of this stage can be found [here](https://github.com/pabloelt/analysis-and-optimization-of-an-ecommerce-company/blob/main/Notebooks/03_Analisis%20e%20Insights.ipynb).

### 6.3 Insights
{style="color: #BBDEFC; font-weight: normal"}

Once the exploratory data analysis has been conducted, the following insights have been obtained:

**Leads:**

* <text style='color: #BBDEFC; font-weight: normal;'>Insight 1:</text> The mayority of the potential customers that are interested in the company are unemployed, particularly 88.84% of the leads.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 2:</text> Only 8.64% of the leads are working professionals.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 3:</text> The number of leads coming that comes from students is very low. It only represents 2.05% of the leads.

**Lead-to-customer conversion rate:**

* <text style='color: #BBDEFC; font-weight: normal;'>Insight 4:</text> The current conversion rate of the company is 41.56%.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 5:</text> Working professionals presents the highest conversion rate of 90.74%.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 6:</text> Unemployed leads, which are the largest group, have a low conversion rate of 36.52%.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 7:</text> Almost all leads that comes from the source *Reference* are converted into customers (89.19% conversion rate) . However, only 4.56% of leads come from this source.

**Commercial and marketing channels:**

* <text style='color: #BBDEFC; font-weight: normal;'>Insight 8:</text> It is observed that 99.98% and 91.07% of the leads do not want to receive phone calls nor emails, respectively. Therefore, the mayority of people that visit the website are not interested in the product.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 9:</text> Email marketing campaigns have untapped potential, since last activity of 41.33% of total number of leads was opening an email but only 36.15% of them were finally converted. Only 14.9% of leads who want to be contacted by email end up converting into paying customers.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 10:</text> SMS campaigns have proven to be highly effective, boasting a conversion rate of 60.82%.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 11:</text> Most potential customers were not interested in receiving a free copy of the lead magnet. Those who did show interest are primarily unemployed and downloaded it mainly from the landing page.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 12:</text> Converted leads spend a median of 16 minutes on the website and visit an average of 2.5 pages per session. In contrast, non-converted leads spend a median of only 6 minutes on the site. 

### 6.4 Recommended actions
{style="color: #BBDEFC; font-weight: normal"}


---

## 7. Variable transformation
{style="color: #BBDEFC"}

---

## 8. Lead segmentation model
{style="color: #BBDEFC"}

---

## 9. Lead scoring model
{style="color: #BBDEFC"}

---

## 10. Evaluation and production of the models
{style="color: #BBDEFC"}

---
## 11. Business case implementation
{style="color: #BBDEFC"}


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