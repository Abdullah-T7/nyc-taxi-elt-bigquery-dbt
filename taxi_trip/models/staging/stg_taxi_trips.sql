select 

VendorID as vendor_id,

CAST(tpep_pickup_datetime as timestamp) as pickup_datetime,
CAST(tpep_dropoff_datetime as timestamp) as dropoff_datetime,

passenger_count,
trip_distance,
fare_amount,
tip_amount,
total_amount

from {{source('taxi_raw', 'taxi_trips')}}



