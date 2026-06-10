from pathlib import Path
import requests
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw" / "live_nav"

RAW_DIR.mkdir(
    parents=True,
    exist_ok=True
)


url = "https://api.mfapi.in/mf/125497"

response = requests.get(
    url,
    timeout=30
)

response.raise_for_status()

data = response.json()

df = pd.DataFrame(data["data"])

df.to_csv(
    RAW_DIR / "HDFC_NAV.csv",
    index=False
)


schemes = {
    "SBI":119551,
    "ICICI":120503,
    "NIPPON":118632,
    "AXIS":119092,
    "KOTAK":120841
}

for name,code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(
        url,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame(data["data"])

    df.to_csv(
        RAW_DIR / f"{name}_NAV.csv",
        index=False
    )

    print(f"{name} downloaded")

full_dates = pd.date_range(
    df["date"].min(),
    df["date"].max(),
    freq="D"
)

df = (
    df.set_index("date")
      .reindex(full_dates)
)

df["nav"] = df["nav"].ffill()

