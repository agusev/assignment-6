from flask import Flask, request

app = Flask(__name__)
PORT = 5001
HOST = 'localhost'

def fact(n):
    return 1 if (n == 1 or n == 0) else n * fact(n - 1)

@app.route('/')
def server1():
    number = int(request.data)
    ret = fact(number)
    print(f'server1_1 | Server one calculated {number}! = {ret}')
    return str(ret)


if __name__ == '__main__':
    print("Starting new_hw6_server1_1 ... done")
    app.run(host=HOST, port=PORT)
