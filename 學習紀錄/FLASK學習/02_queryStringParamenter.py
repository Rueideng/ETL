from flask import Flask,request

app = Flask(__name__)



@app.route("/hello_get")
def hello_get():
    name=request.args.get("name")
    age = request.args.get("age")
    return "Hello{}, you are {} years old.".format(name,age)





if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port = 5000)