import json
import cdsapi

#variables for position and resolution of data
latitude = "56"
longitude = "-1.6"
altitude = "-999." #default as mentioned in lib
date_period = '2023-01-01/2023-01-02'
resolution = "1minute"

def get_database_info(database):
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        return config.get(database, None)

# Example usage
database_irradiation, database_temperature = "irradiation", "temperature"
db_irradiation_info, db_temperature_info = get_database_info(database_irradiation), get_database_info(database_temperature)

url_irradiation, url_temperature = db_irradiation_info.get('url'), db_temperature_info.get('url')
api_key_irradiation, api_key_temperature = db_irradiation_info.get('api_key'), db_temperature_info.get('api_key')

c = cdsapi.Client(url=url_temperature, key=api_key_temperature)
c.retrieve(
    'reanalysis-era5-land',
    {
        'variable': '2m_temperature',
        'year': '2022',
        'month': '01',
        'day': [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
        ],
        'time': [
            '00:00', '01:00', '02:00',
            '03:00', '04:00', '05:00',
            '06:00', '07:00', '08:00',
            '09:00', '10:00', '11:00',
            '12:00', '13:00', '14:00',
            '15:00', '16:00', '17:00',
            '18:00', '19:00', '20:00',
            '21:00', '22:00', '23:00',
        ],
        'area': [
            54.98, -1.62, 54.96,
            -1.58,
        ],
        'format': 'grib',
    },
    'temperature.grib')

c = cdsapi.Client(url=url_irradiation, key=api_key_irradiation)
c.retrieve(
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
        'irradiation.csv'),
