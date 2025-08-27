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
