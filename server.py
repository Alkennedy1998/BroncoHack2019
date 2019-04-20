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
	
	return data

def getILOFatalityPercentData(country):
	data = 0
	
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
		
	return data
					
def getEPIScore(country):
	with open('EPI_DATA.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		columns = True
		for row in csv_reader:
			if (row[2] == country):
				return row[10]
				
	return "NULL"


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
            "product_name": "Back To Nature, Fudge Striped Cookies",
            "title": "",
            "category": "Food, Beverages & Tobacco > Food Items > Bakery > Fudge",
            "manufacturer": "Back To Nature Foods Company, LLC",
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

    querystring = {"barcode":barcode,"key":"s8s1y69twcpt5wwqtcszuljagdxaa7"}

    payload = "{\n\t\"testGreeting\": \"hello\"\n}"
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "086bec25-38af-53a8-6054-4c6184e3965e"
    }

    #response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    product_data_object = json.loads(test_data_JSON())
    #poduct_data_object = json.loads(response.text)

    product_name = product_data_object['products'][0]['manufacturer']

    #remove when using API 
    #return(test_function())

    return(product_name)



@app.route("/product_name")
def product_name():
    return test_function()

@app.route("/productInfo")
def productInfo():
    
    productInfo = {
        "barcode":"NULL",
        "product_name":"NULL",
        "country":"NULL",
        "DOLdata":"NULL",
        "ILOFatalityPercentage":"NULL",
        "EPIScore":"NULL",
        "carterScores":"NULL"

    }

    productInfo["country"] = "India"

    #Get name of product
    productInfo["product_name"] = barcode_To_Product_Name(productInfo["barcode"])

    #Get data from the department of labor website
    #productInfo["DOLdata"] = getDOLCountryData(productInfo["country"])

    #Get data from the international labor organization
    productInfo["ILOFatalityPercentage"] = getILOFatalityPercentData(productInfo["country"])
    #Get environmental performance index 
    productInfo["EPIScore" ] = getEPIScore(productInfo["country"])

    productInfo["carterScores"] = getCompanyScores(productInfo["product_name"])

    return(productInfo)



@app.route("/index")
def index():

    class companyInfo:
        name = "NULL"
        environmentScore = "NULL"
        ank = "NULL"

    companyInfo.name = "Coca-Cola"
    companyInfo.environmentScore = "63.2"
    companyInfo.rank = "70/100"
    return jsonify(name = companyInfo.name,environmentScore = companyInfo.environmentScore, rank = companyInfo.rank)
    #return "Hellooooo"

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
        if company_odd.find('a').text == company_name:
            score = company.find('td',attrs={'class':'col2 rank-newsweek-green-score'})
            gics = company.find('td',attrs={'class':'col5 rank-gics-sector'})

            print(score.find('a').text)

            print(gics.find('a').text)

            even = soup.find_all('tr',attrs={'class':'even'})

            for company in even:
                company_even = company.find('td',attrs={'class':'col3 rank-company'})
                if company_even.find('a').text == company_name:
                    score = company.find('td',attrs={'class':'col2 rank-newsweek-green-score'})
                    gics = company.find('td',attrs={'class':'col5 rank-gics-sector'})
                    print(score.find('a').text)
                    print(gics.find('a').text)
        else:
            score = "NULL"
    return score

def getIVAData(company):
	data = []
	with open('iva_factors.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=';')
		for row in csv_reader:
			if (company.upper() in row[0].upper()):
				data.append(row[11])#Weighted Industry score
				data.append(row[13])#Environmental score
				data.append(row[14])#Environmental weight
				data.append(row[15])#Social score
				data.append(row[16])#Social weight
				data.append(row[17])#Governance score
				data.append(row[18])#Governance weight
				return data
            
	return data

def getCountryOfOrigin(company):
	with open('company_info.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=';')
		for row in csv_reader:
			if (company.upper() in row[1].upper()):
				return row[3]

def getCompanyScores(company_name):
    score = getNewsWeekScore(company_name)
    data = getIVAData(company_name)

    #Fill data array if missing entries
    if len(data) < 7:
        data = data + ['NULL'] * (7 - len(data))

    toReturn = [score, data[1], data[2], data[3], data[4], data[5], data[6]]
    return toReturn

if __name__ == "__main__":
    app.run(debug=True)