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

* <text style='color: #BBDEFC; font-weight: normal;'>Insight 1:</text> Ten neighborhoods with a high investment potential have been identified.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 2:</text> It is recommended to search for two-bedroom properties that can accommodate 4 guests.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 3:</text> It is recommended to search for properties in one of the identified neighborhoods that are not necessarily close to points of interest.
* <text style='color: #BBDEFC; font-weight: normal;'>Insight 4:</text> A new business model based on rentals for specific moments of high sporting interest should be explored.

 A more detailed analysis of this stage can be found [here](https://github.com/pabloelt/detection-inefficiencies-photovoltaic-solar-plants/blob/main/Notebooks/04_Analisis%20e%20Insights.ipynb).

---





The client for this project is a real estate company that invests in large cities by purchasing properties to rent out as vacation apartments. The managers have decided to invest in Madrid and are interested in analyzing publicly available data from the sector leader, Airbnb, to identify the types of properties with the greatest commercial potential for vacation rentals.

{{< figure src="/project2/exhibit_1.png" title="Exhibit 1: ." >}}

The client for this project is a real estate company that invests in large cities by purchasing properties to rent out as vacation apartments. The managers have decided to invest in Madrid and are interested in analyzing publicly available data from the sector leader, Airbnb, to identify the types of properties with the greatest commercial potential for vacation rentals.

{{< figure src="/project2/exhibit_2.png" title="Exhibit 2: ." >}}

The client for this project is a real estate company that invests in large cities by purchasing properties to rent out as vacation apartments. The managers have decided to invest in Madrid and are interested in analyzing publicly available data from the sector leader, Airbnb, to identify the types of properties with the greatest commercial potential for vacation rentals.

{{< figure src="/project2/exhibit_3.png" title="Exhibit 3: ." >}}

The client for this project is a real estate company that invests in large cities by purchasing properties to rent out as vacation apartments. The managers have decided to invest in Madrid and are interested in analyzing publicly available data from the sector leader, Airbnb, to identify the types of properties with the greatest commercial potential for vacation rentals.

{{< figure src="/project2/exhibit_4.png" title="Exhibit 4: ." >}}

The client for this project is a real estate company that invests in large cities by purchasing properties to rent out as vacation apartments. The managers have decided to invest in Madrid and are interested in analyzing publicly available data from the sector leader, Airbnb, to identify the types of properties with the greatest commercial potential for vacation rentals.

{{< figure src="/project2/exhibit_5.png" title="Exhibit 5: ." >}}

The client for this project is a real estate company that invests in large cities by purchasing properties to rent out as vacation apartments. The managers have decided to invest in Madrid and are interested in analyzing publicly available data from the sector leader, Airbnb, to identify the types of properties with the greatest commercial potential for vacation rentals.

{{< figure src="/project2/exhibit_6.png" title="Exhibit 6: ." >}}

The client for this project is a real estate company that invests in large cities by purchasing properties to rent out as vacation apartments. The managers have decided to invest in Madrid and are interested in analyzing publicly available data from the sector leader, Airbnb, to identify the types of properties with the greatest commercial potential for vacation rentals.

{{< figure src="/project2/exhibit_7.png" title="Exhibit 7: ." >}}

The client for this project is a real estate company that invests in large cities by purchasing properties to rent out as vacation apartments. The managers have decided to invest in Madrid and are interested in analyzing publicly available data from the sector leader, Airbnb, to identify the types of properties with the greatest commercial potential for vacation rentals.

{{< figure src="/project2/exhibit_8.png" title="Exhibit 8: ." >}}