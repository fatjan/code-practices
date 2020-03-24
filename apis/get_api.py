import json
import requests

api_url_base = 'https://jsonmock.hackerrank.com/api/transactions/search?userId='
headers = {'Content-Type': 'application/json'}


def getData(uid, page_num):
    api_url = api_url_base + str(uid) + '&page=' + str(page_num)
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def getExpenditure(userId, locationId, netStart, netEnd):
    # Write your code here
    output = getData(userId, 1)
    print(output)
    total_pages = output['total_pages']
    per_page = output['per_page']
    total = 0
    for i in range(1, total_pages+1):
        data = getData(userId, i)
        searched_data = searchData(data['data'], locationId, netStart, netEnd)
        if len(searched_data) > 0:
            for j in range(len(searched_data)):
                total += searched_data[j]
    print(round(total))

def searchData(data,locationId, netStart, netEnd):
    amounts = []
    for i in range(len(data)):
        ip = data[i]['ip']
        index = ip.index('.')
        pre_ip = int(ip[0:index])
        if data[i]['location']['id'] == locationId and pre_ip >= netStart and pre_ip <= netEnd:
            amount = data[i]['amount']
            amount = amount[1:].replace(',', '')
            amounts.append(float(amount))
    return amounts
         

getExpenditure(2,8,5,50)
