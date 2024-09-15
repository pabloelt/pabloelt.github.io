---
title: Sports Company Database Analysis with SQL
summary: A database analysis is conducted using SQL technology for a sports company. The project is structured in sprint weeks to simulate real-world company operations, where various aspects such as sales, clients, products, and distribution channels are investigated.
tags:
  - SQL
date: 2024-09-12
#external_link: http://github.com
---

{{< toc >}}

## 1. Introduction
{style="color: #BBDEFC"}

The client for this project is a sports company specializing in extreme activities, including modalities like skiing, hiking, climbing, and scuba diving, among others. However, the company's database has not been properly analyzed, leaving many potential insights unexplored. The company seeks to uncover valuable information, particularly related to sales, clients, products, and distribution channels. To achieve this, a plan involving six sprint weeks, managed by the directors of various departments, has been proposed to extract and analyze this critical data.

Notes:

* This article presents a technical explanation of the development process followed in the project.
* Here, you can download the {{< staticref "uploads/project_database.sql" "newtab" >}}database{{< /staticref >}} used in this project.

---

## 2. Objectives
{style="color: #BBDEFC"}

The main objective of this project is to thoroughly analyze the company's database to extract insights and valuable information related to sales, clients, products, and distribution channels. The project is designed to simulate real-world operations, with 6 sprint weeks planned and regular interactions with various departments. The insights gained from this analysis are expected to significantly enhance the company's performance, leading to increased profitability and reduced costs.

This entire project is conducted using **MySQL**, an open-source relational database management system. Specifically, the **MySQL Workbench** IDE (Integrated Development Environment) is used for the database analysis.

---

## 3. Project Results
{style="color: #BBDEFC"}

As mentioned earlier, the project is divided into several sprint weeks, each with specific goals and interactions with various departments of the company. These sprints are designed to address different aspects of the business, such as sales, clients, products, and distribution channels.

The different department directors and their main goals are presented in the image below.

{{< figure src="/project8/departments.png" title="Different department directors that are in charge of the company's performance." >}}

### 3.1 Sprint Week 1
{style="color: #BBDEFC; font-weight: normal"}

In the first sprint week, we have recieved the following email from the IT Director.

{{< figure src="/project8/sw_1.png" title="Sprint Week 1. Task 1." >}}

Following the IT Director's advice, we need to import the database provided by the IT team, activate it in the MySQL Workbench environment, and review the content of the main tables. This can be done with the following code.

```mysql
# SPRINT WEEK 1 - TASK 1
---------------------------------------------

-- Import database from dump: database.sql

-- Activate the database as the default one
use project_database;

-- Review the dataset content in the main four tables
select * from channels;
select * from products;
select * from stores;
select * from sales;
```




For the design of this project, we have followed a straightforward methodology, summarized in the following image. The initial time invested in creating this methodology plan will help us to organize the information properly and to present a more complete and valuable final dashboard. Additionally, this methodology will also help to optimize time and resources in the implementation of the dashboard.

{{< figure src="/project4/methodology.png" title="Summarized methodology followed in the project design of the interactive dashboard." >}}

### 3.1 Company requirements
{style="color: #BBDEFC; font-weight: normal"}


