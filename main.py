from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


body {
    background-color: #E6E6FA;
}
form {
    background-color: #eee;
    padding: 20px;
    margin: 0 auto;
    width: 540px;
    font: 16px sans-serif;
    border-radius: 10px;
}
textarea {
    margin: 10px 0;
    width: 540px;
    height: 120px;
}



<!DOCTYPE html>
<html>
    <head>
        
        </style>
    </head>
    <body>



    </body>
</html>


form = """
    <form action="/" method="post">
        <label for="rot">Rotate by:</label>
        <input type="text" name="rot" value="0" />
        <textarea name="text">{0}</textarea>
        <br>
        <input type="submit" value="Submit Query" />
    </form>
"""


@app.route("/")
def index():
    return 

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    text = str(request.form['text'])
    encrypted = rotate_string(text, rot)
    return 


if __name__ == '__main__':
    app.run()