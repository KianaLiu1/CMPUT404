import requests

x = requests.get('https://raw.githubusercontent.com/KianaLiu1/CMPUT404LAB1/main/versionScript.py')
print(x.text)
