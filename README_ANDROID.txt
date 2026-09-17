ESCAPE MYSTERY — ANDROID/TABLET COMPLETE PROJECT

WHAT IS INCLUDED
1. Escape_Mystery_Android.py
   - Touch buttons
   - 50 rooms
   - Original level answers/data from your supplied game
   - Lives, score, timer
   - Inventory/items
   - Save slots 1/2/3
   - Restart/New Game
2. buildozer.spec
   - APK configuration
3. build_apk_windows.bat
   - Windows/WSL helper instructions
4. .github/workflows/build-apk.yml
   - Optional one-click APK build through GitHub Actions

EASIEST METHOD
Use GitHub:
1. Create a new GitHub repository.
2. Upload all files from this folder, including the hidden .github folder.
3. Open the repository's Actions tab.
4. Select "Build Escape Mystery APK".
5. Click "Run workflow".
6. After it finishes, open the workflow run and download the artifact named:
   Escape-Mystery-APK
7. Extract it and copy the .apk to your Android tablet.
8. Open the APK on Android and install it.

LOCAL METHOD
On Windows 10/11, WSL + Ubuntu is recommended for Buildozer.
Inside Ubuntu:
  sudo apt update
  sudo apt install -y python3-pip git zip unzip openjdk-17-jdk
  pip3 install --user buildozer cython
  buildozer android debug

The first Android build can take a long time because Android build tools are downloaded.

NOTE
The APK cannot be generated natively by this Windows-only chat environment. The project and automated build workflow are included so the APK can be produced from GitHub Actions or WSL.
