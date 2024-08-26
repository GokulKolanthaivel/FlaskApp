from flask import Flask, request

app = Flask(__name__)

users = {
    1: {'id': 1, 'name': 'John Doe', 'email': 'johndoe@example.com'},
    2: {'id': 2, 'name': 'Jane Smith', 'email': 'janesmith@example.com'}
}

@app.route('/users', methods=['GET'])
def get_all_users():
    return users



if __name__ == "__main__":
    app.run(host='',port=7071,debug=True)