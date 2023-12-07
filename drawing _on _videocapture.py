import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Set new properties (adjust values accordingly)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 352)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 288)

start_time=time.time()

while cap.isOpened():
    ret, frame = cap.read()
    if ret:

        image = cv2.imread('your_image.jpg')  # Replace 'your_image.jpg' with the path to your image

        # Set the coordinates for the top-left image
        top_left_coordinates = (int(0.23 * frame.shape[1]), int(0.68 * frame.shape[0]))

        # Set the coordinates for the top-right image
        top_right_coordinates = (int(0.56 * frame.shape[1]), int(0.78 * frame.shape[0]))

        # Convert float coordinates to integers
        start_point_arrowed_line = (int(0.95 * frame.shape[1]), int(0.99*frame.shape[0]))
        end_point_arrowed_line = (int(0.1 * frame.shape[1]), int(0.21 * frame.shape[0]))
        # Calculate FPS
        elapsed_time = time.time() - start_time
        fps = 1 / elapsed_time
        start_time = time.time()

        # Display the FPS on the frame
        text_position = (int(0.1 * frame.shape[1]), int(0.1 * frame.shape[0]))

        # Draw arrowed line on the image
        img2 = cv2.arrowedLine(frame, start_point_arrowed_line, end_point_arrowed_line, (255, 255, 0), 2)
        tf = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        # Draw text on the image
        img2 = cv2.putText(frame, f'FPS: {fps:.2f}', text_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2,cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
