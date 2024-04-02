
CREATE OR REPLACE EXTERNAL TABLE `valued-bastion-411614.spff.spff_ext`
OPTIONS (
  format = 'parquet',
  uris = ['gs://dezoomcamp2024-project/spff_stats/rok=*']
);

CREATE OR REPLACE TABLE `valued-bastion-411614.spff.spff_main` as (select * from `valued-bastion-411614.spff.spff_ext`);
