from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/email', methods=['POST'])
def form():
   subject = request.form['subject']
   cmd = "osascript -e 'say \""+subject+"\" using \"Deranged\"'"
   os.system(cmd)
   return "OK"



if __name__=='__main__':
   app.run()
