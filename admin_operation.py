import json
from locale import currency


def remove_user(user_to_be_deleted: str, bank_path: str = "bank.json", auth_path: str = "auth.json" , clients_path: str = "clients.json"):

    # here i  need to change to make this more efficient
    with open(bank_path, "r") as f:
        accounts = json.loads(f.read())

    with open(auth_path, "r") as f:
        credentials = json.loads(f.read())

    with open(clients_path, "r") as f:
        clients = json.loads(f.read())

    accounts.pop(user_to_be_deleted, None)
    credentials.pop(user_to_be_deleted, None)
    clients.pop(user_to_be_deleted, None)


    with open(bank_path, "w") as accounts_file, \
        open(auth_path, "w") as credentials_file, \
        open(clients_path, "w") as clients_file:
        accounts_file.write(json.dumps(accounts, indent=4))
        credentials_file.write(json.dumps(credentials, indent=4))
        clients_file.write(json.dumps(clients, indent=4))


