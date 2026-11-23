import cv2 as cv

def get_frame():
	webcam = cv.VideoCapture(0)

	while True:
		ret, frame = webcam.read()

		if ret == True:
			cv.imshow("YO BRO", frame)
			key = cv.waitKey(1)
			if key == ord("q"):
				break
	webcam.release()
	cv.destroyAllWindows()

if __name__ == "__main__":
	get_frame()
