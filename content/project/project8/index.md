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

{{< figure src="/project8/sw1_task1.png" title="Sprint Week 1. Task 1." >}}

Following the IT Director's advice, we need to import the database provided by the IT team, activate it in the MySQL Workbench environment, and review the content of the main tables. This can be done with the following code:

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

Now we need to check the granularity of the database and identify if any duplicate records exist. To do this, we can use the following SQL query:

```mysql
-- ¿Is it the granularity of the dataset right?
select count(*) as COUNT from sales
group by id_store, id_prod, id_channel, date_time
having COUNT > 1;

-- It seems that some of the records are duplicated, let's investigate that
select id_store, id_prod, id_channel, date_time, count(*) as COUNT from sales
group by id_store, id_prod, id_channel, date_time
having COUNT > 1
order by id_store, id_prod, id_channel, date_time;

-- Some particular cases
select * from sales
where id_store = 1115
  and id_prod = 127110
  and id_channel = 5
  and date_time = '22/12/2016';
```

{{< figure src="/project8/sw1_r1.png" title="Sprint Week 1. Results 1." >}}

It seems the dataset's granularity is incorrect, and some records are duplicated. This could be due to missing fields, such as the time when orders were taken or the number of orders on the same date. To analyze the data properly, we need to fix these issues.

A simple but effective approach is to combine the duplicated records by summing the total amount and considering the average value for the official and offer prices. Here's an example of how to do that:

```mysql
-- We need to create a new table sales_agr with the right granularity, and also:
	-- Change the date_time type 
	-- Create a new field called turnover as the multiplication of amount times offer_price

create table sales_agr as
select str_to_date(date_time, '%d/%m/%Y') as date_time,
	   id_prod, id_store, id_channel,
       sum(amount) as amount,
       avg(official_price) as official_price,
       avg(offer_price) as offer_price,
       sum(amount) * avg(offer_price) as turnover
from sales
group by 1, 2, 3, 4;
```

Now that we have created a new table with the correct granularity and adjusted the *date_time* type, we can move forward with the analysis. The cleaned table will allow for more accurate insights and ensure that the dataset is ready for deeper exploration, such as analyzing sales trends, client behavior, and product performance.



### 3.1 Company requirements
{style="color: #BBDEFC; font-weight: normal"}


