import requests


def get_id_by_name(name: str):
    id = -1
    for hero in data:
        if hero["name"] == name:
            id = hero["id"]
            break
    return id


def get_powerstats_by_id(id: int):
    command = "/powerstats/"+str(id)+".json"
    url = "https://akabab.github.io/superhero-api/api"
    route = url+command
    response = requests.get(route)
    return response.json()


def get_data():
    route = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(route)
    return response.json()


def get_intelligence(d: dict):
    int_ = d["intelligence"]
    return int_


"""Задание 1"""
level = 0
Genious = ""
heroes = ["Hulk", "Captain America", "Thanos"]
data = get_data()
for name in heroes:
    id = get_id_by_name(name)
    d = get_powerstats_by_id(id)
    int_ = get_intelligence(d)
    if level < int_:
        Genious = name
        level = int_
print(Genious)