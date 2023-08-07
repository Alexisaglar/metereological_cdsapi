import cdsapi

copernicus = cdsapi.Client()
latitude = "56"
longitude = "-1.6"
altitude = "-999." #default as mentioned in lib
date_period = '2023-01-01/2023-01-02'
resolution = "1minute"


def retrieve_data(latitude, longitude, altitude, date_period, resolution, name):
    copernicus.retrieve(
        'cams-solar-radiation-timeseries',
        {
            'location': {
                'latitude': latitude,
                'longitude': longitude,
            },
            'altitude': altitude,
            'date': date_period,
            'sky_type': 'observed_cloud',
            'time_step': resolution,
            'time_reference': 'universal_time',
            'format': 'csv',
        },
        f'{name}.csv'),
    
    copernicus.retrieve('reanalysis-era5-pressure-levels', {
            "location": {
                'latitude': latitude,
                'longitude': longitude,
            },
           "variable": "temperature",
           "pressure_level": "1000",
           "product_type": "reanalysis",
           "date": date_period,
           "format": "csv"
       }, 'f{name}_temp.csv')

    
retrieve_data(latitude, longitude, altitude, date_period, resolution, "Newcastle_data_1_min_January")