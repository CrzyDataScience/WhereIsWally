# Import OpenCV
import cv2
import os

os.chdir("D:\Projects\CrazyDataScience\WhereIsWally")

# Image file, the image we are going to try and detect Waldo
IMAGE_FILE = './Where_is_Wally.jpg' 

# Set our cascade classifier we created earlier
CASCADE_FILE = './classifier/cascade.xml'

# Load image file
image = cv2.imread(IMAGE_FILE)

# Load our cascade file
cascade = cv2.CascadeClassifier(CASCADE_FILE)

# Detect "Waldo-like" objects and put rectangles around them
# The scaleFactor and minNeighbors are very important to tune the detection
rectangles = cascade.detectMultiScale(image, scaleFactor=1.105, minNeighbors=18,
			minSize=(25, 25), maxSize=(50,50))
			

for (i, (x, y, w, h)) in enumerate(rectangles):
	# Surround cascade with rectangle
	cv2.rectangle(image, (x, y), (x + w, y + h), (255,0,0), 2)
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(image, "Wally detected!", (x - 100, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,0,0), 2)
	
# Display the image with the detection
cv2.imshow("Where is Waldo?", image)
cv2.waitKey(0)