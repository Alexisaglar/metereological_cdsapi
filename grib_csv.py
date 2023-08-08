import xarray as xr
import pandas as pd

# Load xarray dataset from a file
file_path = 'newcastle.grib'
xarray_dataset = xr.open_dataset(file_path)

# Convert xarray dataset to pandas DataFrame
df = xarray_dataset.to_dataframe()

print(df)