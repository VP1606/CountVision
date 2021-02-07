
def SetCSV():
    from os import path
    import json

    validCSV_Entered = False

    while validCSV_Entered is False:
        directory = input("Enter Directory for CSV: ")

        exists = path.exists(directory)

        if exists is True:
            print("Directory Exists!")

            configFile = open("config.json", "r")
            configData = json.load(configFile)
            configFile.close()

            configData["CSV_Directory"] = directory

            configFile = open("config.json", "w")
            json.dump(configData, configFile)
            configFile.close()

            print("Configured CSV Directory.")
            validCSV_Entered = True



        else:
            print("Directory doesn't exist. Enter a valid Directory.")
