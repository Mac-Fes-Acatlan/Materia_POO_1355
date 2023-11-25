\c postgres;

CREATE TABLE public.TBL_MAINTENANCE
(
  stock_id integer NULL,
  estimate_id integer NULL,
  maintenance_id integer NULL,
  type_id integer NULL,
  package_id integer NULL,
  price_maintenance float NULL
  
);

COPY TBL_MAINTENANCE(

  stock_id ,
  estimate_id ,
  maintenance_id ,
  type_id ,
  package_id ,
  price_maintenance 
  
)
FROM '/home/data/TBL_MAINTENANCE.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE public.TBL_OPERATIONS_MAINTENANCE
(
     mtn_creation_date_id varchar(255) NULL,
     mtn_start_date_id varchar(255) NULL,
     mtn_end_date_id varchar(255) NULL,
     mtn_delivered_date_id varchar(255) NULL, 
     mtn_creation_date varchar(255) NULL,
     mtn_start_date varchar(255) NULL,
     mtn_end_date varchar(255) NULL,
     mtn_delivered_date varchar(255) NULL, 
     maintenance_id integer NULL,
     status_id integer NULL
  
);

COPY TBL_OPERATIONS_MAINTENANCE(

     mtn_creation_date_id ,
     mtn_start_date_id ,
     mtn_end_date_id ,
     mtn_delivered_date_id , 
     mtn_creation_date ,
     mtn_start_date ,
     mtn_end_date ,
     mtn_delivered_date , 
     maintenance_id ,
     status_id  
  
)
FROM '/home/data/TBL_OPERATIONS_MAINTENANCE.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE public.CAT_TYPE_PACKAGE
(
    package_id integer NULL,
    package_name varchar(255) NULL,
    date varchar(255) NULL
  
);

COPY CAT_TYPE_PACKAGE(

    package_id,
    package_name,
    date
  
)
FROM '/home/data/CAT_TYPE_PACKAGE.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE public.CAT_TYPE_STATUS
(
    status_id integer NULL,
    status_name varchar(255) NULL,
    date varchar(255) NULL
  
);

COPY CAT_TYPE_STATUS(

    status_id,
    status_name,
    date
  
)
FROM '/home/data/CAT_TYPE_STATUS.csv'
DELIMITER ','
CSV HEADER;

CREATE TABLE public.CAT_TYPE_MAINTENANCE
(
    type_id integer NULL,
    type_name varchar(255) NULL,
    date varchar(255) NULL
  
);

COPY CAT_TYPE_MAINTENANCE(

    type_id,
    type_name,
    date
  
)
FROM '/home/data/CAT_TYPE_MAINTENANCE.csv'
DELIMITER ','
CSV HEADER;