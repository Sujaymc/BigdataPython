from flask import Flask, jsonify, request

app= Flask(__name__)

#Route
@app.route('/')
def home():
    return jsonify({'message':'Welcome'})

#GET
@app.route('/api/hello',methods=['GET'])
def say_hello():
    name =request.args.get('name','World')
    return jsonify({'message':f'Hello,{name}!!!!!'})

#POST
@app.route('/api/data',methods=['POST'])
def receive_data():
    data = request.json
    return jsonify({'received':data}), 201

if __name__ == '__main__':
    app.run(debug=True)