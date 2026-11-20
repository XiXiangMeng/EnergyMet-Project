# U.S. Derechos and Their Representation in Meteorological Datasets

## Project overview
This Energy Meteorology project examines confirmed U.S. derecho events in the NEXRAD era and investigates how well ERA5 and HRRR-MET represent their wind characteristics. Historical event frequency, duration, and track length provide context for the event comparisons. The motivation is the threat that widespread damaging winds pose to electricity infrastructure.

## Current status
This is an initial project draft. Two SPC archive CSV files have been obtained. The included script checks the event catalog and prepares annual event counts and event-level duration and track-length fields. These summaries are descriptive; they are not evidence of a climate trend by themselves.

- Event catalog preparation script: included and tested on the supplied file.
- Detailed storm-report cleaning and event matching: **not yet complete**.
- ERA5 acquisition and processing: **not yet complete**.
- HRRR-MET acquisition and processing: **not yet complete**.
- Independent station observations: **not yet complete**.
- Matched wind comparisons and uncertainty analysis: **not yet complete**.
- Final figures, interpretation, and conclusions: **not yet complete**.

## Research questions
1. How do event counts, durations, and track lengths vary across the available confirmed-event archive?
2. How well do ERA5 and HRRR-MET reproduce the timing and magnitude of observed winds during selected derechos?

Final hypotheses and event selection: **not yet complete**.

## Repository contents
- `data/raw/`: original uploaded SPC event catalog and storm reports.
- `data/processed/`: generated event and annual summary CSV files.
- `scripts/`: Python analysis code.
- `results/`: reserved for figures and result tables.
- `docs/`: data sources, methods, and remaining work.
- `requirements.txt`: packages required by the current script.

## Data sources
### SPC derecho archive
Source: https://www.spc.noaa.gov/about/derechos/archive/

The supplied NEXRAD event catalog contains 96 events. `Table_S1_Derechos_NEXRAD.csv` contains event start/end times in UTC, endpoint coordinates, duration, and track length. `NEXRAD_Definitive_Derecho_Reports.csv` contains individual wind/damage reports. The original files are included without modification.

Reference: Squitieri, B. J., Wade, A. R., & Jirak, I. L. (2026). On a comprehensive archive for derechos across the contiguous United States. *Bulletin of the American Meteorological Society, 107*(7), E1506–E1535. https://doi.org/10.1175/BAMS-D-25-0002.1

### ERA5
https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels

Access requires a CDS account and acceptance of the dataset licence. Exact dates, region, variables, and download procedure: **not yet complete**.

### HRRR-MET
https://developer.nlr.gov/docs/wind/wind-toolkit/wtk-hrrr-met-toolkit-v1-0-0-download/

The documented API requires an API key and email address. Exact extraction locations and request settings: **not yet complete**.

## Setup and usage
Use Python 3.10 or newer. From the repository root:

```bash
pip install -r requirements.txt
python scripts/01_prepare_catalog.py
```

The script reads the included event catalog and writes `data/processed/events.csv` and `data/processed/annual_event_counts.csv`. Years between the first and last catalog event are retained, including years with zero listed events. The final year's completeness must be checked against archive documentation before trend inference.

Remaining workflow commands: **not yet complete**.

## Planned figures
1. Annual event-count time series: **not yet complete**.
2. Geographic event/report distribution map: **not yet complete**.
3. Matched observed-versus-dataset wind scatterplots: **not yet complete**.

## Limitations
Damage-only reports must not be interpreted as measured zero wind speeds. Estimated and measured winds must be distinguished. Storm reports are not a continuous station time series. Event endpoints do not define an exact track or affected area. Changes in reporting and data coverage require assessment. Mean wind speeds and gusts must not be compared as identical quantities.

Full uncertainty assessment: **not yet complete**.

## AI assistance
ChatGPT assisted with the initial repository structure, documentation, and Python script. Scientific interpretation and final validation: **not yet complete**.
