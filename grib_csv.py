import xarray as xr
import pandas as pd

# Load xarray dataset from a file
file_path = 'download.grib'
xarray_dataset = xr.open_dataset(file_path)

# Convert xarray dataset to pandas DataFrame
df = xarray_dataset.to_dataframe()
df = df.set_index(df['valid_time'])
df = df['t2m']-273.15

print(df)