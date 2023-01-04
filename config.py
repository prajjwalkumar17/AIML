import requests
URL ="https://github.com/prajjwalkumar17/AIML/blob/main/lab1/lab1.md"
res = requests.get(URL).text
start=‘lablabstart’
end=‘lablabend’
print(res.split(start)[1].split(end)[0])
