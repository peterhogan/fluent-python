#!/usr/local/bin/python3.6
from flask import Flask, make_response, jsonify, request
from random import randrange,random
app = Flask(__name__)

'''
class NumberRequest():
    def __init__(schema, error_messages):
        self.schema = schema
        self.errors = error_messages

    def defaults(**kwargs):
'''

errors = {'missing_var':'Please ensure all required variables are specified.',
          'bad_values':'Please ensure all values are correct.',
          'bad_type':'Please ensure all values are of the correct type.'}

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
