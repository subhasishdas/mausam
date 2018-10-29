#Token 824e94f0350237ba172dc177f1061d3f4c88525e

import requests

url = 'https://api.vize.ai/v1/classify/'
headers = {'Authorization': "Token 824e94f0350237ba172dc177f1061d3f4c88525e"}
files = {'image_file': open(r'C:\Users\subha\Desktop\car1.jpg', 'rb')}
data = {'task': '12701284-11dd-4800-ab02-a03406ca518b'}

response = requests.post(url, headers=headers, files=files, data=data)
if response.raise_for_status():
    print(response.text)
else:
    print('Successfully posted API: ' + response.text)
