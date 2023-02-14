server_data = {
    "server": {
        "host": "127.0.0.1",
        "port": "10"
    },
    "configuration": {
        "access": "true",
        "login": "Ivan",
        "password": "qwerty"
    }
}

for name, value in server_data.items():
    print(name)
    for i_name, i_value in value.items():
        print('   ', i_name, ':', i_value)
