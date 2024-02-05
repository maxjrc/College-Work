import requests
resp = requests.post('http://my_textbelt_server/text', {
  'phone': '5555555555',
  'message': 'Hello world',
})
print(resp.json())