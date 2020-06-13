import requests
client_id = "3AGUl0mf3eS0uNtREeDP"
client_secret = "ZbZ0Iu7ovD"
url = "https://openapi.naver.com/v1/vision/celebrity"
files = {'image': open('./PO.jpg', 'rb')}
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }



response = requests.post(url, files=files, headers=headers)
print("lkl", response)

rescode = response.status_code
if(rescode==200):
    print(response.text)
else:
    print("Error Code:" + rescode)