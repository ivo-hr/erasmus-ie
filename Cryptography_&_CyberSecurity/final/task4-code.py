import sys
import cv2
import numpy as np
from Cryptodome.Cipher import AES 
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes

mode = AES.MODE_ECB

inp = input("1 - ECB, 2 - CBC:")
if  inp == "1":
	mode = AES.MODE_ECB
elif inp == "2":
	mode = AES.MODE_CBC
else:
	print("Not valid imput, defaulting to ECB mode...")

if mode != AES.MODE_CBC and mode != AES.MODE_ECB:
    print('Only CBC and ECB mode supported...')
    sys.exit()
keySize = 32
ivSize = AES.block_size if mode == AES.MODE_CBC else 0
imageOrig = cv2.imread("secret.jpg")
rowOrig, columnOrig, depthOrig = imageOrig.shape
cv2.imshow("Original image", imageOrig)
#keyPress = cv2.waitKey(20)
imageOrigBytes = imageOrig.tobytes()
key = get_random_bytes(keySize)
iv = get_random_bytes(ivSize)
cipher = AES.new(key, AES.MODE_CBC, iv) if mode == AES.MODE_CBC else AES.new(key, AES.MODE_ECB)
imageOrigBytesPadded = pad(imageOrigBytes, AES.block_size)
ciphertext = cipher.encrypt(imageOrigBytesPadded)
paddedSize = len(imageOrigBytesPadded) - len(imageOrigBytes)
void = columnOrig * depthOrig - ivSize - paddedSize
ivCiphertextVoid = iv + ciphertext + bytes(void)
imageEncrypted = np.frombuffer(ivCiphertextVoid, dtype = imageOrig.dtype).reshape(rowOrig + 1, columnOrig, depthOrig)
cv2.imshow("Encrypted image", imageEncrypted)
#keyPress = cv2.waitKey(20)
imageOrigBytes = imageOrig.tobytes()
rowEncrypted, columnOrig, depthOrig = imageEncrypted.shape 
rowOrig = rowEncrypted - 1
encryptedBytes = imageEncrypted.tobytes()
iv = encryptedBytes[:ivSize]
imageOrigBytesSize = rowOrig * columnOrig * depthOrig
paddedSize = (imageOrigBytesSize // AES.block_size + 1) * AES.block_size - imageOrigBytesSize
encrypted = encryptedBytes[ivSize : ivSize + imageOrigBytesSize + paddedSize]
cipher = AES.new(key, AES.MODE_CBC, iv) if mode == AES.MODE_CBC else AES.new(key, AES.MODE_ECB)
decryptedImageBytesPadded = cipher.decrypt(encrypted)
decryptedImageBytes = unpad(decryptedImageBytesPadded, AES.block_size)
decryptedImage = np.frombuffer(decryptedImageBytes, imageEncrypted.dtype).reshape(rowOrig, columnOrig, depthOrig)
cv2.imshow("Decrypted Image", decryptedImage)
while True:
	keyPress = cv2.waitKey(1) & 0xFF
	if key == ord('q'):
		break
cv2.destroyAllWindows()
