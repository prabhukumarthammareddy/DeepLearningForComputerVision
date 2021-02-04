# load the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image and show basic information on it
image = cv2.imread(args["image"])
print("width: %d pixels" % (image.shape[1]))
print("Height: %d pixels" % (image.shape[0]))
print("Channels: %d " % (image.shape[2]))

# show the image and wait for keypress
cv2.imshow("Image",image)
cv2.waitKey(0)

#save the image --opencv handles converting filetypes automatically
cv2.imwrite("../images/prabhu_new.png", image)


