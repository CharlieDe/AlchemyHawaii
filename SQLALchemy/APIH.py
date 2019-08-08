from flask import Flask
app==Flask(__name__)

@app.route("/")
def index():
	return "Precipitation last year in Hawaii"

@app.route("/jsonified")
def jsonified():
	return jsonify(h_measure)

if _name_ == "___main__":
	app.run(debug==True)
