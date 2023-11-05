from app.models import *
import json


def cleaning_dataset():
    dataset_raw = DatasetRaw.objects.all()
    df = dataset_raw.to_dataframe(fieldnames=['id', 'year', 'month', 'carrier__carrier_name', 'airport__airport_name', 'arr_flights', 'arr_del15', 'carrier_ct', 'weather_ct', 'nas_ct', 'security_ct', 'late_aircraft_ct', 'arr_cancelled', 'arr_diverted', 'arr_delay', 'carrier_delay', 'weather_delay', 'nas_delay', 'security_delay', 'late_aircraft_delay'])
    df_null = df[df.isna().any(axis=1)]
    df_non_null =df.dropna(axis=0, how='any', inplace=False)
    df_duplicate = df_non_null[df_non_null.duplicated()]
    df_clean = df_non_null[~df_non_null.duplicated()]
    dataset_null_json = json.loads(df_null.to_json(orient="records"))
    dataset_duplicate_json = json.loads(df_duplicate.to_json(orient="records"))
    dataset_clean_json = json.loads(df_clean.to_json(orient="records"))

    success = 1
    context = {
        "dataset_null": dataset_null_json,
        "dataset_duplicate": dataset_duplicate_json,
        "dataset_clean": dataset_clean_json,
        'success': success
    }

    return context