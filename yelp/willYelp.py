from rapidconnect import RapidConnect
import openpyxl

keyword  = input("What would you like to search for?: ")
location = input("Where would you like to search?:    ")
filepath = keyword + " " + location + ".xlsx"
wb = openpyxl.Workbook()
sheet = wb.create_sheet("Restaurant Info")
wb.save(filepath)

rapid = RapidConnect("YelpAdSearch", "596c2786-735a-4d60-a0c1-de2f14bc89fa")

token = rapid.call("YelpAPI", "getAccessToken", { 
    "appId": "yP35XZWRfDcx68mImckV4A",
    "appSecret": "IVk0UmWQBM3Rwk1fJqZQ95L2Pr0n8aihQQDFc5qaWNtaVudLXgYpdaK8Ye4gMvpn"
    })

results = rapid.call("YelpAPI", "getBusinesses", { 
    "accessToken": token["access_token"],
    "term": keyword,
    "location": location,
    "latitude": "",
    "longitude": "",
    "radius": "",
    "categories": "",
    "locale": "",
    "limit": "10",
    "offset": "",
    "sortBy": "",
    "price": "",
    "openNow": "",
    "openAt": "",
    "attributes": ""
    })

for result in range(0, len(results['businesses'])):
    sheet['A' + str(result + 1)] = results['businesses'][result]['phone']
    sheet['B' + str(result + 1)] = results['businesses'][result]['name']
    sheet['C' + str(result + 1)] = results['businesses'][result]['location']['display_address'][0] + ", " + results['businesses'][result]['location']['display_address'][1]
    sheet['D' + str(result + 1)] = results['businesses'][result]['url']

wb.save(filepath)
