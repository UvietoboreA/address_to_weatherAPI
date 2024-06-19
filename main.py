import requests

#COORDINATES API
coordinates_api_key = '662ae3e15602b261278852hfv096bfa'
address = input("Where do you stay?")
coordinates_response = requests.get(url=f'https://geocode.maps.co/search?q={address}&api_key={coordinates_api_key}')
coordinates_response.raise_for_status()
coordinates_data = coordinates_response.json()


#WEATHER API
weather_api_key = 'df0b82324da6a7a0e6e89718f95bc6c9'
lat = coordinates_data[0]['lat']  #9.121200
lon = coordinates_data[0]['lon'] #7.385400   
weather_response = requests.get(url=f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={weather_api_key}')
weather_response.raise_for_status()
weather_data = weather_response.json()

list_of_weathertimes = weather_data['list']

index = 0

while (len(list_of_weathertimes) - 1 >= index):

    weather_type = list_of_weathertimes[index]['weather'][0]['main']
    date = list_of_weathertimes[index]['dt_txt']

    print(f'There will be {weather_type} on {date.split(" ")[0]} by {date.split(" ")[1]}')

    index += 1
    