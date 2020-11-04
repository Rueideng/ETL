from flask import Flask,request,jsonify
import poker as p


app = Flask(__name__)
"""
@app.route('/series')
def series():
    n = int(request.args.get('n'))
    print(n)
    output = str(s.Func(n))
    print(output)
    return output
"""
@app.route('/poker', methods=['GET', 'POST'])
def poker():
    if request.method == 'GET':
        outStr = """
        <html>
            <head>
                <title>poker</title>
            </head>
            <body>
                <h1>How many players?</h1>
                <form action="/poker" method="post">
                    <input type="textbox" name="players">
                    <button type="submit">Submit</button>
                </form>
            </body>
        </html>
        """
        return outStr
    elif request.method == 'POST':
        players = request.form.get('players')
        cards = p.poker(int(players))
        return jsonify(cards)

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port = 5000)