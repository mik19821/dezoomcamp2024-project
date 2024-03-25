<!--multilang v0 en:README.md pl:READMEPL.md -->
<!--multilang buttons-->

language: [English](README.md) also available in:
[Polish](READMEPL.md)

<!--lang:en-->

# DEZoomcamp2024-project

### Data set
Data get from the web site (spcff). This is statistic for HAM operator about Flora&Fauna activation. A set can not be 
download directly so I used python script and MenicalSoup library for web scraping (https://mechanicalsoup.readthedocs.io/en/stable/tutorial.html). 
It's simple to use but I can't share because security reason. Just add 2680 csv files to this repo.

Set structure:
- ID of object (SPFF-DDDD)
- date of activation (YYYYMMDD)
- HAM callsign (SQ7M)
- number of QSO - connection with other operators (integer)