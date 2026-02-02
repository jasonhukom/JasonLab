import cv2 as cv

def get_frame():
	webcam = cv.VideoCapture(0)

	while True:
		ret, frame = webcam.read()

		if ret == True:
			cv.imshow("Face_Scanner", frame)
			key = cv.waitKey(1)
			if key == ord("q"):
				break
	cv.release()
	cv.breakAllWindows()

if __name__ == "__main__":
	get_frame()
