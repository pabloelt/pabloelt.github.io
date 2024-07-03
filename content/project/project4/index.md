---
title: Dream Resort Hotels Dynamic Dashboard
summary: An interactive and dynamic dashboard has been developed for a hotel group. The main KPIs, including turnover, ADR, number of reservations, occupancy rate, RevPAR, and cancellation rate, are visualized in the dashboard along with other relevant metrics.
tags:
  - Dashboards
date: 2024-07-02
#external_link: http://github.com
---
*Note: The final interactive dashboard and its individual sheets are publicly available [here](https://public.tableau.com/views/Dream_resort_hotels_dynamic_dashboard/Dashboard1?:language=es-ES&publish=yes&:sid=&:display_count=n&:origin=viz_share_link).*
{style="color: #aaaaaa"}

{{< toc >}}

## 1. Introduction
{style="color: #BBDEFC"}

The client for this project is a hotel group specializing in the vacation market. They operate several hotels and rooms worldwide. However, the general performance information of the group is not properly organized. Consequently, they need a functional and interactive dashboard displaying the main KPIs and the most relevant information to streamline the operations of the company.

Notes:

* This article presents a technical explanation of the development process followed in the project.
* Final dashboard and its individual sheets are publicly available [here](https://public.tableau.com/views/Dream_resort_hotels_dynamic_dashboard/Dashboard1?:language=es-ES&publish=yes&:sid=&:display_count=n&:origin=viz_share_link).

---

## 2. Objectives
{style="color: #BBDEFC"}

The main objective is to create a functional and interactive dashboard for the company. This will enable managers to organize hotel information effectively and operate in a more data-driven manner. [Tableau Public](https://public.tableau.com/app/discover) software is used for this project.

---

## 3. Project Design
{style="color: #BBDEFC"}

For the design of this project, we have followed a straightforward methodology, summarized in the following image. The initial time invested in creating this methodology plan will help us to organize the information properly and to present a more complete and valuable final dashboard. Additionally, this methodology will also help to optimize time and resources in the implementation of the dashboard.

{{< figure src="/project4/methodology.png" title="Summarized methodology followed in the project design of the interactive dashboard." >}}

### 3.1 Company requirements
{style="color: #BBDEFC; font-weight: normal"}

 The goal in this first and fundamental step is to determine the requirements and the scope of the project. To achieve this, some meetings are organized with the management team of the hotel group to understand their expectations, the business problematics they face, the KPIs they want to measure, the desired time frames, and other relevant details for the good performance of the company. A summary of the questions posed to the management team and its feedback are presented bellow.

<text style='color: #BBDEFC; font-weight: normal;'>What business objectives do you want to achieve by developing this dashboard?</text>

* To have a single report containing the main data necessary for hotel management.
* To view current data as well as trends over the last few months.
* To ensure that the entire management team uses the same data and shares the same metrics.

<text style='color: #BBDEFC; font-weight: normal;'>What data specifically would you like to visualize?</text>

* Turnover
* Number of reservations
* Occupancy rate
* ADR (Average Daily Rate)
* RevPAR (Revenue per Available Room)
* Cancellation rate

<text style='color: #BBDEFC; font-weight: normal;'>Through which dimensions would you like to see these metrics?</text>

* All of the above metrics with the ability to select specific dates for data consultation.
* Evolution of the occupancy rate for the last 6 months.
* Turnover and number of reservations categorized by the customer’s country and how all the metrics are affected by country selection.

<text style='color: #BBDEFC; font-weight: normal;'>What time frame do you need to visualize for the information?</text>

* The longest possible history according to the available data.

<text style='color: #BBDEFC; font-weight: normal;'>At what time unit would you like to see that information?</text>

* Values of all the mentioned metrics according to the selected dates.
* For the evolution of the occupancy rate over the last 6 months, only the available data for that period is used no matter the selected dates in the filter.


### 3.2 Data sources
{style="color: #BBDEFC; font-weight: normal"}

In the second step of the project design, the goal consists of identifying the data sources. How many data sources are available, where are they located, what information is available, which files need to be modified, and so on. In this case, the data provided by the company is contained in a single comma-separated values text file called *hotels.csv*.

This file directly contains the information of two of the metrics required by the client: the number of reservations and the ADR.

### 3.3 Required calculations
{style="color: #BBDEFC; font-weight: normal"}

In the third step, we identify the requirements specified by the management team that are not directly available in the data source. The necessary new information is calculated according to the following table.

{{< figure src="/project4/required_calculations.png" title="Calculation formulas and the corresponding data source fields for each insights." >}}

These calculations will ensure that all necessary metrics are available for the dashboard, providing comprehensive insights for the management team.


### 3.4 Dashboard components
{style="color: #BBDEFC; font-weight: normal"}

In this step, the most appropriate visualizations are chosen for each insight, along with the relevant filters and actions. This information is summarized in the following table.

{{< figure src="/project4/dashboard_components.png" title="Dashboard components selected for each insight." >}}

<text style='color: #BBDEFC; font-weight: normal;'>KPIs band</text>

A band containing all the KPIs is created and located at the top of the dashboard. These are the most valuable metrics, which are used to present the main performance information of the company.

{{< figure src="/project4/kpis_band.png" title="KPIs band used to present the most relevant information." >}}

<text style='color: #BBDEFC; font-weight: normal;'>Occupancy rate evolution in the last 6 months</text>

The occupancy rate evolution in the last 6 months is presented through a line plot and located under the KPIs band. Notice that this dashboard component is not affected by the date slider, since we are presenting the whole information during the 6 most recent months.

{{< figure src="/project4/occupancy_rate_6m.png" title="Component for the occupancy rate evolution in the last 6 months." >}}

<text style='color: #BBDEFC; font-weight: normal;'>Monthly occupancy rate</text>

The seasonality is analysed through the monthly occupancy rate. A component for this metrics is created using a bar plot and located in the left corner under the occupancy rate evolution.

{{< figure src="/project4/monthly_occupancy_rate.png" title="Component for the monthly occupancy rate." >}}

<text style='color: #BBDEFC; font-weight: normal;'>Client adquisition map</text>

Finally, the distribution of the clients is presented in a map. This component is located on the right corner under the occupancy rate evolution and next to the monthly occupancy rate. Notice that this component is also used as a filter for the rest of the performance indicators through an action order.

{{< figure src="/project4/client_adquisition_map.png" title="Component for the client adquisition map." >}}


### 3.5 Dashboard design
{style="color: #BBDEFC; font-weight: normal"}


---

## 4. Dashboard implementation
{style="color: #BBDEFC"}



{{< figure src="/project4/dashboard_desktop.png" title="Dream Resort Hotels Dynamic Dashboard. Desktop version." >}}

{{< figure src="/project4/dashboard_tablet.png" title="Dream Resort Hotels Dynamic Dashboard. Tablet version." >}}

{{< figure src="/project4/dashboard_phone.png" title="Dream Resort Hotels Dynamic Dashboard. Phone version." >}}


