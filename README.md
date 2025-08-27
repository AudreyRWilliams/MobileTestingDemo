# Mobile Testing Demo (For Older Systems)
This project will do the following: 
- creates a tiny iOS app in **Xcode** (runs in the Simulator),
- writes a simple **Appium** UI test in **Python** that opens the Simulator, taps a button and verifies label text,
- explains how to build the app for the Simulator, run Appium, run tests, and push everything to GitHub.
<img width="464" height="940" alt="Screen Shot 2025-08-26 at 5 48 58 PM" src="https://github.com/user-attachments/assets/ecee4cd5-7ee7-4fa4-ab43-dddf3177a70c" /> <br>
<img width="570" height="278" alt="Screen Shot 2025-08-26 at 6 16 21 PM" src="https://github.com/user-attachments/assets/06222b8d-c08a-4ed5-9c3a-37611a504eb0" />

## Checklist / prerequisites
- Make sure Xcode is installed.
- Make sure Appium server is installed.
- Make sure Python 3 and pip3 are available.

## 1 — Create the project folder and git repo
You will end up with this structure (we’ll create it):
<img width="575" height="173" alt="Screen Shot 2025-08-26 at 7 32 48 PM" src="https://github.com/user-attachments/assets/c2fc5ffe-db3e-440c-9d9d-cd439bddccd0" />

## 2 — Create the simple iOS app in Xcode
1. Open **Xcode → File → New → Project... → iOS → Single View App** (or App). <br>
2. Product Name: **HelloSim** <br>
Language: **Swift** <br>
Interface: **Storyboard** <br>
Organization ID: any (e.g., `com.example`) <br>
Minimum iOS: choose one supported by your Xcode (e.g. 12.0) <br>
3. Save the project inside `~/MobileTestingDemo/ios/HelloSim`. <br><br>
**Edit the UI and code**
- Open Main.storyboard:
     - Drag a **Label** in the center; set its **Text** = `Hello`.
     - Drag a **Button** under the label; set its Title = `Tap Me`.
     - For both the Label and Button set **Accessibility Identifiers** (select the element → Identity inspector → Accessibility Identifier):
          - Label: helloLabel
          - Button: tapButton
     - Create `ViewController.swift`
- In Interface Builder: Control-drag the Label to helloLabel outlet and the Button to didTap: action (Touch Up Inside).

**Build & test in Simulator**

- Select a simulator (e.g., iPhone 8) and press ▶ Run in Xcode. Confirm tap changes label from Hello to Tapped!.
## 3 — Build an .app for the Simulator (so Appium can use it)
Instead of hunting derived data, run this from the ios/HelloSim folder to build into a predictable place:
- cd ~/MobileTestingDemo/ios/HelloSim
- xcodebuild -scheme HelloSim -sdk iphonesimulator -configuration Debug -derivedDataPath ./build
After success the simulator app will be at:
- ~/MobileTestingDemo/ios/HelloSim/build/Build/Products/Debug-iphonesimulator/HelloSim.app
Use that full path in your test capabilities (we’ll do that next).
## 4 — Create the Python test and environment
From project root:
- mkdir tests
- cd ~/MobileTestingDemo
  
Create `requirements.txt`..... <br>

Create test `tests/test_hello.py`.....<br>

Create `.gitignore`.....
## 5 — Create & activate Python venv, install client
- cd ~/MobileTestingDemo
- python3 -m venv venv
- source venv/bin/activate
- pip3 install -r requirements.txt

This installs the Appium Python client inside the venv.
## 6 — Start Appium server
In a new Terminal window (leave it open): <br>
<img width="86" height="81" alt="Screen Shot 2025-08-26 at 8 43 16 PM" src="https://github.com/user-attachments/assets/6b6d6026-3780-414e-adfa-8bef6b582551" /> <br>
If Appium starts OK, you’ll see log output and it will listen on http://0.0.0.0:4723.

If you get errors, read the log for WebDriverAgent issues.
## 7 — Find available Simulator names & runtime versions
To list simulators and runtimes: <br>
<img width="233" height="73" alt="Screen Shot 2025-08-26 at 8 45 21 PM" src="https://github.com/user-attachments/assets/0d7dae97-615a-43ee-a44d-f9c4b4960c33" /> <br>

Pick a device and runtime (e.g., iPhone 8 (12.4)), then use those values in deviceName and platformVersion in tests/test_hello.py.
## 8 — Run the test
With Appium running and your virtualenv active:
- source ~/MobileTestingDemo/venv/bin/activate       `# if not already active`
- python3 -m unittest tests/test_hello.py -v

What should happen:

Appium will boot a Simulator (if not already booted), install the .app you built, open it, then the Python test will locate the label/button by accessibility id and assert the text change.

If test passes, you’ll see OK output.
