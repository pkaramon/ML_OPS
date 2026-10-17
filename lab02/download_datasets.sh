#!/bin/bash

wget https://opendata.rijdendetreinen.nl/public/services/services-2024.csv.gz -O data/services-2024.csv.gz && \
gzip -f -d data/services-2024.csv.gz
wget https://opendata.rijdendetreinen.nl/public/disruptions/disruptions-2023.csv -O data/disruptions-2023.csv
wget "https://opendata.rijdendetreinen.nl/public/disruptions/disruptions-2024.csv" -O data/disruptions-2024.csv