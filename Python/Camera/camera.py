import cv2 as cv

def main():
	cam = int(input("""
Do you use an internal or an external webcam?
Internal type '0'
External type '1'
"""))
	if cam == 0:
		txtcam = "Internal"
	elif cam == 1:
		txtcam = "External"
	else:
		quit() # FOLLOW THE RULES!

	name = input("""
What do you want your camera name to be?
""")

	print(f"""
{cam} = {txtcam};
Camera type {txtcam};
App name is {name};
Press q to exit camera
""")
	webcam = cv.VideoCapture(cam)

	while True:
		ret, frame = webcam.read()

		if ret == True:
			cv.imshow(name, frame)
			key = cv.waitKey(1)
			if key == ord("q"):
				break

	webcam.release()
	cv.destroyAllWindows()

if __name__ == "__main__":
	main()
