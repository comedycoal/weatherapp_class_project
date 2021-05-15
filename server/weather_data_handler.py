import json
import datetime

class DateWeatherForecast:
    def __init__(self, date, weatherInfo):
        pass

class City:
    def __init__(self, name):
        pass

class WeatherDataHandler:
    def __init__(self, jsonPath):
        '''
        Create a weather data handler for the weather database

        Parameters:
            jsonPath (str): file path to the database, in json format
        '''
        pass

    def __del__(self):
        pass

    def LoadDatabase(self):
        '''
        Load the database into memory, saves it as an object's member
        '''
        pass

    def FetchAllForecastsByCity(self, cityid):
        pass

    def FetchAllCitiesByDate(self, date):
        pass

    def FetchSevenDayForcastByCity(self, cityid):
        pass

class WeatherDataModifier(WeatherDataHandler):
    def __init__(self, jsonPath):
        pass

    def __del__(self):
        pass
    
    def SaveDatabase(self):
        pass

    def AddCity(self, city:City, id=None):
        pass

    def AddForecastForCity(self, cityid, forecast:DateWeatherForecast): 
        pass

    def AddForcastByValues(self, cityid, weatherInfoTuple):
        pass

    def RemoveForecast(self, cityid, date):
        pass

    def RemoveCity(self, cityid):
        pass