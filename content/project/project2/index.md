---
title: Detection of Inefficiencies in Photovoltaic Solar Plants
summary: Two underperforming photovoltaic solar plants are being analyzed to determine the root cause of the problem. The analysis considers several perspectives, including sensor data, energy generation, and the efficiency in the energy conversion.
tags:
  - Discovery Projects
date: 2022-01-01
#external_link:
---

*Note: Documentation available on the [GitHub Repository](https://github.com/pabloelt/detection-inefficiencies-photovoltaic-solar-plants) is currently in Spanish. It will be soon updated to English.*
{style="color: #aaaaaa"}

{{< toc >}}

## 1. Introduction
{style="color: #BBDEFC"}

The client for this project is a photovoltaic solar power generation company. This company, which operates nationwide, has detected anomalous behaviors in two of its plants. However, the maintenance team cannot identify the cause of the problem.

Before dispatching a team of engineers, they have requested the data science team to analyze the sensor and performance data to identify the potential root cause of the issue.

Notes:

* This article presents a technical explanation of the development process followed in the project.
* Source code can be found [here](https://github.com/pabloelt/detection-inefficiencies-photovoltaic-solar-plants).

---

## 2. Objectives
{style="color: #BBDEFC"}

The main objective is to analyze the data from the past month for the two affected solar plants and investigate the root cause of the problem. Based on this analysis, the company will decide whether to dispatch a team of engineers to the plants or apply another solution.

---

## 3. Project Design
{style="color: #BBDEFC"}

This project has been designed by taking into consideration the following levers, KPIs, and entities from which data have been obtained. In addition, a brief scheme of how this photovoltaic solar plants works, is presented below.

{{< figure src="/project2/scheme.png" title="A brief scheme of how the photovoltaic solar plants works." >}}


### 3.1 Levers
{style="color: #BBDEFC; font-weight: normal"}

The levers for this project are clear and are summarized below:

* <text style='color: #BBDEFC; font-weight: normal;'>Irradiation:</text> Higher irradiation typically leads to greater DC generation. However, the relationship is not strictly monotonic; at certain levels, increased temperatures can reduce generation capacity.
* <text style='color: #BBDEFC; font-weight: normal;'>Condition of the Panels:</text> Panels must be clean and fully operational to maximize DC energy generation.
* <text style='color: #BBDEFC; font-weight: normal;'>Efficiency of the Inverters:</text> While some loss is inevitable in the conversion from DC to AC, it should be minimized. Inverters must be in good condition and functioning properly.
* <text style='color: #BBDEFC; font-weight: normal;'>Meters and Sensors:</text> Accurate measurement is crucial. If meters and sensors fail, we lose traceability and the ability to detect faults.

### 3.2 KPIs
{style="color: #BBDEFC; font-weight: normal"}

* <text style='color: #BBDEFC; font-weight: normal;'>Irradiation:</text> Measures the solar energy received in watts per square meter.
* <text style='color: #BBDEFC; font-weight: normal;'>Ambient and Module Temperature:</text> Measured by the plant sensors in degrees Celsius.
* <text style='color: #BBDEFC; font-weight: normal;'>DC Power:</text> Measures the kilowatts of direct current.
* <text style='color: #BBDEFC; font-weight: normal;'>AC Power:</text> Measures the kilowatts of alternating current.
* <text style='color: #BBDEFC; font-weight: normal;'>Inverter Efficiency:</text> Measures the conversion efficiency from DC to AC. It is calculated as (AC / DC) * 100.

### 3.3 Entities and Data
{style="color: #BBDEFC; font-weight: normal"}

The most relevant entities and data, which are available in the collected information, are summarized below:

* <text style='color: #BBDEFC; font-weight: normal;'>Available information:</text> The information is collected in windows of 15 minutes during 34 days.
* <text style='color: #BBDEFC; font-weight: normal;'>Number of plants:</text> Two plants.
* <text style='color: #BBDEFC; font-weight: normal;'>Number of inverters:</text> Several inverters for each of the affected plants.
* <text style='color: #BBDEFC; font-weight: normal;'>Number of sensors:</text> Just one sensor for each plant. Those sensors are measuring not only the irradiation but also the ambient and modules temperature.

---

## 4. Data Quality
{style="color: #BBDEFC"}

In this stage of the project, general data quality correction processes have been applied, such as:

* Data renaming.
* Type correction.
* Proper selection of the most relevant data for the project.
* Analysis of nulls and duplicated registers.
* Analysis of numerical and categorical variables.
* Creation of new variables: efficiency, indicators for null DC generation, ...

The entire process can be consulted in detail [here](https://github.com/pabloelt/detection-inefficiencies-photovoltaic-solar-plants/blob/main/Notebooks/02_Calidad%20de%20datos%20y%20creacion%20datamart%20analitico.ipynb).

---

## 5. Exploratory Data Analysis
{style="color: #BBDEFC"}

The aim of this phase of the project is to identify trends and patterns that can be transformed into insights, providing valuable information for our project. To achieve this, we perform various statistical evaluations and create graphical representations.

In order to guide this process, a series of seed questions are proposed to serve as a basis for the analysis.

### 5.1 Seed questions
{style="color: #BBDEFC; font-weight: normal"}

**Regarding irradiation:**

* <text style='color: #BBDEFC; font-weight: normal;'>Q1:</text> Does sufficient irradiation reach the plants every day?
* <text style='color: #BBDEFC; font-weight: normal;'>Q2:</text> Is it similar at both plants?
* <text style='color: #BBDEFC; font-weight: normal;'>Q3:</text> How is it distributed by hour?
* <text style='color: #BBDEFC; font-weight: normal;'>Q4:</text>How is it related to ambient temperature and module temperature?

**Regarding the plants:**

* <text style='color: #BBDEFC; font-weight: normal;'>Q5:</text> Do they receive the same amount of irradiation?
* <text style='color: #BBDEFC; font-weight: normal;'>Q6:</text> Do they have a similar number of inverters?
* <text style='color: #BBDEFC; font-weight: normal;'>Q7:</text> Do they generate a similar amount of DC?
* <text style='color: #BBDEFC; font-weight: normal;'>Q8:</text> Do they generate a similar amount of AC?

**Regarding DC generation:**

* <text style='color: #BBDEFC; font-weight: normal;'>Q9:</text> What is the relationship between irradiation and DC generation?
* <text style='color: #BBDEFC; font-weight: normal;'>Q10:</text> Is it affected at any point by the ambient or module temperature?
* <text style='color: #BBDEFC; font-weight: normal;'>Q11:</text> Is it similar at both plants?
* <text style='color: #BBDEFC; font-weight: normal;'>Q12:</text> How is it distributed throughout the day?
* <text style='color: #BBDEFC; font-weight: normal;'>Q13:</text> Is it consistent over the days?
* <text style='color: #BBDEFC; font-weight: normal;'>Q14:</text> Is it consistent across all inverters?
* <text style='color: #BBDEFC; font-weight: normal;'>Q15:</text> Have there been moments of failure?

**Regarding AC generation:**

* <text style='color: #BBDEFC; font-weight: normal;'>Q16:</text> What is the relationship between DC and AC generation?
* <text style='color: #BBDEFC; font-weight: normal;'>Q17:</text> Is it similar at both plants?
* <text style='color: #BBDEFC; font-weight: normal;'>Q18:</text> How is it distributed throughout the day?
* <text style='color: #BBDEFC; font-weight: normal;'>Q19:</text> Is it consistent over the days?
* <text style='color: #BBDEFC; font-weight: normal;'>Q20:</text> Is it consistent across all inverters?
* <text style='color: #BBDEFC; font-weight: normal;'>Q21:</text> Have there been moments of failure?

**Regarding meters and sensors:**

* <text style='color: #BBDEFC; font-weight: normal;'>Q22:</text> Are the irradiation data reliable?
* <text style='color: #BBDEFC; font-weight: normal;'>Q23:</text> Are the temperature data reliable?
* <text style='color: #BBDEFC; font-weight: normal;'>Q24:</text> Are the DC data reliable?
* <text style='color: #BBDEFC; font-weight: normal;'>Q25:</text> Are the AC data reliable?
* <text style='color: #BBDEFC; font-weight: normal;'>Q26:</text> Are the data similar between both plants?

### 5.2 Insights
{style="color: #BBDEFC; font-weight: normal"}

Once the exploratory data analysis has been conducted, the following insights have been obtained:

* <text style='color: #BBDEFC; font-weight: normal;'>Insight 1:</text> Both solar plants are receiving approximately the same amount of energy.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 2:</text> The quality of the data is pretty bad.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 3:</text> Plant 2 generates much lower levels of DC even at similar levels of irradiation.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 4:</text> Plant 1 has a very low capacity to convert DC to AC.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 5:</text> Inverters in Plant 2 are receiving high quantities of zero DC production.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 6:</text> Inverters in Plant 1 are not working properly.

 A more detailed analysis of this stage can be found [here](https://github.com/pabloelt/detection-inefficiencies-photovoltaic-solar-plants/blob/main/Notebooks/04_Analisis%20e%20Insights.ipynb).

---

## 6. Results Communication
{style="color: #BBDEFC"}

In this stage of the project, we are presenting the insights that we have obtained during the exploratory data analysis and the main conclusions for each of them.

<text style='color: #BBDEFC; font-weight: normal;'>Both solar plants are receiving approximately the same amount of energy</text>

* The two affected solar plants are receiving approximately the same energy levels based on irradiation, ambient temperature, and temperature reached by the photovoltaic modules. Moreover, the following data has been found in the sensors analysis:

  * Irradiation is working on the modules from 7 am to 5 pm.
  * Maximum irradiation is reached from 11 am to 12 am.
  * Maximum ambient temperature is reached from 2 pm to 4 pm.

{{< figure src="/project2/exhibit_1.png" title="Exhibit 1: Levels of energy received on each plant based on irradiation, ambient, and modules temperature." >}}

* A deeper anaysis on these quantities is also conducted. The irradiation levels seems to be more connected with the modules than the ambient temperature in both plants.

{{< figure src="/project2/exhibit_2.png" title="Exhibit 2: Several metrics analyzing irradiation, ambient, and modules temperature, highlighting the connections between these factors." >}}


<text style='color: #BBDEFC; font-weight: normal;'>The quality of the data is pretty bad</text>

* The amount of KW registered per day is not trustworthy in either of the two affected plants.

  * Plant 1 presents a peak in the cumulative variable *kw_dia*, which should not be there.
  * Plant 2 presents cumulative data at the earliest hours of the day. It should not be possible.

{{< figure src="/project2/exhibit_3.png" title="Exhibit 3: Mean values of the cumulative KW per hour during a working day for each of the affected plants." >}}

* The registered amounts of KW of DC and AC are also weird, since the *kw_dc* registered in Plant 1 is ten times larger than in Plant 2.

At this stage of the project, the data collection processes and their reliability needs to be reviewed. However, for educational purposes, <u>**we will proceed with the analysis under the assumption that the values of DC and AC are correct**</u>.


<text style='color: #BBDEFC; font-weight: normal;'>Plant 2 generates much lower levels of DC even at similar levels of irradiation</text>

* It seems that Plant 1 generates much more DC than Plant 2 for the same levels of irradiation and temperature.

  * Furthermore, Plant 1 has much more variability, while Plant 2 is more consistent.

{{< figure src="/project2/exhibit_4.png" title="Exhibit 4: Total production of DC in KW per day in each of the affected plants. The variability in Plant 1 is much higher." >}}


<text style='color: #BBDEFC; font-weight: normal;'>Plant 1 has a very low capacity to convert DC to AC</text>

* It seems that Plant 1 has a very poor conversion from DC to AC.
* Plant 2 presents a regular conversion but there is a strange reduction of efficiency in the middle hours. 

{{< figure src="/project2/exhibit_5.png" title="Exhibit 5: Mean efficiency curves per hour for both of the affected plants." >}}


<text style='color: #BBDEFC; font-weight: normal;'>Inverters in Plant 2 are receiving high quantities of zero DC production</text>

* The strange reduction of efficiency in Plant 2 is due to the high quantities of zero DC production that is coming to the affected inverters.
* Inverters in Plant 1 does not present this problem.

{{< figure src="/project2/exhibit_6.png" title="Exhibit 6: Percentage of zero DC production for each inverter in each of the plants." >}}


<text style='color: #BBDEFC; font-weight: normal;'>Inverters in Plant 1 are not working properly</text>

* Inverters in Pant 1 are not working as they should, so their modules needs to be inspected.
* Inverters in Plant 2 are working fine.

{{< figure src="/project2/exhibit_8.png" title="Exhibit 7: Efficiency boxplots for each inverter in Plant 1." >}}


{{< figure src="/project2/exhibit_7.png" title="Exhibit 8: Efficiency boxplots for each inverter in Plant 2." >}}



<text style='color: #BBDEFC; font-weight: normal;'>Final recommendations</text>

* Review the data collection processes and their reliability.
* Perform a maintenance inspection on the modules connected with the identified inverters in Plant 2, since there are many moments of zero DC generation.
* Perform a maintenance inspection of all inverters in Plant 1.