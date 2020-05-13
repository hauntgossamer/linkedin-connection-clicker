# linkedin-connection-clicker

This is a Python bot I made with no experience that gets me connections on LinkedIn. 
In two weeks, it took me from 125 connections to over 500! I coded the bones of the bot on the first day, which I report
[***in this video***](https://www.linkedin.com/posts/thomasshottsjr_100daysofcode-lambdaschool-activity-6662792704356872193-stzM) and it was functional, but slightly buggy, by the end of that day. 
A few days later, I was ready to test the bot and it was a resounding success! 
You can see that, [***here***](https://www.linkedin.com/posts/thomasshottsjr_100daysofcode-lambdaschool-activity-6662792704356872193-stzM).

_This bot uses:_
- [x] Python
- [x] Selenium
- [x] pynput
- [x] selenium.common.exceptions

## If you want to use this bot to boost your own connections (*and you are on Windows*), follow these easy steps!
1. Download and extract the zip of the repo into your ``Downloads`` folder.
2. Install Python [***with this installer***](https://www.python.org/ftp/python/3.8.2/python-3.8.2-amd64.exe) and open perform the following keyboard shortcuts/commands:
- ``Windows Key + R`` and then type ``cmd`` and press ``Enter``
- Type ``cd Downloads/linkedin-connection-clicker-master`` and press ``Enter``
- Type ``pip install pynput selenium wheel`` and press enter
- close the ``cmd`` window
3. Install Firefox from [***here***](https://www.mozilla.org/en-US/firefox/new/) (***or*** skip to step 3, if you already have it)
4. Right-click ``run_connect-clicker.bat`` hover over ``Send To`` and click ``Desktop(create shortcut)``
5. Create a new blank text document called secrets.py in the ``linkedin-connection-clicker`` folder (*the extension **must be .py**)
6. Edit ``secrets.py`` with a text editor, such as ``Notepad`` and insert the following lines, including the single quotes, substituting your information:
- ``email = 'your LinkedIn login email here'``
- ``password = 'your LinkedIn password here'``
(LinkedIn Connection Clicker **does not save your information**)
7. Save and close the text editor.
8. Launch ``run-connect-clicker.bat`` directly or using the shortcut on your desktop
9. When the ``Windows SmartScreen`` window pops up, click ``more info`` and then ``run anyway`` (This is just to protect you in the event that you download a malicious batch file and try to run it. If you don't feel safe, feel free to scan the files with your antivirus software before you override the smart screen warning) 
10. Watch the magic happen!
