import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title, image):
    """Utility function to display an image."""
    plt.figure(figsize=(8,8))
    if len(image.shape) == 2:
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def interactive_edge_detection(image_path):
    """Interactive activity for edge detection and filtering."""
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return
    

    gray_image = cv2.cvtColor((image, cv2.COLOR_BGR2GRAY))
    display_image("Original Grayscale Image", gray_image)

    print("Select an option :")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")

    while True:
        choice = input("Enter your choice(1-6): ")
        
        if choice == "1":
            sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
            combined_sobel = cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))
            display_image("Sobel Edge Detection", combined_sobel)

        elif choice == "2":
            print("Adjust thresholds for Canny (default: 100 and 200)")
            lower_tresh = int(input("Enter lower threshold: "))
            upper_tresh = int(input("Enter upper threshold: "))
            edges = cv2.Canny(gray_image, lower_thresh, upper_thresh)
            display_image("Canny Edge Detection", edges)

        elif choice == "3":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please select a number between 1 and 6")

interactive_edge_detection('goodimage.png')

    