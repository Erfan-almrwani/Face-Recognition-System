import cv2
import numpy as np

def open_camera():
    # Define the camera source (Here, we are using the default camera)
    cap = cv2.VideoCapture(0)
    address= "http://192.168.137.248:4747/video"
    cap.open(address)
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        importa 
        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the windows
    cap.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    open_camera()