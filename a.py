import ezgmail
import requests


## Weather data

response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=52.518742&lon=13.408022&appid=d9a915424cd7069cd4b1ae8470d3de16&units=metric')
data = response.json()
temperature = data ['main']['temp']
description = data['weather'][0]['description']

##compase email message
message = f'The temperature in Berlin is degrees Celsius and the weather is.'
subject = 'Sodoo is sending weather update from Berlin'


##compase email message
message = f'The temperature in Berlin is {temperature} degrees Celsius and the weather is {description}.'
subject = 'Sodoo is sending weather update from Berlin'


## send the email
ezgmail.send('sodko.beat27@gmail.com', subject, message)

