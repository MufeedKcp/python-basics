import logging

data = [
    (1, "alice", 25, True),
    (2, "bob", 17, True),
    (3, "charlie", 35, False),
    (4, "david", 120, True),
    (5, "eve", -5, True),
    (2, "bob", 17, True)
]

logging.basicConfig(filename='report.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s - %(name)s')

valid_users = []
unique_user_id = set()


for user_id, name, age, active in data:
    if age < 0:
        logging.warning(f"removed USER_ID: {user_id} for negative age")
        break
    elif not active:
        logging.warning(f"removed USER_ID: {user_id} for not not being active")
    elif len(name) == 0:
        logging.warning(f"removed USER_ID: {user_id} for no name")
    elif age > 100:
        logging.warning(f"removed USER_ID: {user_id} for out of range age")
    else:
        valid_users.append((user_id, name, age, active))
        unique_user_id.add(user_id)
        



print("---------Valid_User-----------------")
for user in valid_users:
    print(user)

