"""Prepare descriptive event tables from the original SPC catalog."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def main():
    source = ROOT / "data/raw/Table_S1_Derechos_NEXRAD.csv"
    df = pd.read_csv(source)
    events = df.rename(columns={
        "Event #": "event_id",
        "Start Date and Time (UTC)": "start_utc",
        "End Date and Time (UTC)": "end_utc",
        "Start Latitude (Degrees)": "start_lat",
        "Start Longitude (Degrees)": "start_lon",
        "End Latitude (Degrees)": "end_lat",
        "End Longitude (Degrees)": "end_lon",
        "Duration (Hours)": "catalog_duration_hours",
        "Track Length (Kilometers)": "track_length_km",
    })
    for col in ("start_utc", "end_utc"):
        events[col] = pd.to_datetime(events[col], format="%m/%d/%Y %H:%M", utc=True, errors="raise")
    if events.event_id.duplicated().any():
        raise ValueError("Duplicate event IDs need review.")
    events["elapsed_hours"] = (events.end_utc - events.start_utc).dt.total_seconds() / 3600
    if (events.elapsed_hours <= 0).any():
        raise ValueError("Non-positive event duration needs review.")
    events["year"] = events.start_utc.dt.year
    events["month"] = events.start_utc.dt.month
    years = range(int(events.year.min()), int(events.year.max()) + 1)
    annual = events.groupby("year").size().reindex(years, fill_value=0).rename("event_count").reset_index()
    target = ROOT / "data/processed"
    target.mkdir(parents=True, exist_ok=True)
    events.to_csv(target / "events.csv", index=False)
    annual.to_csv(target / "annual_event_counts.csv", index=False)
    print(f"Prepared {len(events)} events; catalog event years {events.year.min()}-{events.year.max()}.")
    print("Trend inference and archive completeness review: not yet complete")

if __name__ == "__main__":
    main()
