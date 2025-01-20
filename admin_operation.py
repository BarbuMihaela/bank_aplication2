import json
from locale import currency


def remove_user(user_to_be_deleted: str, bank_path: str = "bank.json", auth_path: str = "auth.json" , clients_path: str = "clients.json"):

    with open(bank_path, "r") as f1, \
        open(auth_path, "r") as f2, \
        open(clients_path, "r") as f3:
        accounts = json.loads(f1.read())
        credentials = json.loads(f2.read())
        clients = json.loads(f3.read())


    accounts.pop(user_to_be_deleted, None)
    credentials.pop(user_to_be_deleted, None)
    clients.pop(user_to_be_deleted, None)


    with open(bank_path, "w") as accounts_file, \
        open(auth_path, "w") as credentials_file, \
        open(clients_path, "w") as clients_file:
        accounts_file.write(json.dumps(accounts, indent=4))
        credentials_file.write(json.dumps(credentials, indent=4))
        clients_file.write(json.dumps(clients, indent=4))


