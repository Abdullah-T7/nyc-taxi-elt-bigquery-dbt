{{ config(materialized='table') }}

select  

    date(pickup_datetime) as trip_date,
    count(*) as total_trips,
    sum(total_amount) as total_revenue

from {{ ref('stg_taxi_trips') }}

group by 1
order by 1
