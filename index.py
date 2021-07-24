import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

from ascii import ascii_gen

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():
	scale_factor = float(request.form['scalefac'])
	file = request.files['file']
	if scale_factor > 1.0:
		flash('Please Enter Scale between 0.1 to 1.0')
		return redirect(request.url)
	
	##if file.filename == '':
	##	flash('No image selected for uploading')
	##	return redirect(request.url)
	
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	
		ascii_gen(filename,app.config['UPLOAD_FOLDER'],scale_factor)
	
		flash('ASCII Image Generated')
		return render_template('index.html', filename=filename)
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
	print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='/' + 'outImage.png'), code=301)

if __name__ == "__main__":
    app.run(debug=False,host=('0.0.0.0'))