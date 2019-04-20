from app import app
from flask import jsonify

@app.route('/')
@app.route('/index')

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