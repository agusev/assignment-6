from flask import Flask, request

app = Flask(__name__)


def fib(n):
    a = 0
    b = 1
    # n is less 0
    if n < 0:
        print("Incorrect input")
    # Return 0 if n is equal to 0
    elif n == 0:
        return 0
    # Return 1 if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b


@app.route('/')
def server2():
    number = int(request.data)
    ret = fib(number)
    print(f'server2_1 | Server two calculated fib({number}) = {ret}')
    return str(ret)


if __name__ == '__main__':
    print("Starting new_hw6_server2_1 ... done")
    app.run(host='0.0.0.0', debug=True)
