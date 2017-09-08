#!/usr/local/bin/python3.6
import textract
import os
from contextlib import suppress as contextsuppress
from flask import Flask, make_response, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from random import randrange,random

UPLOAD_FOLDER = '/data'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

errors = {'missing_var':'Please ensure all required variables are specified.',
          'bad_values':'Please ensure all values are correct.',
          'bad_type':'Please ensure all values are of the correct type.'}

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

@app.route('/upload', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return make_response(jsonify({'error': 'No file found'}), 400)
        f = request.files['file']
        if f.filename == '':
            return make_response(jsonify({'error': 'Empty POST found.'}), 400)
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            msg = 'File uploaded to {}'.format(str(UPLOAD_FOLDER)+'/'+str(filename))
            print(msg)
            return make_response(jsonify({'status': msg}), 200)
    return make_response(jsonify({'error': 'Please POST a file to process.'}), 405)

@app.route('/extract', methods=['GET','POST'])
def extract_text():
    if request.method == 'POST':
        if 'file' not in request.files:
            return make_response(jsonify({'error': 'No file found'}), 400)
        f = request.files['file']
        if f.filename == '':
            return make_response(jsonify({'error': 'Empty POST found.'}), 400)
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            filepath = str(UPLOAD_FOLDER)+'/'+str(filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_text = textract.process(filepath).decode('UTF-8')
            with contextsuppress(FileNotFoundError):
                os.remove(filepath)
            return make_response(jsonify({'file_name': filename, 'file_path': filepath,
                    'text': file_text}), 200)
    return make_response(jsonify({'error': 'Please POST a file to process.'}), 405)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')












'''
@app.route('/random', methods=['GET'])
def rand_num():
    # Default variables
    (multi, count) = (1,1)
    args = {'multi': {'val':multi,'optional': True,'type':float},
            'count': {'val':count,'optional': True,'type':int}}
    # Get values from URI
    for nm in args.keys():
        try:
            args[nm]['val'] = args[nm]['type'](request.args.get(nm))
        except TypeError:
            if args[nm]['optional'] == True:
                pass
            else:
                return make_response(jsonify({'error': errors['missing_var']}), 400)
        except ValueError:
            return make_response(jsonify({'error': errors['bad_type']}), 400)
    # Create number(s)
    ret_tuple = []
    for i in range(args['count']['val']):
        try:
            rand_float = random()*args['multi']['val']
        except:
            raise
        else:
            ret_tuple.append(rand_float)
    ret_tuple = tuple(ret_tuple)
    return make_response(jsonify({'value': ret_tuple}), 200)

@app.route('/randint', methods=['GET'])
def randint():
    # Default variables
    (high,low,count) = (100,0,1)
    args = {'high': {'val':high,'optional': False,'type':int},
            'low': {'val':low, 'optional': False,'type':int},
            'count': {'val':count,'optional': True,'type':int}}
    # Get values from URI
    for nm in args.keys():
        try:
            args[nm]['val'] = args[nm]['type'](request.args.get(nm))
        except TypeError:
            if args[nm]['optional'] == True:
                pass
            else:
                return make_response(jsonify({'error': errors['missing_var']}), 400)
        except ValueError:
            return make_response(jsonify({'error': errors['bad_type']}), 400)
    # Check numbers
    if args['high']['val'] < args['low']['val']:
        return make_response(jsonify({'error': errors['bad_values']}), 400)
    # Create random number(s)
    ret_tuple = []
    for i in range(args['count']['val']):
        num = randrange(args['low']['val'],args['high']['val'])
        ret_tuple.append(num)
    ret_tuple = tuple(ret_tuple)
    return make_response(jsonify({'value': ret_tuple}), 200)
'''
