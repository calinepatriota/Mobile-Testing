# Mobile-Testing

## iOS Automation

##### Dependencies
* Install Python 3 
* On project directory execute the command:
                    ```
                        pip3 install -r requirements.txt
                   ```
* Install appium with brew 
          ``
          brew install appium
          ``
* Install Xcode (version 13+) - https://developer.apple.com/download/all/?q=xcode%2013
* Install Command Line Tools for Xcode - https://developer.apple.com/download/all/?q=xcode%2013
* Install Appium Inspector - https://github.com/appium/appium-inspector/releases/tag/v2021.9.2 (download file **Appium-Inspector-mac-2021.9.2.dmg**)
    - After download, open terminal on the folder that file is and execute the command (Don't unzipe file before do that!)
          ```
                xattr -cr Appium-Inspector-mac-2021.9.2.dmg
                ```
* Open Xcode and create Simulator (iOS version 10+)
* Install .app Wikipedia on Simulator (Follow the instructions here: https://github.com/wikimedia/wikipedia-ios)