# QMV-maker
Quickly Merge Videos (MP4) from sports cameras like GoPro.
This program allows you to select MP4 files to be joined, and then saves the list of files to a text file. The list of files is displayed in the user interface and can be modified.

### Requirements
* Python 3
* Tkinter
* ffmpeg (in bin folder)
### Installation
1. Clone the repository.
2. Install the required dependencies.
### Usage
Run main.py using Python 3. A window will appear with a “Select Files” button. Click this button to open a file selection dialog. You can select any number of MP4 files. The selected files will be added to the list in the program window.<br>

You can change the order of the files in the list by clicking on a file and then using the “Move Up” and “Move Down” buttons.<br>

When the list of files is ready, enter the path to the output file in the text field at the bottom of the window, and then click the “Save to txt file” button. The program will save the list of files to a text file at the specified path.<br>
