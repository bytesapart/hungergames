### If you are executing using the Python File:

1. Install dependencies by executing "pip install -r requirments.txt" by changing folder to "src".
1. Before doing anything, install google messages on your android or ios device
1. Make it your default messaging application
1. Go to the 3 dots and select messages for Web
1. Go to terminal and run "python.exe main.py". You can also have a "settings.txt" outside off the src folder to run the
   automation by picking up values from settings.txt (This is the recommended way!)
1. Input all info
1. When running for the first time, the Google messages window will open from a Google Chrome window, scan the QR code there from your phone google messages application
1. Yenjoy!

### If you are executing using the EXE:

1. Before doing anything, install google messages on your android or ios device
1. Make it your default messaging application
1. Go to the 3 dots and select messages for Web
1. Go to command prompt and run "main.exe". You can also have a "settings.txt" outside off the src folder to run the
   automation by picking up values from settings.txt (This is the recommended way!)
1. Input all info
1. When running for the first time, the Google messages window will open from a Google Chrome window, scan the QR code there from your phone google messages application
1. Yenjoy!


===== Configuration options in settings.txt =====

Those in bold are **Mandatory**

**Phone**: Valid, numeric phone number that will receive OTP <br>
**State**: The state to filter upon <br>
**District**: The district to filter upon <br>
**Age**:  Only 2 values, "18+" or "45+" (Yes, add the plus sign too) <br>
**Name**:  Exact character matched name, that is there on the schedule page <br>
Covishield: Whether to filter on Covishield <br>
Covaxin: Whether to filter on Covaxin <br>
Sputnik: Whether to filter on Sputnik <br>
Paid: Whether to filter on Paid <br>
Free: Whether to filter on Free <br>
Hospital: A part of the hospital name. For example, "Nanavati" or "Kokilaben" <br>
Pin: The pin code to filter by. <br>
Slot: The time slot to book at. Numerical value between 1 and 4. 1 corresponds to 9am to 11am, 2 corresponds to 11am to 1pm,
3 corresponds to 1pm to 3pm and 4 corresponds to 3pm to 5pm <br>
Mode: "Ultra" or "Normal". Ultra is fast refreshes in case if the slot is in a
heavily occupied territory, and "Normal" is slower, and refreshes the page after
each check <br>

Another way to automate without the automated logging-in and out is:
https://chrome.google.com/webstore/detail/cowin-bot/ipdhilmkmmbfeilncgchfdabkpnhbeog

You can run my automation in one session and this in another for maximizing chances
because auto-login takes around 30 seconds to re-login every 15 minutes.