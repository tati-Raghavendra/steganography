import cv2
import os
import string

# Load the image correctly
img = cv2.imread(r"C:\Users\CSE LAB\Desktop\project\mypic.jpg")

# Check if image was loaded successfully
if img is None:
    print("Error: Could not load image. Check the file path and try again.")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m, n, z = 0, 0, 0

height, width, _ = img.shape  # Get image dimensions

# Encrypt message into image
for i in range(len(msg)):
    if n >= height or m >= width:
        print("Error: Message too long for the image.")
        break

    img[n, m, z] = d[msg[i]]
    n += 1
    m += 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Opens the image on Windows

# Decryption
message = ""
n, m, z = 0, 0, 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    for i in range(len(msg)):  
        if n >= height or m >= width:
            break

        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3

    print("Decrypted message:", message)
else:
    print("YOU ARE NOT AUTHORIZED")