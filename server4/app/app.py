from flask import Flask, request

app = Flask(__name__)
PORT = 5004
HOST = 'localhost'

def reverseS(rev):
    reverse = str(rev)[::-1]
    return int(reverse)

@app.route('/')
def server4():
    rev = int(request.data)
    ret = reverseS(rev)
    print(f'server4_1 | Server four calculated reverse({rev}) = {str(ret)}')
    return str(ret)

if __name__ == '__main__':
    print("Starting new_hw6_server4_1 ... done")
    app.run(host=HOST, port=PORT)
