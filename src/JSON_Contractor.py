import json

def LoadConfig():
    with open("../config.json") as f:
        data = json.load(f)
        return data


def VersionDetail():
    data = LoadConfig()
    return data["RunUI_Version"]

def DeltaRead():
    data = LoadConfig()
    min = float(data["CV_Delta_MIN"])
    max = float(data["CV_Delta_MAX"])

    result = {
        "min": min,
        "max": max
    }

    return result

def CSV_Target():
    data = LoadConfig()
    directory = data["CSV_Directory"]
    return directory