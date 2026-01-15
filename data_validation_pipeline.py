data = [
    (1, "alice", 25, True),
    (2, "bob", 17, True),
    (3, "charlie", 35, False),
    (4, "david", 120, True),
    (5, "eve", -5, True),
    (2, "bob", 17, True)
]

valid_users = []
invalid_users = []
unique_user_id = set()
reason = []

for user_id, name, age, active in data:
    reason = []
    unique_user_id.add(user_id)

    if age < 0:
        reason.append("critical_negative_age")
        invalid_users.append((user_id, name, age, active, reason))
        break

    if not active:
        reason.append("inactive")
    if len(name) == 0:
        reason.append("empty_name")
    if age > 100:
        reason.append("age_out_of_range")
    if len(reason) == 0:
        valid_users.append((user_id, name, age, active))
    else:
        invalid_users.append({"user_id": user_id,  
                            "name": name,
                            "age": age,
                            "active": active,
                            "reason": reason})


print("---------invalid_User-----------------")
for users in invalid_users:
    print(users)

print("---------Valid_User-----------------")
for user in valid_users:
    print(user)

print("---------unique_user_id-----------------")
for id in unique_user_id:
    print(id)