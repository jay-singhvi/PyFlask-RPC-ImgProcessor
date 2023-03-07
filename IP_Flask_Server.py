from PIL import Image, ImageOps
import re
from flasgger import Swagger, LazyString, LazyJSONEncoder, swag_from
from flask import Flask, flash, render_template, request, redirect, url_for, jsonify, send_file
import json
import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

@app.route('/ipMain', methods=['GET'])
def ipMain():
    return render_template('ipMain.html')

@app.route('/editImage',methods = ['GET', 'POST'])
def editImage():
    for f in os.listdir(app.config['UPLOAD_FOLDER']):
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], f))

    actions = request.form.getlist('ListOfActions')
    resizeHeight = int(request.form.getlist('Height')[0])
    resizeWidth = int(request.form.getlist('Width')[0])
    posted_file = request.files.get('imageFile', '')
    posted_file_name = request.files.get('imageFile', '').filename

    x = list(actions[0].replace(",","").replace(" ",""))
    print('============= List Of Actions =============', actions)
    print('============= Resize Height =============', resizeHeight)
    print('============= Resize Width =============', resizeWidth)
    print("============= X =============",x)
    print('============= FileStorage =============', posted_file)
    print('============= Name =============', posted_file_name)

    file = FileStorage(posted_file)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'],posted_file_name))
    pil_image = Image.open(file)

    for i in range(len(x)):
        if x[i] == "1":
            #1. Flip Horizontal
            pil_image = ImageOps.mirror(pil_image)
            pil_image.save(f'static/uploads/Seq_{str(i)}_Task_{str(x[i])}_{posted_file_name}',quality = 95)
        if x[i] == "2":
            #2. Flip Vertical
            pil_image = ImageOps.flip(pil_image)
            pil_image.save(f'static/uploads/Seq_{str(i)}_Task_{str(x[i])}_{posted_file_name}',quality = 95)
        if x[i] == "3":
            #3. Rotate +45 Degrees(Clock Wise)
            pil_image = pil_image.rotate(45, resample=Image.BICUBIC)
            pil_image.save(f'static/uploads/Seq_{str(i)}_Task_{str(x[i])}_{posted_file_name}',quality = 95)
        if x[i] == "4":
            #4. Rotate -45 Degrees(Anti-Clock Wise)
            pil_image = pil_image.rotate(-45, resample=Image.BICUBIC)
            pil_image.save(f'static/uploads/Seq_{str(i)}_Task_{str(x[i])}_{posted_file_name}',quality = 95)
        if x[i] == "5":
            #5. Convert to Grayscale
            pil_image = ImageOps.grayscale(pil_image)
            pil_image.save(f'static/uploads/Seq_{str(i)}_Task_{str(x[i])}_{posted_file_name}',quality = 95)
        if x[i] == "6":
            #6. Resize Image
            pil_image = ImageOps.exif_transpose(pil_image.resize((resizeHeight, resizeWidth), Image.Resampling.LANCZOS))
            pil_image.save(f'static/uploads/Seq_{str(i)}_Task_{str(x[i])}_{posted_file_name}',quality = 95)
        if x[i] == "7":
            #7. Thumbnail(300px X 300px)
            thumbnail_image = ImageOps.exif_transpose(pil_image.resize((300, 300), Image.Resampling.LANCZOS))
            thumbnail_image.save(f'static/uploads/Seq_{str(i)}_Task_{str(x[i])}_{posted_file_name}',quality = 95)
        if x[i] == "8":
            #8. Rotate Right(90 Degrees - Clock Wise)
            pil_image = pil_image.rotate(90, resample=Image.BICUBIC)
            pil_image.save(f'static/uploads/Seq_{str(i)}_Task_{str(x[i])}_{posted_file_name}',quality = 95)
        if x[i] == "9":
            #9. Rotate Left(90 Degrees - Anti-Clock Wise)
            pil_image = pil_image.rotate(-90, resample=Image.BICUBIC)
            pil_image.save(f'static/uploads/Seq_{str(i)}_Task_{str(x[i])}_{posted_file_name}',quality = 95)
        else:
            print("in Else")

    imageListPath = os.listdir('static/uploads')
    imageList = [f'uploads/{image}' for image in imageListPath]
    print('============= Name =============', imageList)
    return render_template("temp.html", imageList=imageList)

