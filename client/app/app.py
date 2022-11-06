
import sys
import requests

if (len(sys.argv) == 2):
    inp = int(sys.argv[1])

    print(f'client_1 | My argument is {inp}')

    # server #1
    server1 = requests.get('http://localhost:5006/', data=str(inp))
    print(server1.text)
    print('client_1 | Request Sent!')
    print("")

    # server #2
    server2 = requests.get('http://localhost:5007/', data=str(inp))
    print(server2.text)
    print('client_2 | Request Sent!')
    print("")

    # server #3
    server3 = requests.get('http://localhost:5008/', data=str(inp))
    print(server3.text)
    print('client_3 | Request Sent!')
    print("")

    # server #4
    server4 = requests.get('http://localhost:5009/', data=str(inp))
    print(server4.text)
    print('client_4 | Request Sent!')
    print("")

else:
    print('Wrong input number, try again')
