import xarray as xr
import matplotlib.pyplot as plt

# Specify the path to your GRIB file
grib_file_path = "download.grib"

# Open the GRIB file using xarray
ds = xr.open_dataset(grib_file_path, engine="cfgrib")

# Define the latitude and longitude range for the specific area
lat_range = slice(50, 60)  # For example, between 30 and 40 degrees latitude
lon_range = slice(-20, -30)  # For example, between -20 and -10 degrees longitude

# Extract temperature data for the specific area
temperature_data = ds.t2m.sel(latitude=lat_range, longitude=lon_range)

# Print the temperature data for the specific area
print("Temperature Data for the Specific Area:")
print(temperature_data)

# Create a plot
plt.figure(figsize=(10, 6))
temperature_data.plot()
plt.title("Temperature in Specific Area")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.grid()
plt.show()

# Close the xarray dataset
ds.close()