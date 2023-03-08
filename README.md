# LEAP-Server-Interface
A server interface for the LEAP dedicated server.

This is being written in Python 3.11.2.
All help on getting this interface done is really appreciated!

- Using [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for the GUI.
- Using [Py-SteamCMD-Wrapper](https://pypi.org/project/py-steamcmd-wrapper/) to download SteamCMD and installing the LEAP server.
- Using [ConfigPaser](https://docs.python.org/3/library/configparser.html) to read/write to the game.ini config file.

Home frame:
![image](https://user-images.githubusercontent.com/22444528/223866951-f6b3ea69-7b55-4861-aace-37ac02212637.png)
- Working on getting a console under the start button insted of a pop up windows.

- Need a stop button also.


Install frame:
![image](https://user-images.githubusercontent.com/22444528/223865610-7ac71d4b-663f-4c29-8419-a11cc5975bf7.png)


Settings frame:
![image](https://user-images.githubusercontent.com/22444528/223865662-4f267ed7-580d-4a3d-8334-802e5a38f9dd.png)


Mods & Maps frame:
![image](https://user-images.githubusercontent.com/22444528/223865711-a24a983b-34f8-42cf-a5fd-14f3e6eec06f.png)
having issues saving CF_ModIds, MapListConfig and MutatorList.
Looking for a fix for this.
Might end up trying to get everything under the /Script/ProjectX.ProjectXGameInstance section in one CTkTextBox.


Multipliers frame:
![image](https://user-images.githubusercontent.com/22444528/223865992-0bb1479e-28a2-4a7c-99c2-ec4c02de961c.png)
