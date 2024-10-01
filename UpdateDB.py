import requests
import sys
import os

def VersionCheck():
    global DBVersion
    with open("MEA.dat","r") as file:
        DBlines=file.readlines()
    for line in DBlines:
        if "Revision" in line:
            line = line.split(" ")
            for word in line:
                if "r" in word:
                    DBVersion = word
                    break
            break

def VersionFetchGit():
    global FetchedVersion, FetchedData
    url = "https://raw.githubusercontent.com/platomav/MEAnalyzer/refs/heads/master/MEA.dat"
    response = requests.get(url)
    if response.status_code == 200:
        FetchedData = response.text
        FecthedLines = response.text.splitlines()
        for line in FecthedLines:
            if "Revision" in line:
                line = line.split(" ")
                for word in line:
                    if "r" in word:
                        FetchedVersion = word
        print(FetchedVersion)
    else:
        print(f"Failed to fetch file. Status code: {response.status_code}")
        sys.exit()

def Update():
    VersionCheck()
    VersionFetchGit()
    if DBVersion == FetchedVersion:
        print("No updates found.")
        os.system('start "" "' + 'MEA.exe' + '"')
    else:
        print("Updating Database...")
        with open("MEA.dat","w") as file:
            file.writelines(FetchedData)
        print("Done")
        os.system('start "" "' + 'MEA.exe' + '"')

Update()