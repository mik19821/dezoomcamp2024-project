import pyarrow as pa 
import pyarrow.parquet as pq
from datetime import datetime
import pandas as pd
import os


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/personal-gcp.json/k.json'
bucket_name = 'zoomcamp24'
project_id = 'valon-4114'
table_name = 'spff_stats'

root_path = f'{bucket_name}/{table_name}'
@data_exporter
def export_data(data, *args, **kwargs):
    table = pa.Table.from_pandas(data)
    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['rok'],
        filesystem=gcs
    )