from flask import Flask, request, Response, jsonify, make_response,render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/data', methods=['GET','POST','DELETE','PUT'])
def data_operation():
    if request.method == 'GET':
        with open('hello.txt','r') as f:
            payload = {
                   'info': f.read(),
                    'time': datetime.now()
            }
            resp = make_response(payload)

            resp.status_code = 200
            resp.headers['etag'] = datetime.now()
            return resp
    # append a new line        
    if request.method == 'POST':
        data = request.json.get('data', None)
        if data == None or data == '':
            return 'empty data', 400
        if data:
            with open('hello.txt','a') as f:
                f.write(data)
                payload = {
                    'info': 'successfully created',
                    'time': datetime.now()
                }
        return payload,201
           
    # delete last line
    if request.method == 'DELETE':
        lines = []
        no = 0
        with open('hello.txt', 'r') as f: 
            lines=f.readlines()
                
            for line in lines:
                no = no +1
        with open('hello.txt','w') as f:
            count = 0
            for line in lines:
                count = count +1
                if count < no:
                    f.write(line)
        return 'deleted'
        # change last line
    if request.method == 'PUT':
        data = request.json.get('data', None)
        if data == None or data == '':

            resp = Response(response='error', status=400)
            return resp
        if data:
            lines = []
            no = 0
            data = request.json['data']
            with open('hello.txt', 'r') as f: 
                lines=f.readlines()
                    
                for line in lines:
                    no = no +1
            with open('hello.txt','w') as f:
                count = 0
                for line in lines:
                    if count < no:
                        f.write(line)
                f.write(data)
            payload = {
                'info': 'successfully updated',
                'time': datetime.now()
            }
            #resp = Response(response=payload, status=200, mimetype="application/json")
            #return jsonify(payload),200
            resp = make_response(payload)
 #           resp.mime_type="application/json"
            resp.status_code=200
            resp.set_cookie("cookiename","cookievalue")
            return resp

            
@app.route('/hello')
def hello():
    return render_template('hello.html')
               


        
            


if __name__=='__main__':
    app.run(debug=True)
