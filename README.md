## iVision-Data-Collector-API-1

This API Enables you to collect images when a motion is triggered.
The input feed is given from IP Cam or Device Cam.

The gathered images could be used for training your ML Model.

An Android APP called DroidCAM runs in your mobile phone
making your phone to act as IPCAMERA, your mobile phone is connected to your
home Wi-Fi router.

A custom developed windows application called IVISION DATA COLLECTOR runs
in your laptop which is connected to the home Wi-Fi network. The mobile phone
is also connected to the laptop which is in same home Wi-Fi network. This
IVISION DATA COLLECTOR application has inbuilt motion detection capability with
which starts to store the JPEG files in a defined folder. These JPEG files are the
DATA which will be further pre-processed, labeled before it is used as training
dataset for the AI model.
All we need is to do this setup and start acting (like walking in disguise) in the
front of the mobile phone camera and use the windows application to collect that
data. And upload those collected jpeg files into the common Google drive.
Use your imagination to disguise and start taking the data!

Some tips:
1. Use a stable place (like a tripod.) to hold the mobile phone without shaking.
2. Look for any constant moving items (like celling fans, fluttering paper etc..)
in the video frame and avoid them as it will un-necessarily trigger the
motion detection
3. You can try to take diversified data different angles, different lighting conditions,
with children in disguise, with multiple human bodies disguised together (say two humans sharing a bedsheet to disguise and walking across)
Running across the camera frame in disguise
Crawling across the camera frame in disguise
4. It will be better to provide at least 400 to 500 Snapshots per scenario for
proper AI training
5. Try to give a much as possible diversified scenarios for a better AI training


Steps to execute:
1. Install DROIDCAM APP (free version from Playstore) in your Android mobile
phone (this will convert your mobile phone to a wireless web camera)
2. Connect your Android phone to your home Wi-Fi router.
3. Download iVision Data Collector 1.1.1.exe to your Windows Laptop 
4. Install the IVISION DATA COLLECTOR windows application in your laptop.
5. Connect your Windows LAPTOP to your home Wi-Fi router.
6. Click iVision Data Collector 1.1.1.exe in the directory in which you have
installed the application to invoke the application
7. Click DROIDCAM app in your Android Phone
8. Use IVISION DATA COLLECTOR inbuilt TEST CAMERA option to test camera
and laptop video streaming connectivity.
9. Create Multiple (say one folder for one scenario) directories in your Laptop
10.Use the IVISION DATA COLLECTOR tool to choose the directories one by
one and start taking the data, while acting in the front of the mobile phone
camera with various disguise

