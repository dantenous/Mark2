import urllib, json
import urllib.request
# nactu z api json cenu
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=USD"
json_url = urllib.request.urlopen(url)
data = json.loads(json_url.read())

#napisi hello
print("Hello")
print("Aktualni cena Bitcoinu: ",data["bitcoin"]["usd"])
hist = "https://api.coindesk.com/v1/bpi/historical/close.json?start=2019-08-01&end=2019-09-04"
json_url2 = urllib.request.urlopen(hist)
data2 = json.loads(json_url2.read())

datum = "2019-08-"
for i in range(10, 30):
    print("Mesic 8: ", data2["bpi"]["2019-08-"+str(i)])
for j in range(1, 5):
    print("Mesic 9: ", data2["bpi"]["2019-09-0"+str(j)])

