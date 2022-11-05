from flask import Flask, request


app = Flask(__name__)
PORT = 5002
HOST = 'localhost'


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        last = int(repr(c)[-1])
        return last


@app.route('/')
def server2():
    number = int(request.data)
    ret = fib(number)
    print(f'server2_1 | Server two calculated {number} = {ret}')
    return str(ret)


if __name__ == '__main__':
    print("Starting new_hw6_server1_1 ... done")
    app.run(host=HOST, port=PORT)
