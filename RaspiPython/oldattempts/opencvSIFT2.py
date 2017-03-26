import numpy as np
import cv2
from matplotlib import pyplot as plt

MIN_MATCH_COUNT = 10

img1 = cv2.imread('1.jpg',0)          # queryImage
img2 = cv2.imread('image3.jpg',0) # trainImage

# plt.imshow(img1, 'gray'),plt.show()
# plt.imshow(img2, 'gray'),plt.show()

# Import ORB as SIFT to avoid confusion.
try:
    from cv2 import ORB as SIFT

    print("Successfully imported ORB!")
except ImportError:
    try:
        from cv2 import SIFT

        print("Successfully imported SIFT!")
    except ImportError:
        try:
            SIFT = cv2.ORB_create
            print("Successfully imported cv2.ORB_create")
        except:
            raise AttributeError("Version of OpenCV(%s) does not have SIFT / ORB."
                                 % cv2.__version__)

# Initiate SIFT detector
sift = cv2.ORB_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = 0,
                   table_number = 12, # 12
                   key_size = 20,     # 20
                   multi_probe_level = 1) #)
search_params = dict(checks = 50)

flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(np.float32(des1), np.float32(des2), 2)

# store all the good matches as per Lowe's ratio test.
good = []
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)

if len(good)>MIN_MATCH_COUNT:
    src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
    matchesMask = mask.ravel().tolist()

    h,w = img1.shape
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    dst = cv2.perspectiveTransform(pts,M)

    img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)

else:
    print ("Not enough matches are found - %d/%d" % (len(good),MIN_MATCH_COUNT))
    matchesMask = None

draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                   singlePointColor = None,
                   matchesMask = matchesMask, # draw only inliers
                   flags = 2)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)

plt.imshow(img3, 'gray'),plt.show()
