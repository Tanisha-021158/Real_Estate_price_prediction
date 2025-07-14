from flask import Flask,request,jsonify

app=Flask(__name__)

if __name__=="__main__":
    print("Starting Python Flask server for Home prediction...")
    app.run()