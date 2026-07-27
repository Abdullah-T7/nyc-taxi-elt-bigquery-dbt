import pandas as pd
from google.cloud import bigquery


client = bigquery.Client.from_service_account_json(
    r"C:\Users\admin\Downloads\taxi-trip-503615-98be2b797bb7.json",
    project="taxi-trip-503615"
)

tabel_id = "taxi-trip-503615.taxi_raw.taxi_trips"

CSV_FILE = '../data/taxi_trip.csv'

chunk_size = 100_000

for i, chunk in enumerate(pd.read_csv(CSV_FILE, chunksize=chunk_size)):

    job = client.load_table_from_dataframe(
        chunk,
        tabel_id,
        job_config=bigquery.LoadJobConfig(
            write_disposition=(
                bigquery.WriteDisposition.WRITE_TRUNCATE
                if i == 0
                else bigquery.WriteDisposition.WRITE_APPEND
            )
        )
    )
    job.result()
    print(f'Uploaded chunk: {i + 1}')



