from flask import Flask
from flask import jsonify
import json
import requests

app = Flask(__name__)




def test_function():
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
    product_data_object = json.loads(response.text)

    return(product_data_object['products'][0]['manufacturer'])
 



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
    poduct_data_object = json.loads(response.text)

    product_name = product_data_object['products'][0]['manufacturer']

    return(product_name)



print(test_function())


@app.route("/product_name")
def home():
    return test_function()

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

if __name__ == "__main__":
    app.run(debug=True)