import json
import os


def LoadConfig():
    cwd = os.getcwd()
    cwdUse = str(cwd)

    if cwdUse.__contains__("src"):
        cwdUse = cwdUse[0: (len(cwdUse) - 1 - 3)]

    jsonDir = str(cwdUse) + "/config.json"

    with open(jsonDir) as f:
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


def IP_URLPull():
    data = LoadConfig()
    url = data["IP_ADDR"]
    return url

def CamPort():
    data = LoadConfig()
    raw = data["WEBCAM_PORT"]
    casted = int(raw)
    return casted


def VideoMode():
    data = LoadConfig()
    mode = data["CAM_MODE"]
    return mode
