from flask import Flask

app = Flask(__name__, static_url_path='/static_url', static_folder='./static')  # static_url_path=網址  localhost:5000/static_url

@app.route('/hello_google')
def hello_google():
    outStr = """
    <link href="/static_url/css/mystyle.css" rel="stylesheet" type="text/css"> 
    <div>
        This is a book.
    </div>
    <div class="test">
        This is a book.
    </div>
    <div>
        <img src="/static_url/images/google.png">
    </div>
    """

    return outStr

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)