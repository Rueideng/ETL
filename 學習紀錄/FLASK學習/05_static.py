from flask import Flask,request

app=Flask(__name__,static_url_path="/static1",static_folder="./static")
@app.route("/hello_google")
def hello_get():
    outStr="""<img scr="/static1/google.png">"""
    return outStr


if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port = 5000)