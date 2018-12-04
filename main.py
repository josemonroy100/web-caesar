from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>

    <head>

         <style>

                form {{

                            background-color: #eee;
                            padding: 20px;
                            margin: 0 auto;
                            width: 540px;
                            font: 16px sans-serif;
                            border-radius: 10px;
                        }}
                        
                        textarea {{
                            margin: 10px 0;
                            width: 540px;
                            height: 120px;
                        
                         }} 
                   
                    </style>
                </head>
                <body>
                    <form method = "post" >
                    <label>Rotate by:
                    <input type="text" name="rot" value="0" />
                    </label>
                    <label>
                    <textarea name="text" >{encrypt_text}</textarea>
                    </label>
                    <input type="submit" value="Submit Query">
                    </form>
                </body>
            

                </html>
                """

                        


@app.route("/")
def index():
    return form.format(encrypt_text = "")

@app.route("/", methods=["POST"])
def encrypt():
    rot = int(request.form['rot'])
    text = request.form['text']

    encryption_string = rotate_string(text, rot)
    return form.format(encrypt_text = encryption_string)

app.run()