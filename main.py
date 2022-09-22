import json

def get_name(steam_id : int):
    with open("RandomUsernames.json", "r") as usernames_f:
        names = json.loads(usernames_f.read())["RandomUsernames"]

    index = steam_id % 2147483647
    index = index % len(names)

    return names[index]



if __name__ == '__main__':
    print(get_name(76561198240345356))