Player Rating Grabber

The Player Rating Grabber is a Python-based tool designed to extract, track, and visualize player ratings from online profiles. It automates the process of fetching player ratings from a specified URL, saving the data to a CSV file, and generating a graph to display rating trends over time.

To change the player URL simply navigate to leetify.com/app/profile/GRAB_YOUR_ID_AND_PASTE_IT_HERE

CSSTATS will be enabled in future updates, for now, data is pulled from Leetify. In order to change the premier rank between colors, you will need to fetch the hosted static image from CSSTATS through inspect element:

![image](https://github.com/user-attachments/assets/04b87963-f10f-4913-aa08-ee1394332af1)

Dependencies
This tool requires the following dependencies to be installed:
Python 3.8+
Ensure you have Python installed on your system. You can download it from python.org.
Required Python Libraries
The following Python libraries are required for the tool to function:
selenium - For web scraping and browser automation.
matplotlib - For generating graphs.
schedule - For scheduling tasks to run periodically.
time - For managing delays in the script.
csv - For handling CSV file operations.
os - For file path and directory management.
datetime - For working with timestamps.
Google Chrome
The tool uses Google Chrome for browser automation. Ensure you have the latest version of Chrome installed.
ChromeDriver
ChromeDriver is required to control the Chrome browser. Download the version of ChromeDriver that matches your Chrome browser version from ChromeDriver Downloads.

Installation Instructions
To install all the required Python libraries, you can use the provided install.bat file. This will automatically install the dependencies using pip.
Install.bat File
This batch file will install all the required Python libraries for the tool.


How to Use the Install.bat File
Save the above content into a file named install.bat in the root directory of your project.
Double-click the install.bat file to run it.
The script will automatically install all the required Python libraries.
Additional Notes
Ensure that pip is added to your system's PATH environment variable. If pip is not recognized, you may need to reinstall Python and check the option to add it to PATH during installation.
If you encounter any issues with ChromeDriver, ensure that the version matches your installed Chrome browser version.

The tool will fetch new data every 30 minutes to allow for real-time updates to your rating while you stream. To cancel the process just press Ctrl+C

Rating.html will contain the overlay source to allow you to utilize a custom widget with StreamLabs Desktop. For now, you will need to manually edit your rating but future updates will have automation.

Overlay Example:

![image](https://github.com/user-attachments/assets/92842412-ecfd-4026-b670-7d866fc1a73f)


Enjoy the tool! -Spoon

