# Methods

## Implemented preparation
The event catalog is read without modifying the original CSV. Times are parsed in UTC. Annual counts use the event start year. Published duration and timestamp-derived duration are retained separately.

## Detailed reports
Cleaning: **not yet complete**.
The report file requires a compatible encoding such as cp1252. It contains missing values and damage-only records. Zero-valued speeds on damage-only records must not be treated as calm winds. Event assignment must check overlapping time windows and location; time alone may be ambiguous.

## Model and observation comparison
Time alignment, spatial matching, wind-height consistency, gust versus mean wind, and validation metrics: **not yet complete**.

## Trend assessment
Coverage review, reporting changes, statistical tests, and uncertainty: **not yet complete**.
