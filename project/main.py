
clients = 'pablo, ricardo,'

def create_client(client_name):
    global clients
    if client_name not in clients:
        clients+=client_name
        _add_comma()
    else:
        print("The client already exist in client list")

def update_client(client_name, update_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name+',',update_client_name+',')
    else:
        print('Clients is not in clients list')

def delete_client(client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name+',', '')
    else:
        print('Clients is not in clients list')

def search_client(client_name):
    client_list = clients.split(',')
    for client in client_list:
        if client != client_name:
            continue
        else:
            return True

def list_clients():
    global clients
    print(clients)

def _add_comma():
    global clients
    clients +=','

def _print_welcome():
    print('WELCOME TO GREENSHELTER VENTAS')
    print('*'*50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist Clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')

def _get_client_name():
    return input('What is the client name? ')


if __name__ == '__main__':
    _print_welcome()
    command = input()
    command = command.upper()
    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input('What is the updated client name')
        update_client(client_name, update_client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('THe client is in the client list')
        else:
            print('The client: {} is not in our client list'. format(client_name))

    else:
        print('invalid command')