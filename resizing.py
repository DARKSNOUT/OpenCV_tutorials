"""import cv2 

# Load the image from file
image_path = r'D:\ML\openCV\11.jpg'
image = cv2.imread(image_path)
image=cv2.resize(image,(900,500))
image2=cv2.imread(r'D:\ML\openCV\2k.png')
# Check if the image is successfully loaded
if image is None:
    print(f"Error: Unable to load the image from '{image_path}'")
else:
    # Display the image
    cv2.imshow('Image', image)
    small_img=cv2.resize(image2,(50,50))
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imshow('Image', small_img)
    small_img=cv2.resize(image,(904,414,3))
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imshow('Image', image2)
    # Wait for a key press and close the window on key press
    print(image2.shape)
    print(image.shape)
    print(small_img.shape)
    cv2.waitKey(0)
    cv2.destroyAllWindows()"""
import cv2

print("OpenCV version:", cv2.__version__)

