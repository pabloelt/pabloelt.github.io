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
* You can also download the {{< staticref "uploads/project_database.sql" "newtab" >}}database{{< /staticref >}} used in this project.

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

<text style='color: #BBDEFC; font-weight: normal;'>Task 1</text>

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

A simple but effective approach is to combine the duplicated records by summing the total amount and considering the average value for the official and offer prices. In addition, a new field for turnover is created, calculated by multiplying the total amount by the average offer price for each record. Here, you can see an example of how to do that:

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
  round(sum(amount) * avg(offer_price),2) as turnover
from sales
group by 1, 2, 3, 4;
```

Now that we have created a new table with the correct granularity and adjusted the *date_time* type, we can move forward with the analysis. The cleaned table will allow for more accurate insights and ensure that the dataset is ready for deeper exploration, such as analyzing sales trends, client behavior, and product performance.

{{< figure src="/project8/sw1_r2.png" title="Sprint Week 1. Results 2." >}}

<text style='color: #BBDEFC; font-weight: normal;'>Task 2</text>

After completing the first task we recieved a new email from the IT Director.

{{< figure src="/project8/sw1_task2.png" title="Sprint Week 1. Task 2." >}}

It seems that the new created table *sales_agr* is still not properly connected with the rest of the tables. We need to fix that:

```mysql
# SPRINT WEEK 1 - TASK 2
---------------------------------------------
-- The new sales_agr table is not connected with the rest of the tables. We need
 --  to include a new key field called id_sale
 --  id_prod as a FK with the corresponding table
 --  id_store as a FK with the corresponding table
 --  id_channel as a FK with the corresponding table
alter table sales_agr add id_sale int auto_increment primary key,
                      add foreign key(id_prod) references products (id_prod) on delete cascade,
                      add foreign key(id_store) references stores (id_store) on delete cascade,
                      add foreign key(id_channel) references channels (id_channel) on delete cascade;
```

The resultant Entity-Relationship (ER) Diagram can be seen in the image below.

{{< figure src="/project8/sw1_r3.png" title="Sprint Week 1. Results 3." >}}

We can now proceed with order identification as suggested by the IT Director. To do this, we will define an order as all the products purchased by the same store, through the same channel, on the same date. It can be accomplish with the following code:

```mysql
-- Create a view over sales_agr that includes the order id
create view v_sales_agr_order as 
with master_orders as (
  select date_time, id_store, id_channel, row_number() over() as id_order
  from sales_agr
  group by date_time, id_store, id_channel)
select id_sale, id_order, s.date_time, s.id_prod, s.id_store, s.id_channel, amount, official_price, offer_price, turnover 
from sales_agr as s
  left join master_orders as m
  on (s.date_time = m.date_time) and (s.id_store = m.id_store) and (s.id_channel = m.id_channel);
    
select * from v_sales_agr_order;
```

{{< figure src="/project8/sw1_r4.png" title="Sprint Week 1. Results 4." >}}


### 3.2 Sprint Week 2
{style="color: #BBDEFC; font-weight: normal"}

<text style='color: #BBDEFC; font-weight: normal;'>Task 1</text>

At the beginning of the second sprint week we received an email from the Strategy Director with some general questions.

{{< figure src="/project8/sw2_task1.png" title="Sprint Week 2. Task 1." >}}

These general questions about the order, dates, products, stores, and channels can be easily solved with the following querys:

```mysql
# SPRINT WEEK 2 - TASK 1
---------------------------------------------

-- How many orders do we have in the historical data?
select max(id_order) from v_sales_agr_order;

-- From which day do we have data?
select min(date_time) as first_day, max(date_time) as last_day from sales_agr;

-- How many different products do we have in our catalog?
select count(distinct id_prod) as num_prod from products;

-- How many different stores do we distribute to?
select count(distinct id_store) as num_store from stores;

-- Through which channels can orders be placed with us?
select distinct channel from channels;
```

Through these queries, we have discovered some new insights. There are 22721 orders in the company's historical data. Our records span from 2015-01-12 to 2018-07-20. We have 274 different products in our catalog and work with 562 different stores to distribute our products. The available channels for placing orders include: Fax, Telephone, Mail, E-mail, Web, Sales visits, Special, and Other.

<text style='color: #BBDEFC; font-weight: normal;'>Task 2</text>

We've received a new email from the Marketing Director requesting more detailed information about the channel dimension. Additionally, data on client performance is also required at this stage.

{{< figure src="/project8/sw2_task2.png" title="Sprint Week 2. Task 2." >}}

These questions can be solved with the following querys:

```mysql
# SPRINT WEEK 2 - TASK 2
---------------------------------------------

-- What are the top 3 channels with the highest turnover?
select channel, round(sum(turnover),2) as turnover_channel
from sales_agr as s
  left join channels as c
  on s.id_channel = c.id_channel
group  by s.id_channel
order by turnover_channel desc
limit 3;
```

{{< figure src="/project8/sw2_r1.png" title="Sprint Week 2. Results 1." >}}


```mysql
-- What is the monthly turnover trend per channel over the last 12 full months?
select channel, month(date_time) as month, round(sum(turnover),2) as turnover_channel
from sales_agr as s
  left join channels as c
  on s.id_channel = c.id_channel
where date_time between '2017-07-01' and '2018-06-30'
group by s.id_channel, month
order by s.id_channel, month;
```

{{< figure src="/project8/sw2_r2.png" title="Sprint Week 2. Results 2." >}}

```mysql
-- What are the top 50 clients (stores with highest turnover)?
select store_name, round(sum(turnover),2) as turnover_store
from sales_agr as s
  left join stores as st
  on s.id_store = st.id_store
group by s.id_store
order by turnover_store desc
limit 50;
```

{{< figure src="/project8/sw2_r3.png" title="Sprint Week 2. Results 3." >}}

```mysql
-- Turnover trend by country per term since 2017.	
select country, year(date_time) as year, quarter(date_time) as quarter, round(sum(turnover),2) as turnover_quarter
from sales_agr as s
  left join stores as st
  on s.id_store = st.id_store
where date_time between '2017-01-01' and '2018-06-30'
group by country, year, quarter
order by country, year, quarter;
```

{{< figure src="/project8/sw2_r4.png" title="Sprint Week 2. Results 4." >}}


### 3.3 Sprint Week 3
{style="color: #BBDEFC; font-weight: normal"}

<text style='color: #BBDEFC; font-weight: normal;'>Task 1</text>

In the thrid sprint week, we have received the next email from the Financial Director.

{{< figure src="/project8/sw3_task1.png" title="Sprint Week 3. Task 1." >}}

To identify the products with the highest margins for each product line, we first need to define what we mean by margin. For this project, it will be considered as the net profit in percantage, which is:

{{< math >}}
$$
\textup{Margin}[\%] = \frac{\textup{Price} - \textup{Cost}}{\textup{Cost}} \cdot 100.
$$
{{< /math >}}

In addition, to separate the margin for each product line, we need to use what are called **window functions**. Specifically, we need to create a ranking partitioned by the product line. Additionally, a **common table expression** (CTE) and a **subquery** are required to properly access the ranking and the margin variables created. This can be achieved with the following code:

```mysql
-- Find the top 20 products with higer margins for each line
with table_margin as(
  select *, round((price-cost)/cost*100, 2) as margin
  from products)
select *
from (select id_prod, line, product, margin, row_number() over(partition by line order by margin desc) as ranking
      from table_margin) as subquery_ranking
where ranking <= 20;
```

{{< figure src="/project8/sw3_r1.png" title="Sprint Week 3. Results 1." >}}

On the other hand, to identify products with excessive discounts, we will consider that a product's discount should not exceed the value that falls below the 90% of all discounts. This means that in the discount distribution, the maximum allowable discount corresponds to the value at the 90th percentile of that distribution. Discounts are defined as follows:

{{< math >}}
$$
\textup{Discount}[\%] = \frac{\textup{Price}_{\textup{official}} - \textup{Price}_{\textup{offer}}}{\textup{Price}_{\textup{official}}} \cdot 100,
$$
{{< /math >}}

where the official and offer prices first need to be averaged for each product line. We can solve this query with the following code:

```mysql
-- Find those products (id_prod) with discounts that exceed the value that falls below the 90% of all discounts
with table_discount as(
  select *, (official_price_avg - offer_price_avg) / official_price_avg as discount
  from(select id_prod, avg(official_price) as official_price_avg, avg(offer_price) as offer_price_avg
       from sales_agr
       group by id_prod) as subquery_avg_price)
select *
from (select id_prod, round(discount*100, 2) as discount, round(cume_dist() over(order by discount), 5) as discount_dist
      from table_discount) as subquery_dist
where discount_dist >= 0.9;
```

{{< figure src="/project8/sw3_r2.png" title="Sprint Week 3. Results 2." >}}


<text style='color: #BBDEFC; font-weight: normal;'>Task 2</text>

We’ve received a new email from the Financial Director requesting more information about the company's product portfolio and how many products can be eliminated while still maintaining at least 90% of the company's turnover.

{{< figure src="/project8/sw3_task2.png" title="Sprint Week 3. Task 2." >}}


The approach for solving product selection is as follows: first, we need to order the products by turnover. Once this is done, we calculate the total turnover, allowing us to determine the cumulative percentage each product contributes to the total revenue. Finally, we select the products that account for up to 90% of the total turnover.

```mysql
# SPRINT WEEK 3 - TASK 2
---------------------------------------------

-- How many products are we selling?
select count(distinct product) from products; #144 different products
select count(distinct id_prod) from products; #274 different products (color distinction)

-- Which products would we need to keep to maintain 90% of the current turnover?
with table_turnover_prod_cum_per as(
  select id_prod,
         round(sum(turnover_prod) over(order by turnover_prod desc), 2) as turnover_prod_cum,
         round(sum(turnover_prod) over(), 2) as turnover_prod_total,
         round(sum(turnover_prod) over(order by turnover_prod desc)/sum(turnover_prod) over(), 4) as turnover_prod_cum_per
  from (select id_prod, sum(turnover) as turnover_prod
        from sales_agr
        group by id_prod
        order by turnover_prod desc) as subquery_turnover_prod)
select id_prod, turnover_prod_cum, turnover_prod_cum_per
from table_turnover_prod_cum_per
where turnover_prod_cum_per <= 0.9;

-- And therefore, which specific products could we eliminate and still maintain 90% of the revenue?
with table_turnover_prod_cum_per as(
  select id_prod,
         round(sum(turnover_prod) over(order by turnover_prod desc), 2) as turnover_prod_cum,
         round(sum(turnover_prod) over(), 2) as turnover_prod_total,
         round(sum(turnover_prod) over(order by turnover_prod desc)/sum(turnover_prod) over(), 4) as turnover_prod_cum_per
  from (select id_prod, sum(turnover) as turnover_prod
        from sales_agr
        group by id_prod
        order by turnover_prod desc) as subquery_turnover_prod)
select id_prod, turnover_prod_cum, turnover_prod_cum_per
from table_turnover_prod_cum_per
where turnover_prod_cum_per > 0.9;
```

{{< figure src="/project8/sw3_r3.png" title="Sprint Week 3. Results 3." >}}

<text style='color: #BBDEFC; font-weight: normal;'>Task 3</text>

At the end of the third sprint week, we received another email from the Marketing Director.

{{< figure src="/project8/sw3_task3.png" title="Sprint Week 3. Task 3." >}}

She is concerned about the various product lines and how we can reduce costs in that area without significantly impacting the company’s overall turnover. Additionally, we need to identify which products are trending. In this context, we will define a trend as the product’s performance over the last two terms, comparing the evolution between the first and second terms of 2018.

```mysql
# SPRINT WEEK 3 - TASK 3
---------------------------------------------

-- What different product lines are we selling?
select distinct line from products;

-- What is the contribution (in percentage) of each line to the total turnover?
with table_turnover_line as(
  select line, round(sum(turnover), 2) as turnover_line
  from sales_agr as s
    left join products as p
    on s.id_prod = p.id_prod
  group by line
  order by turnover_line desc)
select line, turnover_line, round(turnover_line / sum(turnover_line) over(), 2) as turnover_line_per
from table_turnover_line;
```

{{< figure src="/project8/sw3_r4.png" title="Sprint Week 3. Results 4." >}}

The outdoor protection line accounts for only 1% of the overall turnover, so eliminating this product line should be considered.

---