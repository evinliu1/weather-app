import requests
import PySimpleGUI as sg

# my api for accessing the weather 
user_api = '046ac129c5890d452342dc29c3983bf4'

# layout of my application
layout = [
    [sg.Text('Welcome to the Weather Application')],
    [sg.Input('Seoul',key = '-INPUT_FIELD-'),sg.Button('Go', key='-SEARCH_CITY-'), sg.Button('Exit',key='-CLOSE_BUTTON-')],
    [sg.Text('Display:')],
    [sg.Text('', key='-DATA_FIELD-')]
]

# create the window and attach layout to it
window = sg.Window('Weather App',
            layout,
            grab_anywhere = True,
            keep_on_top = True)

while True:

    # window is keeping track of events and value fields
    event, values = window.read()

    # if user presses exit button
    if event == '-CLOSE_BUTTON-':
        break

    # if user presses 'go' button
    if event == '-SEARCH_CITY-':
        location = values['-INPUT_FIELD-']
        request_link = 'https://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid='+ user_api
        api = requests.get(request_link)
        api_data = api.json()

        # if city name is invalid
        if api_data['cod'] == '404':
            values['-DATA_FIELD-'] = 'Something seems wrong. Please be sure you entered a valid city name'
        else:
            # initializing variables with weather information
            temp = (
                round(((api_data['main']['temp']) - 273) * 9/5 + 32)
            )
            description = api_data['weather'][0]['description']
            humidity = api_data['main']['humidity']
            wind_speed = api_data['wind']['speed']
            # this is what will be displayed
            update = '''
            Temperature: ''' + str(temp) + '''\n
            Description: ''' + description + '''\n
            Humidity ''' + str(humidity) + '''\n
            Wind Speed: ''' + str(wind_speed) + '\n'

            window['-DATA_FIELD-'].update(update)

window.close()
