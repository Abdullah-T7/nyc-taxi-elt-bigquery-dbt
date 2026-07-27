{{ config(materialized='table') }}

select  

    extract(hour from pickup_datetime) as pickup_hour,
    count(*) as total_trips,
    round(avg(trip_distance), 2) as average_distance,
    round(avg(total_amount), 2) as total_revenue

from {{ ref('stg_taxi_trips') }}

group by pickup_hour
order by pickup_hour

