from flask import Flask, request

app = Flask(__name__)


def reverseS(rev):
    reverse = str(rev)[::-1]
    return int(reverse)


@app.route('/')
def server4():
    rev = int(request.data)
    ret = reverseS(rev)
    print(f'server4_1 | Server four calculated reverse({rev}) = {str(ret)}')
    return f'server4_1 | Server four calculated reverse({rev}) = {str(ret)}'


if __name__ == '__main__':
    print("Starting new_hw6_server4_1 ... done")
    app.run(host='0.0.0.0', debug=True)
