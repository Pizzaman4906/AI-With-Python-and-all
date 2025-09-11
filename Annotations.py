import cv2
import matplotlib as plt

image_path = 'macaw.png'
image = cv2.imread(image_path)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BG2RGB)

height, width, _ = image_rgb.shape

rect1_width, rect1_height = 150, 150
top_left1 = (20, 20)
bottom_right1 = (top_left1[0] + rect1_width, top_left1[1] + rect1_height)
cv2.rectangle(image_rgb, top_left1, bottom_right1, (0, 255, 255), 3)

rect2_width, rect2_height = 200,150
top_left2 = (20, 20)
bottom_right1 = (top_left1[0] + rect2_width, top_left2[1] + rect2_height)
cv2.rectangle(image_rgb, top_left1, bottom_right1, (0, 255, 255), 3)
#draw circles at the centers of both rectangles
center1_x = top_left1[0] + rect1_width // 2
center1_y = top_left1[1] + rect1_width // 2
center2_x = top_left2[0] + rect2_width // 2
center2_y = top_left2[1] + rect2_width // 2
cv2.circle(image_rgb, (center1_x, center1_y), 15, (0, 255, 0), -1)
cv2.circle(image_rgb, (center1_x, center1_y), 15, (0, 0, 255), -1)

cv2.line(image_rgb, (center1_x, center1_y), (center1_x, center2_y), (0, 255, 0), 3)

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image_rgb, 'Region 1', (top_left1[0], top_left1[i] - 10), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
cv2.putText(image_rgb, 'Region 2', (top_left2[0], top_left2[i] - 10), font, 0.7, (255, 0, 255), 2, cv2.LINE_AA)
cv2.putText(image_rgb, 'Center 1', (center1_x - 30, center1_y + 40), font, 0.6, (0, 255, 0), 2, cv2.LINE_AA)
cv2.putText(image_rgb, 'Center 2', (center1_x - 30, center1_y + 40), font, 0.6, (0, 255, 0), 2, cv2.LINE_AA)

plt.figure(figsize=(12, 8))
plt.imshow(image_rgb)
plt.title('Annotated Image with Regions, Centers, and Bi-Directional Height Arrow')
plt.axis('off')
plt.show()