import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
from datetime import datetime
import os  
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


os.environ['GOOGLE_APPLICATION_CREDENTIAL'] = "/home/src/personal-gcp.json/valued-bastion-411614-99b5bae0865e.json"
bucket_name = 'dezoomcamp2024-project''
project_id = 'valued-bastion-411614'

table_name = 'spff_stats'

root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):
    # Przekształć datę w formacie tekstowym na obiekt datetime
    # date_object = datetime.strptime(data['dzien'], '%Y-%m-%d')
    # data_object = str(data_object)
    # data['rok'] = date_object.year

    table = pa.Table.from_pandas(data)
    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['znak'],
        filesystem=gcs
    )
    


