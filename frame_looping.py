import cv2
# Open a video capture object
cap = cv2.VideoCapture(0)  # Replace 'your_video.mp4' with the actual video file path

# Specify the target width and height
target_width = 600
target_height = 600

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    if not ret:
        break  # Break the loop if the video is finished

    # Resize the frame
    resized_frame = cv2.resize(frame, (target_width, target_height), interpolation=cv2.INTER_LINEAR)

    # Display the original and resized frames
    cv2.imshow('Original Frame', frame)
    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imshow('Resized Frame', resized_frame)
    # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    

# Release the video capture object and close the windows
cap.release()
cv2.destroyAllWindows()
