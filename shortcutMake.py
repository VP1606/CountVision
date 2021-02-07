def makeShortcut():
    from pyshortcuts import make_shortcut
    import os

    cwd = os.getcwd()
    scriptPath = str(cwd) + "/src/RunUI.py"

    iconPath = str(cwd) + "/CountVision.ico"

    make_shortcut(scriptPath, name="CountVision", icon=iconPath, desktop=True)