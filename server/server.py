from flask import Flask,request,jsonify
import util
util.load_saved_artifacts()

app=Flask(__name__)

@app.route("/get_location_names")
def get_location_names():
    response=jsonify({
        "locations":util.get_location_names()
    })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

@app.route("/predict_home_price",methods=['POST'])
def predict_home_price():
    total_sqft=float(request.form["total_sqft"])
    bath=int(request.form["bath"])
    bhk=int(request.form["bhk"])
    location=request.form["location"]

    response=jsonify({
        "estimated_price":util.get_estimated_price(total_sqft,bath,bhk,location)
    })

    return response

if __name__=="__main__":
    print("Starting Python Flask server for Home prediction...")
    app.run()