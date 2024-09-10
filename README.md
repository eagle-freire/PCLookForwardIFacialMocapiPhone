# PCLookForwardIFacialMocapiPhone
Sends a command from PC to iPhone's IFacialMocap to look forward (calibrate) by simply opening the .py or .exe file

## Set up:
1. Install [Python](https://www.python.org/ftp/python/3.12.6/python-3.12.6-amd64.exe)
1. Edit the .py file by opening it on notepad or your IDE
2. Put your iphone IP on the field
```py
DstIP = "192.168.15.0"
#          ^^^ Put your own iphone IP here, between "  "
```
*You can see the IP on iphone's wi-fi adjustments or on the router settings, it's easier if you reserve your IP in the settings to avoid having to change this value frequently*
3. Open the file when you want iFacialMocap to Look Forward

## My macro set up:
1. Open the terminal
2. Run the command
```shell
pip install pyinstaller
```
4. Run the command
```shell
pyinstaller --onefile -w 'lookforwardvbridger.py'
```
This will compile the .py file into an .exe file, so the macro program can open it up

6. Use Voice Meeter Macro Buttons with the following command on "Request for Button ON / Trigger IN":
```java
System.Execute("C:\Users\Eagle\Desktop\lookforwardvbridger.exe");
   ```
and using the keyboard shortcut "Numpad8"
