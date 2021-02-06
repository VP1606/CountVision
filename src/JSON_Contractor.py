import json

def LoadConfig():
    with open("../config.json") as f:
        data = json.load(f)
        return data


def VersionDetail():
    data = LoadConfig()
    return data["RunUI_Version"]