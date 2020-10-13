from flask import Flask, request

app = Flask(__name__)


@app.route('/data', methods=['GET','POST','DELETE','PUT'])
def data_operation():
    if request.method == 'GET':
        with open('hello.txt','r') as f:
            return f.read()
    # append a new line        
    if request.method == 'POST':
        data = request.json.get('data', None)
        if data == None or data == '':
            return 'empty data'
        if data:
            with open('hello.txt','a') as f:
                f.write(data)
                return 'created'
       
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
            return 'empty data'
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
            return 'updated'

            
                


        
            


if __name__=='__main__':
    app.run(debug=True)
