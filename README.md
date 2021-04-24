# flask-example-sabpaisa


This package is used to integrate sabpaisa payment gateway with your python application.

## Installation

You can add SabPaisa SDK to your existing python flask project using following pip command: -

```sh
pip install flask
pip install sabpaisa
```

## Example
```
from flask import Flask,redirect,request
from sabpaisa import main,auth
import random



dic={
    "username":"your username",
    "password":"your password",
    "API_KEY":"your api key",
    "API_IV":"your api iv",
    "client_code":"your client code",
    "email":"your email"}
s = main.Sabpaisa(URLfailure="http://127.0.0.1:5000/response",
                  URLsuccess="http://127.0.0.1:5000/response",
                  payerFirstName="payer first name",
                  payerLastName="payer last name",
                  auth=True,payerContact="payer phone number",
                  payerAddress="payer address",
                  tnxId="your txn id",
                  spDomain="https://uatsp.sabpaisa.in/SabPaisa/sabPaisaInit", # for live env use "https://securepay.sabpaisa.in/SabPaisa/sabPaisaInit" for test env use "https://uatsp.sabpaisa.in/SabPaisa/sabPaisaInit"
                  udfs=["","kanishk","kkk","","","","","","",'','','','','','',''], # array is starting from udf5 to udf20 size of array should be 16
                  param1="",
                  param2="",
                  param3="",
                  param4="",
                  username=dic["username"],
                  password=dic["password"],
                  authKey=dic["API_KEY"],
                  authIV=dic["API_IV"],
                  clientCode=dic["client_code"],
                  payerEmail="payer email id",
                  txnAmt="amount")


app  = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/payment')
def payment():
    return redirect(s.genrateLink())
@app.route("/response", methods=["POST"])
def response():
    query = request.args.get('query')
    st = auth.AESCipher(dic["API_KEY"],dic["API_IV"]).decrypt(query)
    return st


```






