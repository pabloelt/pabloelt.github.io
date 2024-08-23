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
SP[$] = \left( Price_{prod} \cdot CR - Cost_{leads} \right) \cdot N_L,
$$
{{< /math >}}
where {{< math >}}$Price_{prod}${{< /math >}} is the price of the online course, and {{< math >}}$Cost_{leads}${{< /math >}} is the cost per lead arising from commercial and marketing actions.

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
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 7:</text> Almost all leads that comes from the source *Reference* are converted into customers (89.19% conversion rate). However, only 4.56% of leads come from this source.

**Commercial and marketing channels:**

* <text style='color: #BBDEFC; font-weight: normal;'>Insight 8:</text> It is observed that 99.98% and 91.07% of the leads do not want to receive phone calls nor emails, respectively. Therefore, the mayority of people that visit the website are not interested in the product.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 9:</text> Email marketing campaigns have untapped potential, since last activity of 41.33% of total number of leads was opening an email but only 36.15% of them were finally converted. Only 14.9% of leads who want to be contacted by email end up converting into paying customers.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 10:</text> SMS campaigns have proven to be highly effective, boasting a conversion rate of 60.82%.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 11:</text> Most potential customers were not interested in receiving a free copy of the lead magnet. Those who did show interest are primarily unemployed and downloaded it mainly from the landing page.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 12:</text> Converted leads spend a median of 16 minutes on the website and visit an average of 2.5 pages per session. In contrast, non-converted leads spend a median of only 6 minutes on the site. 

### 6.4 Recommended actions
{style="color: #BBDEFC; font-weight: normal"}

<text style='color: #BBDEFC; font-weight: normal;'>Actions to improve leads' management:</text>

1. Enhance the quality of survey or form questions to gather more user inputs and reduce the occurrence of NaN or default (‘Select’) values.
2. Collect timestamps for website visits to enable seasonality analysis and implement cookies to track and identify users as they navigate different pages on the website.
3. Develop a new <text style='color: #BBDEFC; font-weight: normal;'>_lead segmentation algorithm_</text> that categorizes the company's diverse lead profiles, enabling the identification of the best-fitting group for each new lead. This will allow for more personalized commercial actions.


<text style='color: #BBDEFC; font-weight: normal;'>Actions to improve lead-to-customer conversion rate:</text>

1. Implement a <text style='color: #BBDEFC; font-weight: normal;'>_predictive lead scoring algorithm_</text> that identifies individuals most likely to convert into paying customers. This will reduce the sales team's workload allowing them to focus more time on engaging with the most promising leads.


<text style='color: #BBDEFC; font-weight: normal;'>Actions to improve commercial and marketing channels performance:</text>

1. Enhance the content strategy across the website, lead magnet, and emails to attract more traffic and increase user engagement. Focus on creating tailored content specifically for working professionals interested in the data science sector.
2. Develop a referral program to motivate existing customers to recommend the course to their friends, family, and colleagues.
3. Allocate more resources to acquiring leads through ‘Reference’ channel, as they demonstrate the highest conversion rate.
4. Boost investments in SMS campaigns, given their strong performance.

---

## 7. Variable transformation
{style="color: #BBDEFC"}

At this stage of the project, various variable transformation techniques are applied to ensure they meet the requirements of the algorithms used in the modeling phase.

As outlined during the exploratory data analysis, two distinct models will be developed:

1. A <text style='color: #BBDEFC; font-weight: normal;'>lead segmentation model</text> to assist sales and marketing teams in identifying different lead profiles within the company.
2. A <text style='color: #BBDEFC; font-weight: normal;'>predictive lead scoring model</text> to pinpoint individuals most likely to convert into paying customers.

In both models, categorical variables must be transformed into numerical ones. Since the categorical cariables in the dataset are all nominal, the one-hot encoding technique is employed for this purpose.

For the lead segmentation model, an unsupervised machine learning algorithm is recommended, specifically the KMeans algorithm. This clustering-based algorithm is highly sensitive to the scales of different features because it relies on distance calculations. Therefore, rescaling techniques must be applied to ensure that all features are on the same scale. Given the decision to apply one-hot encoding to categorical variables, the most appropriate rescaling technique in this case is min-max scaling, which will transform feature values to a scale between 0 and 1.

For the predictive lead scoring model, a supervised machine learning algorithm is recommended. Among the various classification algorithms available, the most promising candidates are logistic regression, random forest, XGBoost, and LightGBM. We will analyze these options in more detail later.

Additionally, we need to decide whether to apply feature discretization or binarization. Considering that the project's primary focus is on prediction accuracy rather than interpretability, and given that one of the models is based on a segmentation algorithm, neither discretization nor binarization will be applied.

Lastly, it is important to note that class balancing processes are not necessary for this project, as the dataset contains a sufficiently significant representation of both classes (converted=1, converted=0).

---

## 8. Lead segmentation model
{style="color: #BBDEFC"}

At this stage, after completing data quality checks, exploratory data analysis, and variable transformation, we are ready to develop the lead segmentation model. As mentioned earlier, an unsupervised machine learning model will be used for this purpose, specifically the KMeans algorithm, which has demonstrated strong performance in the clustering process. By implementing this model, we aim to uncover new insights that can enhance the company's sales and marketing strategies.

### 8.1 Selecting the number of segments
{style="color: #BBDEFC; font-weight: normal"}

In order to identify the optimal number of clusters in the KMeans algorithm, we apply 4 different methods. The result are shown in the figure below.

{{< figure src="/project5/exhibit_3.png" title="Exhibit 3. Main methods for identifying the optimal number of clusters in KMeans algorithm." >}}

* **Elbow Method:** This method typically identifies the optimal number of clusters by selecting the point where the curve bends or "elbows," indicating diminishing returns in reducing within-cluster variance. However, in this case, the chart shows only a linear decrease, offering little useful guidance for cluster selection.

* **Silhouette Method:** This metric measures how similar each point is to its own cluster compared to other clusters. Values closer to 1 indicate better-defined clusters. Here, a segmentation of 4 to 5 clusters appears optimal based on this method.

* **Calinski-Harabasz Index:** This index evaluates cluster separation, with higher values indicating better-defined clusters. According to this method, a segmentation into 3 or 4 clusters is likely the best.

* **Davies-Bouldin Index:** This index assesses the average similarity ratio of each cluster to its most similar cluster, with lower values indicating better clustering. For this analysis, a segmentation of 4 clusters is preferred based on this index.

It is important to note that an iterative process was applied before arriving at the final charts. The procedure involved the following steps:

1. Initially, charts for the four methods mentioned above were generated. Based on this data, a fixed number of clusters was selected.
2. The KMeans algorithm was then applied with this fixed segmentation, and the values for each variable were analyzed.
3. Typically, initial segmentations revealed some inconsistencies, leading to the elimination of certain variables and testing different cluster configurations.
4. Steps 1 through 3 were repeated several times until a final, consistent cluster segmentation was achieved.

After completing this process, it was determined that a 4-cluster segmentation provided the most meaningful business insights.

### 8.2 Segment profiling
{style="color: #BBDEFC; font-weight: normal"}

Once the optimal number of clusters and the most relevant segmentation variables have been selected, the model is trained and executed, assigning each lead to one of the four existing clusters.

To understand the business implications, average values for each variable used in the model has been calculated, allowing us to identify the most distinguishing characteristics of each segment. This is shown in the table below.

{{< figure src="/project5/exhibit_4.png" title="Exhibit 4. Unsupervised ML modelling: Cluster results from KMeans algorithm." >}}

### 8.3 Segment analysis
{style="color: #BBDEFC; font-weight: normal"}

After analysing the above results, the most differential characteristics for each segment are identified and presented.

<text style='color: #BBDEFC; font-weight: normal;'>Segment 0: Super High-quality Leads</text>

* Origin: Lead Add Form.
* Last activity: Non categorize.
* Occupancy: Working Professionals.
* Largest time spent on the website.
* Great conversion rate. Nine out of ten leads in this segment end up buying the company's product.

<text style='color: #BBDEFC; font-weight: normal;'>Segment 1: Very low-quality Leads</text>

* Origin: Landing Page Submission.
* Last activity: Email opened.
* Occupancy: Students and unemployed.
* Very low time spent on the website.
* Worst conversion rate group.

<text style='color: #BBDEFC; font-weight: normal;'>Segment 2: Medium-quality Leads</text>

* Origin: Landing Page Submission.
* Last activity: SMS sent.
* Occupancy: Unemployed.
* They spent some time on the website.
* Moderate conversion rate.

<text style='color: #BBDEFC; font-weight: normal;'>Segment 3: Low-quality Leads</text>

* Origin: API.
* Last activity: Chat conversation.
* Occupancy: Unemployed.
* Very low time spent on the website.
* Low conversion rate.

### 8.4 Segmentation insights
{style="color: #BBDEFC; font-weight: normal"}



---

## 9. Lead scoring model
{style="color: #BBDEFC"}

---

## 10. Evaluation and production of the models
{style="color: #BBDEFC"}

---
## 11. Business case implementation
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