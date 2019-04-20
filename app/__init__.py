from lxml import html
from flask import Flask
from flask import jsonify
import json
import requests
#from lxml import html
import csv
from bs4 import BeautifulSoup


app = Flask(__name__)


def getCountryScores(country):
	labourTypes = getDOLCountryData(country)
	fatalityRate = getILOFatalityPercentData(country)
	epiScore = getEPIScore(country)
	
	fatalityRate = float(fatalityRate)
	epiScore = float(epiScore)
	
	overall = epiScore - fatalityRate
	if (labourTypes != []):
		overall -= 10
	
	scores = [overall, epiScore, fatalityRate, labourTypes]
	
	#print (scores)
	
	return scores
	

def getDOLCountryData(country):
	web = requests.get('https://www.dol.gov/agencies/ilab/reports/child-labor/list-of-goods?items_per_page=All&combine=')
	page = html.fromstring(web.content)
	
	data = []
	
	countries = page.xpath('//div[@class="table-responsive"]/table/tbody/tr')
	
	for elem in countries:
		name_data = elem.xpath('./td[@class="views-field views-field-name-1"]/a')
		if name_data == []:
			name_data = elem.xpath('./td[@class="views-field views-field-name-1"]')
		
		product_data = elem.xpath('./td[@class="views-field views-field-name"]')
		labor_data = elem.xpath('./td[@class="views-field views-field-field-exploitation-type-group"]')
		
		name = name_data[0].text.strip()
		product = product_data[0].text.strip()
		labor = labor_data[0].text.strip()
		if (name == country):
			data.append((product, labor))
	
	return 1 if data != 0 else 0

def getILOFatalityPercentData(country):
	data = 0
	country = "United States" if country == "United States of America" else country

	with open('ILOSTAT_.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		found = False
		for row in csv_reader:
			if (row[3] == country):
				if (row[8] == 'SEX_T' and row[11] == 'Status: Total'):
					data = row[21]
					found = True
			elif (found):
				return data
		
	return 0
					
def getEPIScore(country):
	with open('EPI_DATA.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		columns = True
		for row in csv_reader:
			if (row[2] == country):
				return row[10]
				
	return "0"

def test_data_JSON():
    API_RETURN = {
    "products": [
        {
            "barcode_number": "819898011094",
            "barcode_type": "UPC",
            "barcode_formats": "UPC 819898011094, EAN 0819898011094",
            "mpn": "Spk-120952",
            "model": "",
            "asin": "",
            "product_name": "Soda popeeee",
            "title": "",
            "category": "Food, Beverages & Tobacco > Food Items > Bakery > Fudge",
            "manufacturer": "The Coca-Cola Company",
            "brand": "",
            "label": "",
            "author": "",
            "publisher": "",
            "artist": "",
            "actor": "",
            "director": "",
            "studio": "",
            "genre": "",
            "audience_rating": "",
            "ingredients": "Unbleached Wheat Flour. Fudge Coating (sugar, Palm Kernel Oil, Coca, Cocoa Processed With Alkali {dutched}, Palm Oil, Whey {from Milk}, Soy Lecithin, Natural Flavor), Palm Oil, Cane Sugar, Cane Sugar Invert Syrup, Sea Salt, Baking Soda, Soy Lecithin, Sugar, Natural Flavor.",
            "nutrition_facts": "Energy 516 kcal, Protein 3.23 g, Total lipid (fat) 25.81 g, Carbohydrate, by difference 67.74 g, Fiber, total dietary 3.2 g, Sugars, total 32.26 g, Calcium, Ca 0 mg, Iron, Fe 3.75 mg, Potassium, K 177 mg, Sodium, Na 403 mg, Vitamin C, total ascorbic acid 0.0 mg, Vitamin A, IU 0 IU, Fatty acids, total saturated 14.520 g, Fatty acids, total monounsaturated 6.450 g, Fatty acids, total polyunsaturated 1.610 g, Fatty acids, total trans 0.000 g, Cholesterol 0 mg",
            "color": "",
            "format": "",
            "package_quantity": "",
            "size": "",
            "length": "",
            "width": "",
            "height": "",
            "weight": "",
            "release_date": "",
            "description": "<b>Features</b><ul><li>Welcome to the mouthwatering combination of rich fudge and the light crunch of shortbread.</li><li>What a tasty surprise.</li><li>Capacity - 8.5 oz.</li><li>Pack of 6.</li></ul>",
            "features": [],
            "images": [
                "https://images.barcodelookup.com/1618/16188638-1.jpg"
            ],
            "stores": [
                {
                    "store_name": "Wal-Mart.com USA, LLC",
                    "store_price": "4.85",
                    "product_url": "http://www.walmart.com/ip/Back-to-Nature-Cookies-Fudge-Striped-8-5-OZ/42713187",
                    "currency_code": "USD",
                    "currency_symbol": "$"
                },
                {
                    "store_name": "Jet.com",
                    "store_price": "5.80",
                    "product_url": "https://jet.com/product/Back-to-Nature-Fudge-Stripe-Shortbread-Cookie-85-oz/da702767dc63463786d2e65275440b11",
                    "currency_code": "USD",
                    "currency_symbol": "$"
                },
                {
                    "store_name": "Newegg.com",
                    "store_price": "41.32",
                    "product_url": "https://www.newegg.com/Product/Product.aspx?Item=9SIA62V4074205&nm_mc=AFC-C8Junction-MKPL&cm_mmc=AFC-C8Junction-MKPL-_-HW+-+Vitamins++Minerals+++Supplements-_-KeHE+Distributors-_-9SIA62V4074205",
                    "currency_code": "USD",
                    "currency_symbol": "$"
                },
                {
                    "store_name": "UnbeatableSale.com",
                    "store_price": "41.22",
                    "product_url": "http://www.gourmet-foodshop.com/rtl96594.html",
                    "currency_code": "USD",
                    "currency_symbol": "$"
                },
                {
                    "store_name": "Rakuten.com",
                    "store_price": "41.22",
                    "product_url": "https://www.rakuten.com/shop/unbeatablesale/product/RTL96594/?sku=RTL96594?scid=af_feed",
                    "currency_code": "USD",
                    "currency_symbol": "$"
                },
                {
                    "store_name": "Newegg Business",
                    "store_price": "44.03",
                    "product_url": "https://www.neweggbusiness.com/Product/Product.aspx?Item=9SIV19P7EM0387&nm_mc=afc-cjb2b&cm_mmc=afc-cjb2b-_-HW+-+Vitamins++Minerals+++Supplements-_-Back+To+Nature-_-9SIV19P7EM0387",
                    "currency_code": "USD",
                    "currency_symbol": "$"
                }
            ],
            "reviews": []
        }
    ]}

    class response:
        text = ""

    response.text = json.dumps(API_RETURN)

    return(response.text)

#accept barcode and return product name
def barcode_To_Product_Name(barcode):

    url = "https://api.barcodelookup.com/v2/products"

    querystring = {"barcode":barcode,"key":"m6jo0kxl0vbgmvxcoremm2a3e00web"}

    payload = "{\n\t\"testGreeting\": \"hello\"\n}"
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
    }

  
    
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    print(response.text)
    #product_data_object = json.loads(test_data_JSON())

    if(response.status_code == 404):
        print("NO Response")
        return("NULL")
    else:
        product_data_object = json.loads(response.text)
        product_name = product_data_object['products'][0]['manufacturer']
        return(product_name)


    

    #remove when using API 
    #return(test_function())


def getNewsWeekScore(company_name):
    url = "https://www.newsweek.com/top-500-global-companies-green-rankings-2017-18"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    req = requests.get(url, headers=headers)
    the_page = req.text
    odd = []
    even = []
    soup = BeautifulSoup(the_page,features="lxml")
    odd = soup.find_all('tr',attrs={'class':'odd'})

    for company in odd:
        company_odd = company.find('td',attrs={'class':'col3 rank-company'})
        if (isSameCompany(company_odd.find('a').text, company_name)):
            score = company.find('td',attrs={'class':'col2 rank-newsweek-green-score'}).text
            #gics = company.find('td',attrs={'class':'col5 rank-gics-sector'}).text
            return score
    even = soup.find_all('tr',attrs={'class':'even'})
    for company in even:
        company_even = company.find('td',attrs={'class':'col3 rank-company'})
        if (isSameCompany(company_even.find('a').text, company_name)):
            score = company.find('td',attrs={'class':'col2 rank-newsweek-green-score'}).text
            #gics = company.find('td',attrs={'class':'col5 rank-gics-sector'}).text
            return score
        
    return "NULL"

def isSameCompany(c1, c2):
    c1 = c1.lower()
    c2 = c2.lower()
    if (c1 == c2):
        return True

    c1 = c1.replace('.', '')
    c1 = c1.replace(',', '')
    c2 = c2.replace('.', '')
    c2 = c2.replace(',', '')

    if (c1 == c2):
        return True
	
    c1 = c1.split(' ')
    c2 = c2.split(' ')
	
    c1Re = ''
    c2Re = ''
	
    for word in c1:
        if (word == "inc" or word == "corp" or word == "the" or word == "ltd" or word == "limited" or word == "company" or word == "corporation" or word == "co" or word == "llc" or word == "plc"):
            continue
        else:
            c1Re += word

    for word in c2:
        if (word == "inc" or word == "corp" or word == "the" or word == "ltd" or word == "limited" or word == "company" or word == "corporation" or word == "co" or word == "llc" or word == "plc"):
            continue
        else:
            c2Re += word
            
    if (c1Re == c2Re):
        return True
    else:
        return False

def getIVAData(company):
    data = []
    with open('iva_factors.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            if (isSameCompany(company, row[0])):
                data.append(row[11])#Weighted Industry score
                data.append(row[13])#Environmental score
                data.append(row[14])#Environmental weight
                data.append(row[15])#Social score
                data.append(row[16])#Social weight
                data.append(row[17])#Governance score
                data.append(row[18])#Governance weight
                return data
    return "NULL"

def getCountryOfOrigin(company):
    with open('company_info.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            if (isSameCompany(company, row[1])):
                return row[3]
    return "NULL"
             
def getCompanyScores(company_name):
    score = getNewsWeekScore(company_name)
    score = score[0:len(score) - 1]
    data = getIVAData(company_name)
    if (data == "NULL"):
        toReturn = [0, 0, 0, 0]
    else:
        toReturn = [score, data[1], data[3], data[5]]
    return toReturn


@app.route("/product_name")
def product_name():
    return test_function()

@app.route("/productInfo/<string:name>")
def productInfo(name):
    
    productInfo = {
        "barcode":"NULL",
        "product_name":"NULL",
        "country":"NULL",
        "DOLdata":0,
        "ILOFatalityPercentage":0,
        "EPIScore":0,
        "carterScores":[0,0,0,0],
        "laborScore":0,
        "environmentScore":0

    }

    productInfo["barcode"] = name 
    #Get name of product
    productInfo["product_name"] = barcode_To_Product_Name(productInfo["barcode"])

    productInfo["country"] = getCountryOfOrigin(productInfo["product_name"])
    #Get data from the department of labor website
    productInfo["DOLdata"] = getDOLCountryData(productInfo["country"])
    #Get data from the international labor organization
    productInfo["ILOFatalityPercentage"] = getILOFatalityPercentData(productInfo["country"])
    #Get environmental performance index 
    productInfo["EPIScore"] = getEPIScore(productInfo["country"])

    productInfo["carterScores"] = getCompanyScores(productInfo["product_name"])

    carterScores = productInfo["carterScores"]

    productInfo["ILOFatalityPercentage"] = float(productInfo["ILOFatalityPercentage"]) 
    productInfo["EPIScore"] = float(productInfo["EPIScore"])

    carterScores[0] = float(carterScores[0])
    carterScores[1] = float(carterScores[1])
    carterScores[2] = float(carterScores[2])
    carterScores[3] = float(carterScores[3])

    #THE ALGIRITIHHIHIMSMSMMSS
    productInfo["laborScore"] = (carterScores[2]*10)-(15*productInfo["DOLdata"])-productInfo["ILOFatalityPercentage"]
    productInfo["environmentScore"] = ((carterScores[1]*10)+productInfo["EPIScore"]+carterScores[0])/3

    return(json.dumps(productInfo))



@app.route("/index")
def index():
    class companyInfo:
        name = "NULL"
        environmentScore = "NULL"
        ank = "NULL"

    companyInfo.name = "Coca-Cola"
    companyInfo.environmentScore = "73.2"
    companyInfo.rank = "70/100"
    return jsonify(name = companyInfo.name,environmentScore = companyInfo.environmentScore, rank = companyInfo.rank)
    #return "Hellooooo"


if __name__ == "__main__":
    app.run(debug=True)