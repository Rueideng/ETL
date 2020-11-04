from flask import Flask,request

app = Flask(__name__)


@app.route("/hello_post", methods=["GET","POST"])
def hello_post():
    request_method = request.method
    outStr=""
    if request_method == "GET":
        outStr = """
        <body>
            <form action="hello_post" method="POST">
                <input type="textbox" name="name">
                <button type="submit">SUBMIT</button>
            </form>
        </body>
        """
        return outStr
    elif request_method == "POST":
        outStr = """
        <body>
            <form action="hello_post" method="POST">
                <input type="textbox" name="name">
                <button type="submit">SUBMIT</button>
            </form>
               
        """
        name = request.form.get("name")
        outStr += """
            <div>
                Hello{}
            </div>
        """.format(name)
        outStr +="""
        </body>
        """
        return outStr
if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port = 5000)