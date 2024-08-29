---
title: Forecasting for a Retail Company 
summary: A forecasting model is developed to reduce warehouse costs and stock-outs by using a scalable set of recursive machine learning algorithms. This model predicts demand for the next 8 days at a store-product level, based on the historical data provided by the company.
tags:
  - Machine Learning
date: 2024-08-02
#external_link: http://github.com
---
*Note: Documentation available on the [GitHub Repository](https://github.com/pabloelt/lead-scoring-analysis-and-segmentation) is currently in Spanish. It will be soon updated to English.*
{style="color: #aaaaaa"}

{{< toc >}}

## 1. Introduction
{style="color: #BBDEFC"}

The client for this project is a large retailer based in the United States. The company has identified issues in its warehouse operations, leading to losses and stock-outs for several products. The objective is to implement a forecasting model using artificial intelligence algorithms to predict the appropriate stock levels for at least the next 8 days. This initiative aims to enhance operational efficiency and increase the company's profitability.

Notes:

* This article presents a technical explanation of the development process followed in the project.
* Source code can be found [here](https://github.com/pabloelt/lead-scoring-analysis-and-segmentation).

---

## 2. Objectives
{style="color: #BBDEFC"}

The primary objective is to develop a forecasting model utilizing a set of machine learning algorithms to predict sales for the next 8 days at the store-product level. These algorithms are trained using the extensive three-year history available in the retail company's SQL database, employing massive modeling techniques to ensure accuracy and reliability.

{{< figure src="/project6/system.png" title="Three-steps approach employed to developed the forecasting model." >}}

---

## 3. Understanding of the problem
{style="color: #BBDEFC"}

Forecasting is one of the most widely used techniques in the data science field due to its significant impact on a company's balance sheet and its potential to greatly enhance overall performance. Some of the mayor beneficts are summarized below:

* <text style='color: #BBDEFC; font-weight: normal;'>Inventory optimization:</text> Forecasting helps predict demand more accurately, reducing overstock and stock-outs. This leads to better inventory management, minimizing costs and improving cash flow.

* <text style='color: #BBDEFC; font-weight: normal;'>Improved customer satisfaction:</text> By anticipating demand, the company can ensure products are available when customers want them, enhancing the shopping experience and increasing customer loyalty.

* <text style='color: #BBDEFC; font-weight: normal;'>Better decision-making:</text> Forecasting provides data-driven insights, enabling more informed decisions about pricing, promotions, and product launches, ultimately improving profitability.

* <text style='color: #BBDEFC; font-weight: normal;'>Resource allocation:</text> Forecasting helps in planning staffing, logistics, and marketing efforts, ensuring resources are allocated effectively to meet anticipated demand.

* <text style='color: #BBDEFC; font-weight: normal;'>Competitive advantage:</text> Companies with better forecasting capabilities can respond more quickly to market changes, offering them an edge over competitors.

In this context, traditional sales forecasting methods have been reliable for decades. However, with the advent of machine learning algorithms, it is now possible to implement powerful forecasting models using a data science approach. These modern techniques enable the prediction of product or service demand over a specified future period by leveraging historical company data. Compared to traditional forecasting methods, a machine learning approach offers several advantages:

* Accelerated data processing speed
* Automated forecast updates based on recent data
* Enhanced data analysis capabilities
* Identification of hidden patterns in data
* Greater adaptability to changes

For this project, an innovative forecasting model has been developed, utilizing massive and scalable machine learning techniques.

---

## 4. Project Design
{style="color: #BBDEFC"}

### 4.1 Methodology
{style="color: #BBDEFC; font-weight: normal"}

The project has been designed with a multi-step methodology, which is summarized in the figure bellow.

{{< figure src="/project5/methodology.png" title="Project methodology." >}}

The process for this project consists of two main stages: the development phase and the production phase.

The development phase begins with the set up and data importation, followed by a thorough data quality review. Next, an exploratory data analysis is conducted to uncover key insights. The variable transformation step involves selecting the most relevant variables that impact the problem and applying the necessary transformations. Following this, the forecasting model is implemented based on machine learning algorithms. During the evaluation process, all metrics are thoroughly tested.

In the production phase, the model is prepared for deployment, ensuring that the code is optimized for production. Additionally, a retraining script is created during this stage to facilitate future updates.

### 4.2 Project scope, entities, and data
{style="color: #BBDEFC; font-weight: normal"}

This project is developed using data from a three-year SQL database of a large American retailer. However, due to the computational constraints of the available equipment, the project's scope is limited to forecasting sales for ten products that belong to a sigle category (food) in two different stores. Nevertheless, the system is fully scalable and can be extended to predict sales for additional products, categories, and stores by simply adjusting the relevant parameters.

{{< figure src="/project6/scheme.png" title="Basis scheme of the retail company's performance." >}}

The most relevant entities from which we can obtain data are summarized below:

* <text style='color: #BBDEFC; font-weight: normal;'>Store id:</text> It shows the identification number associated with the store at which the product are sold.
* <text style='color: #BBDEFC; font-weight: normal;'>Item id:</text> Identification number for each of the items that the company offers.
* <text style='color: #BBDEFC; font-weight: normal;'>Operation day:</text> Code for the day when a certain product is sold.
* <text style='color: #BBDEFC; font-weight: normal;'>Number of sales:</text> The quantity of items sold each day for each store, as recorded in the dataset.
* <text style='color: #BBDEFC; font-weight: normal;'>Sell price:</text> Price at which the items are sold.

Before conducting any analysis or data transformation, it is crucial to set aside a portion of the dataset for validation purposes. This reserved data will be used to validate the models after they have been trained and tested on the remaining data. Since this is a forecasting project, the reserved data must be in chronological order (time series) to accurately test the model's performance. Therefore, the data from the last month, December 2015, has been extracted and will be used as a validation later.


### 4.3 Forecasting-related problems approach
{style="color: #BBDEFC; font-weight: normal"}

<text style='color: #BBDEFC; font-weight: normal;'>Hierarchical Forecasting:</text>

In forecasting models, it is common to encounter time series data that follows a hierarchical aggregation structure. In the retail market, for instance, sales data for a Stock Keeping Unit (SKU) at a store often rolls up into various category and subcategory hierarchies. In such cases, it's essential to ensure that the sales forecasts are consistent when aggregated to higher levels. To achieve this, a hierarchical forecasting approach is employed, which generates coherent forecasts (or reconciles incoherent ones). This approach allows individual time series to be forecasted independently while maintaining the relationships within the hierarchy.

{{< figure src="/project6/hierarchical_structure.png" title="Hierarchical structure of the project." >}}

The major problems when generating a forecasting model are the following:

* There are different levels of hierarchies in the commercial catalog.
* It may be interesting to predict sales at different levels.
* Since the forecasts are probabilistic, predictions at different levels will not match exactly.

A hierarchy forecasting approach offers different methods to solve these problems. The most common ones include:

* <text style='color: #BBDEFC; font-weight: normal;'>Bottom-up:</text> This method begins by forecasting at the most granular level of the hierarchy (e.g., items in level 2) and then aggregates these forecasts up to higher levels (e.g., stores in level 1 and finally food in level 0). It provides detailed and localized insights, capturing specific trends and patterns. However, the aggregation process may introduce inconsistencies or misalignment at higher levels if the individual forecasts are not well-calibrated.

* <text style='color: #BBDEFC; font-weight: normal;'>Top-down:</text> This method begins with forecasting at the highest level of the hierarchy (e.g., food in level 0) and then distributes the forecast down to lower levels (e.g., stores in level 1 and finally items in level 0). The roll down is done by mantaining the percentage representation of each subcategory from the raw data. This system ensures that the overall forecast is consistent with the broader organizational targets and constraints. However, it might overlook specific local variations or nuances that are important at lower levels.

* <text style='color: #BBDEFC; font-weight: normal;'>Hybrid:</text> This method combines elements of both bottom-up and top-down approaches. For example, it might start with a top-down forecast to set high-level targets and then refine the forecast using bottom-up methods to adjust for local details. It aims to balance the accuracy of detailed forecasts with the consistency of high-level targets, potentially improving both overall alignment and granularity. However, implementing a hybrid approach can be complex, as it requires coordination between different forecasting processes and levels of the hierarchy.

In this project, a bottom-up approach is implemented for hierarchical forecasting, where the models are developed at the most granular level, specifically the store-product level.


<text style='color: #BBDEFC; font-weight: normal;'>Intermittent demand:</text>

Intermittent demand, or sporadic demand, occurs when a product experiences multiple periods of zero sales. This issue can arise from two primary causes:
* The product was in stock but no sales occurred.
* The product was out of stock, preventing any sales.

The source of these zero values can sometimes be unclear, leading to noise and making it difficult for the model to generate accurate predictions.

{{< figure src="/project6/exhibit_1.png" title="Exhibit 1. Intermittent demand for item 120, which is sold in both stores." >}}

To address intermittent demand, several solutions can be employed:

* <text style='color: #BBDEFC; font-weight: normal;'>Getting the inventory information:</text> It helps us to generate stock-out features that allow the algorithms to discriminate the cause of the zero values.

* <text style='color: #BBDEFC; font-weight: normal;'>Model at a higher hierarchical level:</text> If the inventary information and/or stock-out marks are not available, another possible approach is to model at a higher hierarchical level, especially if the products are in very low demand.

* <text style='color: #BBDEFC; font-weight: normal;'>Create synthetic features:</text> It is also possible to create synthetic features that try to identify whether or not stock-outs have occurred.

* <text style='color: #BBDEFC; font-weight: normal;'>Machine learning forecasting:</text> Employing forecasting methods based on machine learning techniques, which are less sensitive to these problems than classical approaches.

* <text style='color: #BBDEFC; font-weight: normal;'>Advanced methodologies:</text> Lastly, there is some more advanced methodologies such as croston method and specialized machine learning models can predict the probability of zero sales on certain days.

In this project, since inventory and stock-out information are not available, synthetic features will be created based on business rules to indicate potential stock-out scenarios.

<text style='color: #BBDEFC; font-weight: normal;'>Huge amount of Stock Keeping Units (SKUs):</text>

In practical applications, particularly in sectors like retail and e-commerce, there are often thousands of different products that need to be modeled to predict sales levels accurately. Given the vast number of SKUs, the desired level of temporal aggregation (e.g., hourly, daily, weekly), the volume of historical data, and the available computational resources, the modeling process can become computationally infeasible. This complexity can challenge even advanced systems and may necessitate the use of scalable approaches or optimization techniques to manage the modeling workload effectively.

In this context, several solutions can be employed:

* <text style='color: #BBDEFC; font-weight: normal;'>Adopt Machine Learning Forecasting:</text> Machine learning models, once trained, can generate forecasts much faster than traditional methods, improving efficiency.
* <text style='color: #BBDEFC; font-weight: normal;'>Utilize Fast Algorithms:</text> Implement faster algorithms like LightGBM, which are optimized for speed and scalability.
* <text style='color: #BBDEFC; font-weight: normal;'>Hierarchical Modeling:</text> Model at a higher hierarchical level and apply top-down reconciliation techniques to estimate forecasts for lower levels, balancing detail and computational demands.
* <text style='color: #BBDEFC; font-weight: normal;'>Leverage Big Data Technologies:</text> Employ big data techniques, such as using powerful cloud computing resources or big data clusters, to handle large datasets and complex models efficiently.

Consequently, for the reasosns explained above, a forecasting model based on a machine learning approach and a LightGBM tree-based algorithm architecture has been developed in this project.




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

The entire process can be consulted in detail [here](https://github.com/pabloelt/lead-scoring-analysis-and-segmentation/blob/main/03_Notebooks/02_Desarrollo/02_Calidad%20de%20Datos.ipynb).

---

## 6. Exploratory Data Analysis
{style="color: #BBDEFC"}

The aim of this phase of the project is to identify trends and patterns that can be transformed into insights, providing valuable information for our project. To achieve this, we perform various statistical evaluations and create graphical representations.

In order to guide this process, a series of seed questions are proposed to serve as a basis for the analysis.

### 6.1 Seed questions
{style="color: #BBDEFC; font-weight: normal"}

**Regarding sales:**

* <text style='color: #BBDEFC; font-weight: normal;'>Q1:</text> How has the company's sales performance evolved over time?
* <text style='color: #BBDEFC; font-weight: normal;'>Q2:</text> How about the sales per product?
* <text style='color: #BBDEFC; font-weight: normal;'>Q3:</text> How are product sales performing across different stores?
* <text style='color: #BBDEFC; font-weight: normal;'>Q4:</text> Are product sales consistent over time, or are there periods with zero demand? If so, is this due to stock-outs, or are the products simply not selling during those periods?
* <text style='color: #BBDEFC; font-weight: normal;'>Q5:</text> What is the seasonality pattern in sales? How do sales vary by month and by day of the week?

**Regarding sell price:**
* <text style='color: #BBDEFC; font-weight: normal;'>Q6:</text> How have the selling prices for each product changed over time?
* <text style='color: #BBDEFC; font-weight: normal;'>Q7:</text>  Are the selling prices fixed, or are they adjusted based on seasonality?
* <text style='color: #BBDEFC; font-weight: normal;'>Q8:</text> How is the selling price impacted by seasonality?

**Regarding events:**
* <text style='color: #BBDEFC; font-weight: normal;'>Q9:</text> How do major events throughout the year affect sales? Which holidays or festivities have the most significant impact?
* <text style='color: #BBDEFC; font-weight: normal;'>Q10:</text> How does each event category influence sales?
* <text style='color: #BBDEFC; font-weight: normal;'>Q11:</text> Which products are particularly affected by these special occasions?


### 6.2 Some results obtained through the EDA
{style="color: #BBDEFC; font-weight: normal"}

These are some of the results that we have obtained by performing the exploratory Data Analysis (EDA) for both categorical and numerical variables that are present in the dataset.

{{< figure src="/project6/exhibit_2.png" title="Exhibit 2. Exploratory Data Analysis: Sell price evolution over time for each of the products." >}}

{{< figure src="/project6/exhibit_3.png" title="Exhibit 3. Exploratory Data Analysis: Seasonality of the sales for each of the products." >}}

 A more detailed analysis of this stage can be found [here](https://github.com/pabloelt/lead-scoring-analysis-and-segmentation/blob/main/03_Notebooks/02_Desarrollo/03_EDA.ipynb).

### 6.3 Insights obtained through the EDA
{style="color: #BBDEFC; font-weight: normal"}

Once the exploratory data analysis has been conducted, the following insights have been obtained:

**Sales:**

* <text style='color: #BBDEFC; font-weight: normal;'>Insight 1:</text> New products were added after a few months, initially launched in just one store.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 2:</text> One store is more significant, often used to test new products before they are introduced in the second store.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 3:</text> There are periods when certain products experience zero demand. It is unclear whether this is due to stock-outs or simply a lack of sales during those times.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 4:</text> Product performance is influenced by seasonality. Some products perform better in summer, while others do better in winter.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 5:</text> Saturdays and Sundays consistently show the highest sales across all products.

**Sell price:**

* <text style='color: #BBDEFC; font-weight: normal;'>Insight 6:</text>  Selling prices show high variability, especially for certain products.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 7:</text> Discounts are relatively common for some products.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 8:</text> While some products have seen consistent price increases, others have experienced permanent price reductions. However, the majority of products maintain relatively stable prices.


**Events:**

* <text style='color: #BBDEFC; font-weight: normal;'>Insight 9:</text>  Sales per product tend to increase during special events, with Thanksgiving, Labor Day, and Easter performing particularly well.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 10:</text> All event categories show similar performance, though sporting and cultural events generate slightly higher sales on average.


### 6.4 Recommended actions
{style="color: #BBDEFC; font-weight: normal"}

Some of the actionable initiatives that the company can implement are the following:

1. With the current information, it is challenging to determine whether intermittent demand is due to stock-outs or simply zero demand for the product. Therefore, it is highly recommended to track warehouse data closely.

2. To optimize sales and reduce warehouse costs, implementing a forecasting model based on machine learning algorithms can be highly effective. A bottom-up approach, starting at the product level, is particularly recommended in this context.

3. Discounts have proven to be quite successful, especially for product 090, which is the top seller. It may be worthwhile to apply this strategy to other products and evaluate the overall impact.

4. Saturdays and Sundays show the highest sales volumes, presenting an opportunity to develop targeted strategies and campaigns.

5. Special days like Thanksgiving, Labor Day, and Easter generate significant sales. These occasions should be thoroughly analyzed, and marketing strategies should be developed to enhance the company’s profitability.


---

## 7. Variable creation and transformation
{style="color: #BBDEFC"}

At this stage of the project, various variable transformation techniques are applied to ensure they meet the requirements of the algorithms used in the modeling phase.

First, to enhance the model’s predictive capacity, new variables are introduced, including:

* <text style='color: #BBDEFC; font-weight: normal;'>Intermittent demand variables:</text> These variables estimate stock-outs using a rolling feature. It assumes that after a certain number of days with zero sales, a stock-out has occurred. Variables are created to account for fixed stock-outs over 3, 7, and 15 days.

* <text style='color: #BBDEFC; font-weight: normal;'>Lag variables:</text> Lag variables are generated for sales (over a range of up to 15 days), selling price (over a range of up to 7 days), and stock-outs (over a range of up to 1 day). The one-day lag for stock-outs is chosen due to the nature of the variable. Since predicting exact zero demand is challenging for the model, using longer lags would be less effective, making a 1-day lag sufficient for this approach. These lag variables are particullarly useful in forecasting predictive models.

* <text style='color: #BBDEFC; font-weight: normal;'>Rolling windows variables:</text> Rolling window variables for the minimum, average, and maximum values are created over a range of up to 15 days. These rolling variables have demonstrated strong predictive power in forecasting projects.

Note that all of these defined variables need to be shifted by one day in the functions, as the model cannot access information for the day it is predicting.

On the other hand, **one-hot encoding** and **target encoding** techniques are used to transform categorical variables into numerical ones. Both methods are applied at this stage: one-hot encoding serves as the basic transformation, while target encoding incorporates sales information before the transformation. We will experiment with both and select the most predictive approach during model analysis.

Regarding the numerical variables, no transformations are necessary since we are using LightGBM, a tree-based algorithm known for its effectiveness in forecasting projects with large datasets. As such, **normalization** and **rescaling** are not required for this project. Similarly, **discretization** or **binarization** of variables is not useful for this project, as our primary focus is on the model's forecasting accuracy rather than interpretability. **Class balancing** is also not applicable in this context.


More details can be found [here](https://github.com/pabloelt/lead-scoring-analysis-and-segmentation/blob/main/03_Notebooks/02_Desarrollo/04_Transformacion%20de%20datos.ipynb).

---

## 8. Forecasting model
{style="color: #BBDEFC"}

At this stage, after completing data quality checks, exploratory data analysis, and variable transformation, we are ready to develop the forecasting model. As mentioned earlier, a supervised machine learning model will be used for this purpose, specifically the LightGBM algorithm, which has demonstrated strong performance in forecasting projects.

To develop the final forecasting model, we need to create a specific model for each product sold in each store. This requires building 20 independent models and reconciling the information using the bottom-up strategy mentioned earlier. The approach involves first testing a particular case to determine the optimal specifications. Then, in the final code, a loop will be implemented to apply the best parameters obtained for that specific product-store combination.

More details about this process can be found [here](https://github.com/pabloelt/lead-scoring-analysis-and-segmentation/blob/main/03_Notebooks/02_Desarrollo/05_Modelizacion%20para%20No%20Supervisado.ipynb).

### 8.1 General variable selection
{style="color: #BBDEFC; font-weight: normal"}

A general variable selection process, considering all products in the dataset, is conducted at this stage of the project. The most predictive features are identified by comparing the results of three different selection methods: Recursive Feature Elimination, Mutual Information, and Permutation Importance. Among these, the Mutual Information method has demonstrated the best performance, offering a smooth transition between variables. This is crucial because we do not want to eliminate too many variables, as this selection analysis will need to be performed for each specific product-store combination.

{{< figure src="/project6/exhibit_4.png" title="Exhibit 4. General variable selection analysis: A number of 73 variables has been selected through the Mutual Information method." >}}

As a result of this analysis, 73 variables have been selected. This set of variables will be used when applying the Mutual Information method to each product-store combination.

### 8.2 Segment profiling
{style="color: #BBDEFC; font-weight: normal"}

Once the optimal number of clusters and the most relevant segmentation variables have been selected, the model is trained and executed, assigning each lead to one of the four existing clusters.

To understand the business implications, average values for each variable used in the model has been calculated, allowing us to identify the most distinguishing characteristics of each segment. This is shown in the table below.

{{< figure src="/project5/exhibit_4.png" title="Exhibit 4. Unsupervised ML modelling: Cluster results from KMeans algorithm." >}}

### 8.3 Segment analysis
{style="color: #BBDEFC; font-weight: normal"}

After analysing the above results, the most differential characteristics for each segment are identified and presented.

<text style='color: #BBDEFC; font-weight: normal;'>Segment 0: Super high-quality Leads</text>

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
* They spend some time on the website.
* Moderate conversion rate.

<text style='color: #BBDEFC; font-weight: normal;'>Segment 3: Low-quality Leads</text>

* Origin: API.
* Last activity: Chat conversation.
* Occupancy: Unemployed.
* Very low time spent on the website.
* Low conversion rate.

### 8.4 Segmentation insights
{style="color: #BBDEFC; font-weight: normal"}

1. The company's most valuable leads are working professionals who arrive through the lead form submission.

2. While SMS campaigns are generally effective, they should be targeted more precisely:
  * Focus on working professionals from API sources who spend above-average time on the website.
  * Avoid sending SMS to leads from Landing Page Submissions who spend minimal time on the site, as they represent the lowest quality leads and divert resources from more promising campaigns.

3. The live chat feature primarily attracts low-quality leads. The company should consider reallocating resources from this service and, for leads from API sources, prioritize email marketing and SMS campaigns instead.


---

## 9. Predictive lead scoring model
{style="color: #BBDEFC"}

A predictive lead scoring model is developed using a supervised machine learning approach. At this stage of the project, several algorithms are tested, including logistic regression, random forest, XGBoost, and LightGBM. Each algorithm is analyzed with an extensive range of hyperparameters to ensure optimal predictive performance. The implementation of this model will enhance customer identification, thereby increasing the conversion rate (CR) and reducing marketing costs.

More details for the predictive lead scoring model can be consulted [here](https://github.com/pabloelt/lead-scoring-analysis-and-segmentation/blob/main/03_Notebooks/02_Desarrollo/07_Modelizacion%20para%20Clasificacion.ipynb).


### 9.1 Variable selection for predictive model
{style="color: #BBDEFC; font-weight: normal"}

Several variable selection methods were tested to identify the most useful features for the predictive model. The primary methods considered were mutual selection, recursive feature elimination, and permutation importance. Among these, permutation importance proved to be the most accurate for this case and aligned well with the variable selection used in the lead segmentation model. The results are displayed in the image below. 

{{< figure src="/project5/exhibit_5.png" title="Exhibit 5. Feature importance: Permutation importance method." >}}

Based on the permutation importance method, the 20 most relevant variables were selected for the predictive model. Additionally, the correlations between these variables were examined, and highly correlated ones were removed. While strong correlations do not typically hinder tree-based algorithms, they can negatively impact the performance of other algorithms, such as logistic regression.

More details [here](https://github.com/pabloelt/lead-scoring-analysis-and-segmentation/blob/main/03_Notebooks/02_Desarrollo/06_Preselecci%C3%B3n%20de%20variables.ipynb).

### 9.2 Model selection
{style="color: #BBDEFC; font-weight: normal"}

Different combinations of hyperparameters are tested for each of the algorithms and the ones with the best AUC (Area under Curve) scoring are collected. On the other hand, all of the combinations are tested with the **cross-validation** method in order to ensure a good stability in the models. The performance of these algorithms is tested with three methods, which are cumulative gains curve,  lift curve, and ROC curve.

Roughly speaking, the cumulative gain curve measures the effectiveness of a classification model by showing the proportion of true positives, while the lift curve shows the ratio of the model's performance to random performance, which helps to understand how much better the model is compared to random guessing. The ROC curve is used to evaluate the trade-off between the true positive rate (sensitivity) and the false positive rate at various threshold settings.

The cumulative gains and lift curves focus on how well the model identifies positives within a sorted population, while the ROC curve evaluates the overall discrimination capability of the model across all thresholds. The results are shown in the figure below.

{{< figure src="/project5/exhibit_6.png" title="Exhibit 6. Performance comparison of the selected algorithms for several metrics." >}}

The XGBoost algorithm presents the best performance in the three charts, however, the results are pretty similar for all of them. Therefore, it is decided to implement the **logistic regression algorithm** for the project due to the following reasons:

1. Its predictive ability closely matches that of the random forest, XGBoost, and LightGBM models.
2. It offers greater interpretability compared to the more complex tre-based algorithms.
3. Being a simpler model, it is easier to maintain and quicker to train, retrain, and execute.
4. Its mathematical simplicity allows for easy migration to the platforms and software used by the company.

Thus, the logistic regression algorithm is used with the following hyperparametrization:
* C = 1
* n_jobs = -1
* penalty = 'l1'
* solver = 'saga'

### 9.3 Optimal discrimination threshold for maximizing ROI
{style="color: #BBDEFC; font-weight: normal"}

Once the predictive model is trained and tested, the next step is to specify the optimal threshold that determines whether a lead is classified as a potential customer (1) or not (0) based on the model's score. To achieve this, a method focused on maximizing ROI is implemented. This method determines the optimal threshold using confusion and impact matrices, which are defined as follows.

{{< figure src="/project5/confusion_matrix.jpg" title="Confusion and Impact matrices." >}}

* **Confusion matrix:** This matrix is used to describe the performance of a classification model. It shows the actual versus predicted classifications and helps to identify how often the model is correctly and incorrectly predicting each class. The output “TN” stands for True Negative which shows the number of negative examples classified accurately. Similarly, “TP” stands for True Positive which indicates the number of positive examples classified accurately. The term “FP” shows False Positive value, i.e., the number of actual negative examples classified as positive; and “FN” means a False Negative value which is the number of actual positive examples classified as negative.
* **Impact matrix:** This matrix is used to quantify the impact or cost associated with the different types of errors made by a model, such as false positives and false negatives. Unlike the confusion matrix, which counts occurrences, the impact matrix assigns a numerical value to the consequences of these outcomes. The output “ITN” stands for Impact of True Negative which shows the economic impact of not to carry out any commercial actions on those leads that were not going to buy the product. Similarly, “ITP” stands for Impact of True Positive which indicates the net profit obtained from commercial actions on customers who end up buying the course. The term “IFP” shows Impact of False Positive value, i.e., the opportunity cost of not having carried out commercial actions on leads who would have become customers. Finally, “IFN” means a Impact of False Negative value which represent the economic cost of commercial actions carried out on a lead that finally does not buy the company’s product.

Therefore, by calculating the confusion matrix and multiplying it by the economic impact matrix for each possible value of the discrimination threshold, it becomes possible to determine which threshold maximizes the resulting function and, consequently, the company’s ROI. The results are shown in the image below.

{{< figure src="/project5/exhibit_7.png" title="Exhibit 7. Expected value for each discrimination treshold. Optimal value is found at 0.05." >}}

In this case, the discrimination threshold value that provides the higher return on investment for the company is 0.05.

---

## 10. Evaluation of the predictive lead scoring model
{style="color: #BBDEFC"}

Finally, the model has been tested on a batch of 2084 leads never seen before by the model (the validation dataset that we reserved at the beginning). By applying the developed lead scoring predictive model, the company has been able to:

1. Increase its conversion rate from 41.70% to 45.77%.
2. Reduce by 9.31% the workload to be managed by the sales department.
3. Reduce by 28.81% the loss in investments.
4. Increase its sales profit by 4.75%.

{{< figure src="/project5/kpi_results.png" title="KPIs improvements achieved after applying the predictive lead scoring model." >}}

The evaluation results can be found [here](https://github.com/pabloelt/lead-scoring-analysis-and-segmentation/blob/main/05_Resultados/Resultados%20del%20proyecto.ipynb).

---

## 11. Retraining and Production scripts
{style="color: #BBDEFC"}

After successfully developing, training, and evaluating both segmentation and predictive models, the final stage of the project involves organizing and optimizing the entire process. This is accomplished by compiling all necessary processes, functions, and code into two streamlined Python scripts:

* <text style='color: #BBDEFC; font-weight: normal;'>Retraining Script:</text> This script is designed to automatically retrain all developed models with new data as needed, ensuring that the models remain accurate and up-to-date.

* <text style='color: #BBDEFC; font-weight: normal;'>Production Script:</text> This script executes all models and generates the desired results, ensuring a smooth transition from development to production.