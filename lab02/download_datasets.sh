#!/bin/bash

mkdir -p data

# lab

wget https://opendata.rijdendetreinen.nl/public/services/services-2024.csv.gz -O data/services-2024.csv.gz && \
gzip -f -d data/services-2024.csv.gz
wget https://opendata.rijdendetreinen.nl/public/disruptions/disruptions-2023.csv -O data/disruptions-2023.csv
wget "https://opendata.rijdendetreinen.nl/public/disruptions/disruptions-2024.csv" -O data/disruptions-2024.csv

# homework

wget -nc https://opendata.rijdendetreinen.nl/public/tariff-distances/tariff-distances-2022-01.csv -P data
wget -nc https://opendata.rijdendetreinen.nl/public/stations/stations-2023-09.csv -P data

for year in $(seq 2011 2023); do
  wget -nc https://opendata.rijdendetreinen.nl/public/disruptions/disruptions-$year.csv -P data
done

for year in $(seq 2019 2025); do
  wget -nc https://opendata.rijdendetreinen.nl/public/services/services-$year.csv.gz -P data
done
