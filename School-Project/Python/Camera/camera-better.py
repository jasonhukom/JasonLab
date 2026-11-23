import cv2 as cv
import sys

def main():
    # 1. Setup Camera Choice
    print("--- Webcam Viewer Pro ---")
    try:
        cam_input = input("Use Internal (0) or External (1) webcam? [Default 0]: ").strip()
        # Default to 0 if input is empty; otherwise convert to int
        cam_idx = int(cam_input) if cam_input in ['0', '1'] else 0
        txt_cam = "Internal" if cam_idx == 0 else "External"
    except ValueError:
        print("Invalid input. Defaulting to Internal (0).")
        cam_idx = 0
        txt_cam = "Internal"

    # 2. Set App Name
    name = input("Enter your App Name [Default 'My Webcam']: ").strip() or "My Webcam"

    # 3. Initialize Video Capture
    webcam = cv.VideoCapture(cam_idx, cv.CAP_V4L2)
    webcam.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc(*'MJPG'))

    # Check if the camera is actually accessible
    if not webcam.isOpened():
        print(f"Error: Could not open the {txt_cam} camera.")
        print("Make sure it is plugged in or not being used by another app.")
        sys.exit()

    print(f"\nSuccess! Running {txt_cam} camera as '{name}'.")
    print("Commands: Press 'q' to quit | Press 'ESC' to quit.")

    try:
        while True:
            ret, frame = webcam.read()

            if not ret:
                print("Error: Could not read frame from camera.")
                break

            # Show the frame
            cv.imshow(name, frame)

            # 5. Handle Exit Conditions
            key = cv.waitKey(1) & 0xFF
            # Exit if 'q' is pressed, 'ESC' (27) is pressed, or window is closed
            if key == ord('q') or key == 27 or cv.getWindowProperty(name, cv.WND_PROP_VISIBLE) < 1:
                break
    finally:
        # 6. Proper Resource Cleanup
        webcam.release()
        cv.destroyAllWindows()
        print("\nResources released. Goodbye!")

if __name__ == "__main__":
    main()

