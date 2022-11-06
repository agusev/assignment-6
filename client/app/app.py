import requests
import sys

if (len(sys.argv) == 2):
    inp = int(sys.argv[1])

    print(f'client_1 | My argument is {inp}')

    # server #1
    server1 = requests.get('http://localhost:5001/', data=str(inp))
    print('client_1 | Request Sent!')
    print("")

    # server #2
    server2 = requests.get('http://localhost:5002/', data=str(inp))
    print('client_2 | Request Sent!')
    print("")

    # server #3
    server3 = requests.get('http://localhost:5003/', data=str(inp))
    print('client_3 | Request Sent!')
    print("")

    # server #4
    server4 = requests.get('http://localhost:5004/', data=str(inp))
    print('client_4 | Request Sent!')
    print("")

else:
    print('Wrong input number, try again')
