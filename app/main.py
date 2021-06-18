from flask import Flask, jsonify, request

from servises import get_name, parse_site

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/ok/auth', methods=['GET'])
def get_names():
    login = request.args.get('login')
    password = request.args.get('password')
    try:
        name, id = get_name(parse_site(login=login, password=password))
        return jsonify({'status': 'ok','id':id, 'name': name})
    except Exception as e :
        print(e)
        return jsonify({'status': 'fail'})


if __name__ == '__main__':
    app.run()
