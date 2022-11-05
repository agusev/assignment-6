import requests
import sys

if (len(sys.argv) == 2):
    inp = int(sys.argv[1])

    # server #1
    print(f'client_1 | My argument is {inp}')
    server1 = requests.get('http://localhost:5001/', data=str(inp))
    print('client_1 | Request Sent!')
    print(f'client_1: server_1 returned {server1.text}')
    print("")

    # server #2
    print(f'client_2 | My argument is {inp}')
    server2 = requests.get('http://localhost:5002/', data=str(inp))
    print('client_2 | Request Sent!')
    print(f'client_2: server_2 returned {server2.text}')
    print("")

    # server #3
    print(f'client_3 | My argument is {inp}')
    server2 = requests.get('http://localhost:5003/', data=str(inp))
    print('client_3 | Request Sent!')
    print(f'client_3: server_3 returned calculations for {server2.text}')
    print("")

    # # server #4
    print(f'client_4 | My argument is {inp}')
    server2 = requests.get('http://localhost:5004/', data=str(inp))
    print('client_4 | Request Sent!')
    print(f'client_4: server_4 returned {server2.text}')
    print("")

else:
    print('ivalid input')
