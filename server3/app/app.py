from flask import Flask, request

app = Flask(__name__)
PORT = 5003
HOST = 'localhost'

def square(n):
    return n ** 2

@app.route('/')
def server3():
    number = int(request.data)

    for i in range(number):
        n = square(int(i) + 1)
        print(f'server3_1 | Server three calculated {i+1}^2 = {n}')
    return str(number)

if __name__ == '__main__':
    print("Starting new_hw6_server3_1 ... done")
    app.run(host=HOST, port=PORT)
