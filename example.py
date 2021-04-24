from flask import Flask,redirect,request
from sabpaisa import main,auth


dic=dic={"username":"nishant.jha_2885","password":"SIPL1_SP2885","API_KEY":"rMnggTKFvmGx8y1z","API_IV":"0QvWIQBSz4AX0VoH","client_code":"SIPL1","email":"kanu0704@gmail.com"}
s = main.Sabpaisa(URLfailure="http://127.0.0.1:5000/response",
                  URLsuccess="http://127.0.0.1:5000/response",
                  payerFirstName="kanishk",
                  payerLastName="dixit",
                  auth=True,payerContact="+918979626196",
                  payerAddress="ABC",
                  tnxId="nvcdsjksdsdsdacdssav12",
                  username=dic["username"],
                  password=dic["password"],
                  authKey=dic["API_KEY"],
                  authIV=dic["API_IV"],
                  clientCode=dic["client_code"],
                  payerEmail="kanu0704@gmail.com",
                  txnAmt="800")


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
