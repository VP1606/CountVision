
def SetCSV():
    import os
    from os import path
    import json

    validCSV_Entered = False

    while validCSV_Entered is False:
        directory = input("Enter Directory for CSV (Hit ENTER if you want to Save to Folder):")

        if directory == "" or directory == " ":
            cwd = os.getcwd()
            cwdUse = str(cwd)
            cwdSave = cwdUse[0: (len(cwdUse) - 12)]

            configFile = open("config.json", "r")
            configData = json.load(configFile)
            configFile.close()

            configData["CSV_Directory"] = cwdSave

            configFile = open("config.json", "w")
            json.dump(configData, configFile)
            configFile.close()

            print("Configured CSV Directory.")
            validCSV_Entered = True

        else:
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

SetCSV()