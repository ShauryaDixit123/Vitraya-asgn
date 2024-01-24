from flask import Flask, request
import flask
from extract import  cnv_img, extract_text
import base64
from cv2 import COLOR_BGR2GRAY
from db import conn

app = Flask(__name__)


def handleGet():
    con = conn()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM images")
    return cursor.fetchall()

def handleExtract():
    img = request.json['img']
    imgdata = base64.b64decode(img)
    with open("./imgs/temp.png", "wb") as fh:
        fh.write(imgdata)
    img = cnv_img("./imgs/temp.png")
    text = extract_text(img)
    return text

def handleSaveData(img_name,text):
    print(img_name,text,"xczxc")
    con = conn()
    cursor = con.cursor()
    cursor.execute("INSERT INTO images (img_name, img_text) VALUES (%s, %s)", (img_name, text))
    con.commit()
    cursor.close()

@app.route("/",methods=["POST","GET"])
def main():
    if request.method == "GET":
        return handleGet()
    if request.method == "POST":
        img_name = request.json['img_name']
        text=  handleExtract()
        handleSaveData(img_name,text)
        response = flask.jsonify({'text': text})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
        

if __name__ == "__main__":
    app.run("http://local.sage.com/data",9000, debug=True)
