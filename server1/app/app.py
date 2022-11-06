from flask import Flask, request

app = Flask(__name__)


def fact(n):
    return 1 if (n == 1 or n == 0) else n * fact(n - 1)


@app.route('/')
def server1():
    number = int(request.data)
    ret = fact(number)
    print(f'server1_1 | Server one calculated {number}! = {ret}')
    return f'server1_1 | Server one calculated {number}! = {ret}'


if __name__ == '__main__':
    print("Starting new_hw6_server1_1 ... done")
    app.run(host='0.0.0.0', debug=True)
