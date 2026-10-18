# Data cheat sheet

| Table | Lives in | Source file(s) |
|---|---|---|
| `stations` | DuckDB | `stations-2023-09.csv` |
| `distances` / `distances_long` | DuckDB | `tariff-distances-2022-01.csv` |
| `services` | DuckDB | `services_2019-2025.parquet` (from `services-20??.csv.gz`) |
| `station_connections` | DuckDB | built from `services` + `distances_long` (section 8) |
| `disruptions` | Postgres (`pg.public.disruptions` via ATTACH) | `disruptions-2011.csv` … `disruptions-2023.csv` |

## stations (591 rows)
- `code`: station code, e.g. `ASD` (Amsterdam Centraal). **Join key.**
- `uic`: international station number
- `name_short` / `name_medium` / `name_long`: names
- `slug`: URL name
- `country`: `NL`, `D`, `B`, `F`, `A`, `CH`, `I`, `GB`, ...
- `type`: `megastation`, `knooppuntIntercitystation`, `intercitystation`, `sneltreinstation`, `stoptreinstation`, `facultatiefStation`, ...
- `geo_lat`, `geo_lng`: coordinates

## distances (wide matrix)
- `Station`: origin code; every other column is a destination code
- cell = tariff distance in km, `XXX` on the diagonal
- `distances_long` = UNPIVOT, one row per `(station1, station2, distance)`

## disruptions (one row per disruption)
- `rdt_id`: ID
- `ns_lines`, `rdt_lines`, `rdt_lines_id`: affected lines
- `rdt_station_names`, `rdt_station_codes`: affected stations (comma-separated, empty in old years)
- `cause_nl` / `cause_en`: specific cause
- `statistical_cause_nl` / `statistical_cause_en`: normalised cause, **use for "most common cause"**
- `cause_group`: `infrastructure`, `rolling stock`, `external`, `weather`, `accidents`, `engineering work`, `logistical`, `staff`, `unknown`
- `start_time`, `end_time`, `duration_minutes`
- no service ID, so no direct join to `services`

## services (one row per stop of a service)
- `Service:RDT-ID`: end-to-end service ID, **GROUP BY this for "a service"**
- `Service:Date`
- `Service:Type`: `Sprinter`, `Intercity`, `Stoptrein`, `Sneltrein`, `Intercity direct`, ...
- `Service:Company`: `NS`, `Arriva`, `R-net`, `Blauwnet`, `DB`, `NMBS`, ...
- `Service:Train number`
- `Service:Completely cancelled`, `Service:Partly cancelled`: booleans
- `Service:Maximum delay`: minutes
- `Stop:RDT-ID`: stop row ID
- `Stop:Station code` / `Stop:Station name`: join `code` to `stations.code`
- `Stop:Arrival time`: **NULL = first station**
- `Stop:Departure time`: **NULL = last station**, order by this for `LEAD()`
- `Stop:Arrival delay`, `Stop:Departure delay`: minutes
- `Stop:Arrival cancelled`, `Stop:Departure cancelled`
- `Stop:Platform change`, `Stop:Planned platform`, `Stop:Actual platform`

## Gotchas
- Column names have `:` and spaces, so quote them: `"Service:RDT-ID"`
- `Service:Type` casing varies (`stoptrein` vs `Stoptrein`)
- Disruptions glob: `['data/disruptions-201[1-9].csv', 'data/disruptions-202[0-3].csv']` (skips the lab's 2024 file)
