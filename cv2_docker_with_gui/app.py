import cv2
import numpy as np

# Create a black image
image = np.zeros((400, 400, 3), dtype=np.uint8)

# Draw a red circle
cv2.circle(image, (200, 200), 100, (0, 0, 255), -1)

# Display the image
cv2.imshow("Circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
