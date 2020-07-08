import json
import requests
url = "https://covidtracking.com/api/v1/us/current.json"
webdata = requests.get(url)
json_data = json.loads(webdata.text)
#print(json_data)
print('Positive Cases =  ',"{:,}".format(json_data[0]['positive']))
print('Negative Cases = ',"{:,}".format(json_data[0]['negative']))
print('People Currently Hospitalized = ',"{:,}".format(json_data[0]['hospitalizedCurrently']))
print('People Currently  in the ICU = ',"{:,}".format(json_data[0]['inIcuCurrently']))

while True:
    try:
        print('\n\n')
        state = str.lower((input('Enter State Abv >>')))
        state_url = str('https://covidtracking.com/api/v1/states/' + state + '/current.json')
        statedata = requests.get(state_url)
        state_data = json.loads(statedata.text)
        #print(state_data)
    except (TypeError, KeyError):
        print('uhhh ohh..... You did not enter a valid state abbreviation....')

    try:
        print('Positive Cases =  ',"{:,}".format(state_data['positive']))
    except (TypeError, KeyError):
        try:
            print('Positive Cases =  ', (state_data['positive']))
        except (TypeError, KeyError):
            pass

    try:
         print('Negative Cases = ',"{:,}".format(state_data['negative']))
    except (TypeError, KeyError):
        try:
            print('Negative Cases = ',(state_data['negative']))
        except (TypeError, KeyError):
            pass

    try:
        print('People Currently Hospitalized = ',"{:,}".format(state_data['hospitalizedCurrently']))
    except (TypeError, KeyError):
        try:
            print('People Currently Hospitalized = ', (state_data['hospitalizedCurrently']))
        except (TypeError, KeyError):
            pass
    try:
        print('People Currently  in the ICU = ',"{:,}".format(state_data['inIcuCurrently']))
    except (TypeError, KeyError):
        try:
            print('People Currently  in the ICU = ', (state_data['inIcuCurrently']))
        except (TypeError, KeyError):
            pass











