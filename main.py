from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>
    <html>
        <head>
            <link href="https://fonts.googleapis.com/css?family=Cedarville+Cursive|Poppins" rel="stylesheet">

            <style>
                body {{
                    background-image: url("http://tumblrchase.com/img/bg/5.png");
                    font-family: 'Poppins', Tahoma, sans-serif;
                }}
                form {{
                    background-color: #dfa290;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                    color: #fff;
                    font-family: 'Poppins', sans-serif;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                    font-family: 'Poppins', sans-serif;
                }}
                h1 {{
                    font-family: 'Cedarville Cursive', cursive;
                    text-align: center;
                    font-size: 50px;
                }}
                submit {{
                    font-family: 'Poppins', sans-serif;
                }}
            </style>
        </head>
        <body>
        <h1>Web Caesar</h1>
        <form method="POST">
            <label for rotation>Rotate by:</label>
            <input type="text" id="rotation" name="rot" value="0">
            <textarea id="text" name="text">{0}</textarea>
            <input type="submit" value="Submit">
        </form>
        </body>

    </html>
    """

@app.route("/")

def index():

    return form.format("")

@app.route("/", methods=['POST'])

def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']

    rotated_text = rotate_string(text, rot)

    return form.format(rotated_text)

app.run()
