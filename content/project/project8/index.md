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
* Here, you can download the {{< staticref "uploads/hotels.csv" "newtab" >}}database.csv{{< /staticref >}} used in this project.

---

## 2. Objectives
{style="color: #BBDEFC"}

The main objective of this project is to thoroughly analyze the company's database to extract insights and valuable information related to sales, clients, products, and distribution channels. The project is designed to simulate real-world operations, with 6 sprint weeks planned and regular interactions with various departments. The insights gained from this analysis are expected to significantly enhance the company's performance, leading to increased profitability and reduced costs.

This entire project is conducted using **MySQL**, an open-source relational database management system. Specifically, the **MySQL Workbench** IDE (Integrated Development Environment) is used for the database analysis.

---

## 3. Project Results
{style="color: #BBDEFC"}

As mentioned earlier, the project is divided into several sprint weeks with different goals and interactions with the company's departments. 

```mysql
# SPRINT SEMANA 2 - TAREA 1
---------------------------------------------------------------------------------------------------------------------------------------

-- Importa la bbdd a partir de dump: caso.sql
# Server/Data import/Import from self-contained file -> Start import

-- Activala como la bbdd por defecto
use caso;

-- Revisa el contenido de las 4 tablas
select * from canales;
select * from productos;
select * from tiendas;
select * from ventas;
# Revisado. Parece que los principales id no están con un auto incremento lógico

-- ¿Cuantos registos tiene la tabla ventas?
select count(*) from ventas;
# Tiene 7 registros: id_tienda, id_prod, id_canal, fecha, cantidad, precio_oficial, precio_oferta.altera
# Creo que le faltaría el id_venta. Parece una primary key necesaria

-- Revisa el tipo de los datos, ¿ves algo raro?
# canales/canal -> debería ser varchar()?
# productos -> varchar()?
# tiendas -> varchar()?
# ventas -> fecha-date?

-- ¿Está al nivel que necesitamos? tienda - producto - canal – fecha (no tiene que haber duplicados)
select * from ventas;
# Al fijarnos en la tabla ventas vemos que hay tiendas que han pedido varios productos por el mismo canal y en la misma fecha.
# Vamos a ver si hay duplicados
select id_tienda, id_prod, id_canal, fecha, count(*) as conteo
from ventas
group by id_tienda, id_prod, id_canal, fecha
having conteo > 1;

# Vemos que efectivamente hay algunos registros que están duplicados, quizás por que se hicieron el mismo día pero a diferentes horas.
# Debemos depurar esa información para que la tabla quede en el nivel tienda - producto - canal – fecha, así podríamos darle un id_venta también

-- Si hay duplicados muéstralos para identificar algún caso concreto
select id_tienda, id_prod, id_canal, fecha, count(*) as conteo
from ventas
group by id_tienda, id_prod, id_canal, fecha
having conteo > 1
order by id_tienda, id_prod, id_canal, fecha;


-- Revisa un par de ellos
select * from ventas
where id_tienda = 1115 and id_prod = 127110 and id_canal = 5 and fecha = '22/12/2016';

select * from ventas
where id_tienda = 1132 and id_prod = 92110 and id_canal = 5 and fecha = '10/04/2017';

# Parece ser que el cmapo que está rompiendo el nivel es la cantidad, bien porque se hayan hecho distintos pedidos el mismo día.
# Tenemos que hacer una agregación de los datos.
select id_tienda, id_prod, id_canal, fecha, sum(cantidad) as cantidad, avg(precio_oficial) as precio_oficial, avg(precio_oferta) as precio_oferta from ventas
group by id_tienda, id_prod, id_canal, fecha
order by id_tienda, id_prod, id_canal, fecha;


-- Crea una nueva tabla de ventas_agr agregada a ese nivel, y además:
	-- Cambia la fecha a tipo date 
    -- (pista: usa la función de texto str_to_date con formato '%d/%m/%Y'. Ver: https://www.w3schools.com/sql/func_mysql_str_to_date.asp)
	-- Crea un campo facturación como la multiplicación de la cantidad por el precio_oferta


create table ventas_agr as
select str_to_date(fecha, '%d/%m/%Y') as fecha,
	   id_prod, id_tienda, id_canal, 
	   sum(cantidad) as cantidad,
	   avg(precio_oficial) as precio_oficial,
	   avg(precio_oferta) as precio_oferta,
	   sum(cantidad) * avg(precio_oferta) as facturacion
from ventas
group by 1, 2, 3, 4 # Los ordenamos por columnas en vez de por el nombre para evitar el warning al crear la tabla, debido a la repetición del nombre  
order by 1, 3, 4;


-- Revisa la nueva tabla creada
select * from ventas_agr;

-- Revisa cuantos registros tiene la nueva tabla
select count(*) from ventas_agr;
select count(*) from ventas;
```




For the design of this project, we have followed a straightforward methodology, summarized in the following image. The initial time invested in creating this methodology plan will help us to organize the information properly and to present a more complete and valuable final dashboard. Additionally, this methodology will also help to optimize time and resources in the implementation of the dashboard.

{{< figure src="/project4/methodology.png" title="Summarized methodology followed in the project design of the interactive dashboard." >}}

### 3.1 Company requirements
{style="color: #BBDEFC; font-weight: normal"}


