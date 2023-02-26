"""
       Done by Isaac Muuo
       +254741437712
       aimewizard2000@gmail.com
       Copyright 2022
                       """
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return '<head><title>einstein.com</title></head><body><h1>WEB PROGRAMMING</h1><br><br><div style = "height:600px;width:100%;' \
           'background:linear-gradient(180deg, violet, maroon);box-shadow:0 0 10px #2196f3, 0 0 30px #2196f3, 0 0 50px #2196f3">' \
           '                <div class = "cont"><h2>Einstein</h2><br><br><br><br><br><br><br><br><br><br>' \
           '                <br><br><br><br><br><br><br><br><br><a href = #>www.einstein.com</a></div>' \
           '                <div class = "cont"><h2>Einstein</h2><br><br><br><br><br><br><br><br><br><br>' \
           '                <br><br><br><br><br><br><br><br><br><a href = #>www.einstein.com</a></div>' \
           '                <div class = "cont"><h2>Einstein</h2><br><br><br><br><br><br><br><br><br><br>' \
           '                <br><br><br><br><br><br><br><br><br><a href = #>www.einstein.com</a></div>' \
           '                <div class = "cont"><h2>Einstein</h2><br><br><br><br><br><br><br><br><br><br>' \
           '                <br><br><br><br><br><br><br><br><br><a href = #>www.einstein.com</a></div>' \
           '                <div class = "cont"><h2>Einstein</h2><br><br><br><br><br><br><br><br><br><br>' \
           '                <br><br><br><br><br><br><br><br><br><a href = #>www.einstein.com</a></div>' \
           '                </div><style>body{text-align:center;' \
           'background:#000;}h1{color:#fff;font-style:normal;}h2{background:#000;box-shadow:0 0 20px #fff, 0 0 30px maroon, 0 0 50px maroon;}a{padding: 12px 40px;letter-spacing:2px;color:#fff;' \
           'background:linear-gradient(90deg, blue, maroon);border-radius:40px;text-decoration:none;font-size:normal;}' \
           '.cont{color:#fff;background:#2196f3;height:70%;width:230px;float:left;margin:20px;padding:10px;}h1:hover{box-shadow:0 0 10px #fff' \
           ', 0 0 30px #2196f3, 0 0 50px #2196f3;}a:hover{box-shadow:0 0 10px #fff, 0 0 10px #fff, 0 0 20px #2196f3, 0 0 30px #2196f3, 0 0 50px #2196f3;font-size:large;}</style></body>'

if __name__ == '__main__':
    app.run(debug=True)