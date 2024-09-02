---
title: Risk Scoring for Company in the Banking Sector 
summary: A risk-scoring model is developed using machine learning algorithms to assess the profitability of each new transaction or customer. The model predicts the expected loss by analyzing the Probability of Default, Loss Given Default, and Exposure at Default.
tags:
  - Machine Learning
date: 2024-08-30
#external_link: http://github.com

---

*Note: Documentation available on the [GitHub Repository](https://github.com/pabloelt/sales-forcasting-for-a-retail-company) is currently in Spanish. It will be soon updated to English.*
{style="color: #aaaaaa"}

{{< toc >}}

<ul class="cta-group">
  <li>
    <a href="https://03-notebooks03-systemapp-risk-scoring-deploymentapp-ri-cv1jfo.streamlitapp.com/" target="_blank" rel="noopener" class="btn btn-primary px-3 py-3">Launch Credit Risk Analyzer Web App!</a>
  </li>
</ul>

## 1. Introduction
{style="color: #BBDEFC"}

The client for this project is a neo bank company specialized in offering loans at a competitive he client for this project is a neobank specializing in offering competitively priced loans. However, the company is concerned about the quality of borrowers accessing their products. They require a robust system to assist in making informed loan approval decisions based on applicants' profiles.

The goal is to implement a risk-scoring model using artificial intelligence algorithms to identify 'risky' applicants and estimate their associated expected losses. This information will be used to manage the bank's economic capital, portfolio, and risk assessment effectively.

Notes:

* This article presents a technical explanation of the development process followed in the project.
* Source code can be found [here](https://github.com/pabloelt/sales-forcasting-for-a-retail-company).
* You can also test the credit risk analyzer web application [here](https://github.com/pabloelt/sales-forcasting-for-a-retail-company).

---

## 2. Objectives
{style="color: #BBDEFC"}

The main objective is to develop a risk-scoring model using machine learning algorithms to predict potentially risky borrowers. This model will estimate the expected financial loss for each new customer-loan pairing, based on the company's historical data. By leveraging this advanced analytical tool, the company's performance will be significantly enhanced.

---

## 3. Understanding of the problem
{style="color: #BBDEFC"}

Credit risk is associated with the possibility that a borrower will fail to meet their obligations according to the agreed terms, such as repaying a loan. This risk is a critical concern for banks because it can lead to financial losses if borrowers default on their loans. Banks manage credit risk through various means, including:

* <text style='color: #BBDEFC; font-weight: normal;'>Credit Assessment:</text> Evaluating the borrower's creditworthiness before approving a loan.

* <text style='color: #BBDEFC; font-weight: normal;'>Diversification:</text> Spreading out lending across different sectors and borrowers to reduce the impact of any single default.

* <text style='color: #BBDEFC; font-weight: normal;'>Collateral:</text> Requiring assets to secure loans, which can be seized if the borrower defaults.

* <text style='color: #BBDEFC; font-weight: normal;'>Monitoring:</text> Continuously assessing borrowers' financial health and adjusting terms as needed.

Effective credit risk management is crucial for banks to maintain financial stability and absorb potential losses without compromising their overall health. In this regard, machine learning algorithms have proven particularly valuable. They can be employed to develop sophisticated models that predict financial loss per borrower using data science techniques and historical company data. These advanced models enhance the accuracy of risk assessments and support better decision-making in credit management.

---

## 4. Project Design
{style="color: #BBDEFC"}

### 4.1 Methodology
{style="color: #BBDEFC; font-weight: normal"}

The project has been designed with a multi-step methodology, which is summarized in the figure bellow.

{{< figure src="/project5/methodology.png" title="Project methodology." >}}

The process for this project consists of two main stages: the development phase and the production phase.

The development phase begins with the set up and data importation, followed by a thorough data quality review. Next, an exploratory data analysis is conducted to uncover key insights. The variable transformation step involves selecting the most relevant variables that impact the problem and applying the necessary transformations. Following this, the risk-scoring model is implemented based on machine learning algorithms. During the evaluation process, all metrics are thoroughly tested.

In the production phase, the model is prepared for deployment, ensuring that the code is optimized for production. Additionally, a retraining script is created during this stage to facilitate future updates.

### 4.2 Project scope
{style="color: #BBDEFC; font-weight: normal"}

To estimate the Expected Loss {{< math >}}$(EL)${{< /math >}} associated with a loan application, three key risk parameters are considered:

* <text style='color: #BBDEFC; font-weight: normal;'>Probability of Default {{< math >}}$(PD)${{< /math >}}:</text> This measures the likelihood that a borrower will default, based on an internally assigned credit rating.

* <text style='color: #BBDEFC; font-weight: normal;'>Exposure at Default {{< math >}}$(EAD)${{< /math >}}:</text> This indicates the amount of outstanding debt at the time of default.

* <text style='color: #BBDEFC; font-weight: normal;'>Loss Given Default {{< math >}}$(LGD)${{< /math >}}:</text> This metric represents the percentage of the loan exposure that is not expected to be recovered if a default occurs.

To estimate these risk parameters, three predictive machine learning models will be developed. The predictions from these models will then be combined to calculate the expected loss for each loan transaction. To calculate this value, the following formula is applied:

{{< math >}}
$$
EL[$] = PD \cdot P[$] \cdot EAD \cdot LDG,
$$
{{< /math >}}

where {{< math >}}$P${{< /math >}} is the loan principal, i.e., the amount of money the borrower whises to apply for.


### 4.3 Entities and data
{style="color: #BBDEFC; font-weight: normal"}

The data under analysis includes information collected by the company about two primary entities:

* <text style='color: #BBDEFC; font-weight: normal;'>Borrowers:</text> This dataset features details on the applicant's profile, such as employment history, the number of mortgages and credit lines, annual income, and other personal information.

* <text style='color: #BBDEFC; font-weight: normal;'>Loans:</text> The remaining features provide information about the loans themselves, including the loan amount, interest rate, status (i.e., whether the loan is current or in default), tenor (either 36 or 60 months), among other details.

On the other hand, before conducting any analysis or data transformation, it is crucial to set aside a randomly selected portion of the dataset for validation purposes. This reserved data will be used to validate the models after they have been trained and tested on the remaining data.

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

The entire process can be consulted in detail [here](https://github.com/pabloelt/sales-forcasting-for-a-retail-company/blob/main/03_Notebooks/02_Desarrollo/02_Calidad%20de%20Datos.ipynb).

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

 A more detailed analysis of this stage can be found [here](https://github.com/pabloelt/sales-forcasting-for-a-retail-company/blob/main/03_Notebooks/02_Desarrollo/03_EDA.ipynb).

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


More details can be found [here](https://github.com/pabloelt/sales-forcasting-for-a-retail-company/blob/main/03_Notebooks/02_Desarrollo/04_Transformacion%20de%20datos.ipynb).

---

## 8. Risk-scoring model
{style="color: #BBDEFC"}






The risk-scoring model is compound of three different and independent models: a first one for the Probability of Default, a second one for the Exposure at Default, and a third one for the Loss Given Default.

{{< figure src="/project7/el_models.png" title="Expected loss predicted with a combination of three different machine learning algorithms for PD, EAD, and LGD." >}}

It is important to note that the model for estimating the Probability of Default will utilize a logistic regression algorithm. ‘Black box algorithms’ are often unsuitable for regulated financial services due to their lack of interpretability and auditability, which can pose macro-level risks and, in some cases, conflict with legal requirements for explainability. To address this, a highly explainable AI model like logistic regression will be used, as it provides clear and understandable insights into its decision-making process.

For estimating Exposure at Default and Loss Given Default, various algorithms and hyperparameter combinations were evaluated, including Ridge, Lasso, and LightGBM. Ultimately, the LightGBM algorithm was selected for both cases due to its superior performance.








At this stage, after completing data quality checks, exploratory data analysis, and variable transformation, we are ready to develop the forecasting model. As mentioned earlier, a supervised machine learning model will be used for this purpose, specifically the LightGBM algorithm, which has demonstrated strong performance in forecasting projects.

To develop the final forecasting model, we need to create a specific model for each product sold in each store. This requires building 20 independent models and reconciling the information using the bottom-up strategy mentioned earlier. The approach involves first testing a particular case to determine the optimal specifications. Then, in the final code, a loop will be implemented to apply the best parameters obtained for that specific product-store combination.

More details about this process can be found [here](https://github.com/pabloelt/sales-forcasting-for-a-retail-company/blob/main/03_Notebooks/02_Desarrollo/06_Modelizacion%20para%20Regresion.ipynb).

### 8.1 General variable selection
{style="color: #BBDEFC; font-weight: normal"}

A general variable selection process, considering all products in the dataset, is conducted at this stage of the project. The most predictive features are identified by comparing the results of three different selection methods: Recursive Feature Elimination, Mutual Information, and Permutation Importance. Among these, the Mutual Information method has demonstrated the best performance, offering a smooth transition between variables. This is crucial because we do not want to eliminate too many variables, as this selection analysis will need to be performed for each specific product-store combination.

{{< figure src="/project6/exhibit_4.png" title="Exhibit 4. General variable selection analysis: A number of 73 variables has been selected through the Mutual Information method." >}}

As a result of this analysis, a number of 73 variables have been selected. This number of variables will be used when applying the Mutual Information method to each product-store combination.

More information is provided [here](https://github.com/pabloelt/sales-forcasting-for-a-retail-company/blob/main/03_Notebooks/02_Desarrollo/05_Preselecci%C3%B3n%20de%20variables.ipynb).

### 8.2 Developing a one-step forecasting model for a specific product-store combination
{style="color: #BBDEFC; font-weight: normal"}

The objective at this stage of the project is not to produce the final models, but to design the modeling process—covering algorithm selection, hyperparameter optimization, and model evaluation—at the minimum analysis unit (product-store). This is done to ensure the process functions correctly and to identify and eliminate potential error sources before scaling the one-step forecasting process to all product-store combinations.

For this case, the product with code 586 sold in the store CA_3 is selected for this specific analysis.


<text style='color: #BBDEFC; font-weight: normal;'>Cross-validation strategy:</text>

To prevent overfitting and evaluate model performance more robustly than with a simple train-test split, a cross-validation strategy has been implemented. However, cross-validation for time series data is not straightforward. Randomly assigning samples to the test or train sets is not feasible due to the temporal dependency between observations. The time sequence must be preserved.

The appropriate method for cross-validating time series models is rolling cross-validation. This approach starts with a small subset of data for training, forecasts subsequent data points, and then assesses the accuracy of these forecasts. The forecasted data points are incorporated into the next training set, and the process continues with forecasting subsequent data points.

{{< figure src="/project6/cross_validation.png" title="Cross-validation process for time-series data." >}}

In the present project the cross-validation process has been implemented using <text style='color: #BBDEFC; font-weight: normal;'>sklearn.model_selection.TimeSeriesSplit</text> class of scikit-learn package with 3 splits and 8 days as maximum training size.

<text style='color: #BBDEFC; font-weight: normal;'>Selecting algorithm and hyperparameters:</text>

As outlined in the general design phase of the project, the LightGBM algorithm is chosen for implementing the various models due to its strong balance between predictive accuracy and computational efficiency.

Different combinations of hyperparameters have been tested to find those with the best performance. Evaluation scores obtained in the tested parametrizations remains stable during the cross-validation process, which is a good indicator of the stability of the model predictions.

In the particular case of product 586 sold in store CA_3, the best parametrization obtained for the LightGBM algorithm is:

* learning_rate = 0.1
* max_iter = 100
* max_leaf_nodes = 31
* max_depth = None
* min_samples_leaf = 20
* l2_regularization = 0
* max_bins = 255
* scoring = 'loss'

<text style='color: #BBDEFC; font-weight: normal;'>Checking:</text>

The objective here is not to evaluate the model's quality, as the predictions were made using the training data, but rather to ensure that the process functions correctly. We aim to confirm that the predictions are within the correct order of magnitude and that no other anomalies are detected before moving forward with the project.

{{< figure src="/project6/exhibit_5.png" title="Exhibit 5: Checking of the predicted data from the forecasting model for product 'FOODS_3_586' sold in store 'CA_3' over the last three months." >}}

No issues have been identified, so the project will proceed as planned.


### 8.3 Generalizing the one-step forecasting model creation process
{style="color: #BBDEFC; font-weight: normal"}

Once the forecasting model has been created and tested for an individual product-store combination, we can develop the necessary code to scale this process across all product-store combinations (massive forecasting evaluation). At this stage, the same 73 variables selected for product 586 are still being used. These variables will be updated to the specific ones for each combination in the final production code. The model algorithms, however, are now tailored to each specific combination.


<text style='color: #BBDEFC; font-weight: normal;'>Checking:</text>

Again, it is important to note that the results obtained here are solely for verifying that the process functions correctly, not for evaluating the quality of the models, as predictions are made using the training data rather than the validation dataset.

{{< figure src="/project6/exhibit_6.png" title="Exhibit 6: Checking of the predicted data from the forecasting model for all product-store combinations over the last three months." >}}

No issues have been identified and the project can continue.

### 8.4 Multi-Step Forecasting
{style="color: #BBDEFC; font-weight: normal"}

Once the general code for production is developed, it is essential to decide on the type of multi-step forecasting to implement. There are two main approaches to this: a direct forecasting and a recursive forecasting.

<text style='color: #BBDEFC; font-weight: normal;'>Direct Multi-step Forecasting:</text>

In direct forecasting, separate models are trained for each future time step. For example, to predict the next 3 days, you would need to train three distinct models: one for t+1, another for t+2, and a third for t+3.

{{< figure src="/project6/direct_forecast.png" title="Direct Multi-step Forecast strategy." >}}

This approach allows each model to be tailored to the specific characteristics of the prediction horizon, often resulting in more accurate predictions for the individual time steps since each model is directly optimized for that step using only real data. However, this method requires more computational resources because multiple models need to be trained, and there is no shared information across different days, which can be a disadvantage if the time steps are strongly correlated.

<text style='color: #BBDEFC; font-weight: normal;'>Recursive Multi-step Forecasting:</text>

In recursive forecasting (also known as iterative forecasting), a single model is used to predict one time step ahead, and this prediction is then fed back into the model to predict the next time step, and so on. For example, to predict t+1, t+2, and t+3, the model first predicts t+1, then uses the predicted t+1 to predict t+2, and uses t+2 to predict t+3.

{{< figure src="/project6/recursive_forecast.png" title="Recursive Multi-step Forecast strategy." >}}

This approach is simpler as it requires only one model, reducing both training time and computational resources. It can also be more stable in some cases by leveraging the sequential nature of time series data. However, errors tend to propagate, leading to decreased accuracy for predictions further into the future. Additionally, the model is not specifically optimized for each time step beyond the first one.

For this project, a recursive multi-step forecasting approach has been implemented to minimize development and maintenance costs for the models."


---

## 9. Evaluation of the forecasting model
{style="color: #BBDEFC"}

Once the general production code is developed, the forecasting model's performance can be evaluated. To do this, we first need to prepare the data for the model. In real-life operation, the model requires only the last 15 days of data to function, as determined by the lag variables defined earlier in the modeling process. To facilitate this, we have prepared a file called 'DatosParaProduccion.csv,' which is part of the validation data (December 2015) reserved at the beginning of this project specifically for the evaluation of the final forecasting model.

In a real-life scenario, data will typically be sourced from a SQL database. The process should follow these steps:

* A SQL script should be prepared to extract the company’s last 15 days of data, with additional commands to structure the resulting CSV file. The output file must match the structure of 'DatosParaProduccion.csv' to ensure the forecasting model operates correctly.

* The CSV file is then generated and passed to the model to obtain predictions for the next 8 days.

* This process is repeated automatically each day to provide new predictive data, enabling informed business decisions that enhance the company's profitability.

Therefore, the model has been evaluated using the prepared data in 'DatosParaProduccion.csv,' and the predictions for each product-store combination are shown in the figure below. While some models perform better than others, the overall performance of the recursive forecasting approach is satisfactory. The final mean absolute error, calculated by comparing actual and predicted sales across all product-store combinations, is approximately 4.73.

{{< figure src="/project6/exhibit_7.png" title="Exhibit 7. Comparison between the predicted and real sales for each product for the last 8 days of December 2015." >}}

The evaluation results can be found [here](https://github.com/pabloelt/sales-forcasting-for-a-retail-company/blob/main/03_Notebooks/02_Desarrollo/07_Preparacion%20del%20codigo%20de%20produccion.ipynb).

---

## 10. Retraining and Production scripts
{style="color: #BBDEFC"}

After successfully developing, training, and evaluating the forecasting model, the final stage of the project involves organizing and optimizing the entire process. This is accomplished by compiling all necessary processes, functions, and code into two streamlined Python scripts:

* <text style='color: #BBDEFC; font-weight: normal;'>Retraining Script:</text> This script is designed to automatically retrain all developed models with new data as needed, ensuring that the models remain accurate and up-to-date.

* <text style='color: #BBDEFC; font-weight: normal;'>Production Script:</text> This script executes all models and generates the desired results, ensuring a smooth transition from development to production.