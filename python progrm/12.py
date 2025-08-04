import requests

WEATHER_TOKEN = '71c7fd59939ea8d8cece773a726acbf7'
weather_url = 'http://api.openweathermap.org/data/2.5/weather'
city = input('Введите название города в котором вы находитеь.')
res = requests.get(url=weather_url, params={'q': city, 'units': 'metric', 'APPID': WEATHER_TOKEN})
data = res.json()
if data.get('cod') != 200:
    print('Такой город не найден! Пожайлуста, попробуйте ещё раз.')
else:
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather_description = data['weather'][0]['description']

    print(f'Температура: {temperature}°C'
          f'\nВлажность: {humidity}%'
          f'\nОписание: {weather_description}')

    if temperature < 0:
        print('Наулице холодно! Наденьте теплую куртку, шапку и перчатки.')
    elif 0 <= temperature < 10:
        print('Наулице прохладно. Оденьте пальто и шарф.')
    elif 10 <= temperature < 20:
        print('Наулице прохладно. Оденьте лёгкую куртку.')
    elif 20 <= temperature < 30:
        print('Наулице тепло. Можно одеть футболку и джинсы.')
    else:
        print('Сегодня жарко! Наденьте легкую одежду.')

    if 'rain' in weather_description:
        print('Возьмите зонтик, возможен дождь!')
    elif 'clear' in weather_description:
        print('Сегодня солнечно!')
    elif 'snow' in weather_description:
        print('Возможно пойдет снег!')
    else:
        print('Погода неплохая.')