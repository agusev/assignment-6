from flask import Flask, request

app = Flask(__name__)


def square(n):
    return n ** 2


@app.route('/')
def server3():
    number = int(request.data)
    res = ""

    for i in range(number):
        n = square(int(i) + 1)
        print(f'server3_1 | Server three calculated {i+1}^2 = {n}')
        res += f'server3_1 | Server three calculated {i+1}^2 = {n}\n'
    return res


if __name__ == '__main__':
    print("Starting new_hw6_server3_1 ... done")
    app.run(host='0.0.0.0', debug=True)
