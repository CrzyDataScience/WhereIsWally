# Where is Wally/Waldo
This repository contains all the example code for the Crazy Data Science - Where is Wally / Waldo project.
(https://www.youtube.com/watch?v=jtiS8V4iQS4)

All of the scripts and images can be found in the "code" folder.
Keep in mind that you need to have OpenCV compiled and working with Python bindings if you plan to run the example Python scripts.
If you are running Windows make sure to place the following files in the directory with the rest of the files and folders:

- opencv_createsamples.exe
- opencv_traincascade.exe
- opencv_visualisation.exe
- opencv_ffmpeg340_64.dll
- opencv_world340.dll
- opencv_world340d.dll

The cascade classifier has already been trained and is stored in the "classifier" folder.
The same goes for the positive sample vector "positives.vec" file.

## Reproducing the examples from the start

If you want to walk through all the steps make sure to remove the "positives.vec" file and empty the following directories:

- annotations
- classifier

Create positive samples using this command
opencv_createsamples -img wally.jpg -bg negatives.txt -info annotations/annotations.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1300

Create the positive sample vector file
opencv_createsamples -info annotations/annotations.lst -num 1300 -w 25 -h 25 -vec positives.vec

Train the Haar Cascade classifier
opencv_traincascade -data classifier -vec positives.vec -bg negatives.txt -numPos 1200 -numNeg 600 -numStages 10 -w 25 -h 25

Run the python scripts!




