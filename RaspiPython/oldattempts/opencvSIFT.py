import numpy as np

import cv2

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

def findMatchesBetweenImages(image_1, image_2):
  """ Return the top 10 list of matches between two input images.

  This function detects and computes SIFT (or ORB) from the input images, and
  returns the best matches using the normalized Hamming Distance.

  Follow these steps:
  1. Compute SIFT keypoints and descriptors for both images
  2. Create a Brute Force Matcher, using the hamming distance (and set
     crossCheck to true).
  3. Compute the matches between both images.
  4. Sort the matches based on distance so you get the best matches.
  5. Return the image_1 keypoints, image_2 keypoints, and the top 10 matches in
     a list.

  Note: We encourage you use OpenCV functionality (also shown in lecture) to
  complete this function.

  Args:
    image_1 (numpy.ndarray): The first image (grayscale).
    image_2 (numpy.ndarray): The second image. (grayscale).

  Returns:
    image_1_kp (list): The image_1 keypoints, the elements are of type
                       cv2.KeyPoint.
    image_2_kp (list): The image_2 keypoints, the elements are of type
                       cv2.KeyPoint.
    matches (list): A list of matches, length 10. Each item in the list is of
                    type cv2.DMatch.

  """
  # matches - type: list of cv2.DMath
  matches = None
  # image_1_kp - type: list of cv2.KeyPoint items.
  image_1_kp = None
  # image_1_desc - type: numpy.ndarray of numpy.uint8 values.
  image_1_desc = None
  # image_2_kp - type: list of cv2.KeyPoint items.
  image_2_kp = None
  # image_2_desc - type: numpy.ndarray of numpy.uint8 values.
  image_2_desc = None
  # WRITE YOUR CODE HERE.

  sift = cv2.ORB_create()
  image_1_kp, image_1_desc = sift.detectAndCompute(image_1, None)
  image_2_kp, image_2_desc = sift.detectAndCompute(image_2, None)

  # bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
  # matches = bf.match(image_1_desc, image_2_desc)
  # matches = sorted(matches, key = lambda x:x.distance)
  # matches = matches[:10]

  bf = cv2.BFMatcher()
  matches = bf.knnMatch(image_1_desc, image_2_desc, k=2)

  # Apply ratio test
  good = []
  for m, n in matches:
      print(m.distance, n.distance, m.distance < .75*n.distance)
      if m.distance < (0.75 * n.distance):
          good.append([m])

  # We coded the return statement for you. You are free to modify it -- just
  # make sure the tests pass.
  print(len(good), good)
  return image_1_kp, image_2_kp, matches
  # END OF FUNCTION.


def drawMatches(image_1, image_1_keypoints, image_2, image_2_keypoints, matches):
  """ Draws the matches between the image_1 and image_2.

  This function is provided to you for visualization because there were
  differences in the OpenCV 3.0.0-alpha implementation of drawMatches and the
  2.4.9 version, so we decided to provide the functionality ourselves.

  Note: Do not edit this function, it is provided for you for visualization
  purposes.

  Args:
    image_1 (numpy.ndarray): The first image (can be color or grayscale).
    image_1_keypoints (list): The image_1 keypoints, the elements are of type
                              cv2.KeyPoint.
    image_2 (numpy.ndarray): The image to search in (can be color or grayscale).
    image_2_keypoints (list): The image_2 keypoints, the elements are of type
                              cv2.KeyPoint.

  Returns:
    output (numpy.ndarray): An output image that draws lines from the input
                            image to the output image based on where the
                            matching features are.
  """
  # Compute number of channels.
  num_channels = 1
  if len(image_1.shape) == 3:
    num_channels = image_1.shape[2]
  # Separation between images.
  margin = 10
  # Create an array that will fit both images (with a margin of 10 to separate
  # the two images)
  joined_image = np.zeros((max(image_1.shape[0], image_2.shape[0]),
                           image_1.shape[1] + image_2.shape[1] + margin,
                           3))
  if num_channels == 1:
    for channel_idx in range(3):
      joined_image[:image_1.shape[0],
                   :image_1.shape[1],
                   channel_idx] = image_1
      joined_image[:image_2.shape[0],
                   image_1.shape[1] + margin:,
                   channel_idx] = image_2
  else:
    joined_image[:image_1.shape[0], :image_1.shape[1]] = image_1
    joined_image[:image_2.shape[0], image_1.shape[1] + margin:] = image_2

  for match in matches:
    image_1_point = (int(image_1_keypoints[match.queryIdx].pt[0]),
                     int(image_1_keypoints[match.queryIdx].pt[1]))
    image_2_point = (int(image_2_keypoints[match.trainIdx].pt[0] + \
                         image_1.shape[1] + margin),
                   int(image_2_keypoints[match.trainIdx].pt[1]))

    cv2.circle(joined_image, image_1_point, 5, (0, 0, 255), thickness = -1)
    cv2.circle(joined_image, image_2_point, 5, (0, 255, 0), thickness = -1)
    cv2.line(joined_image, image_1_point, image_2_point, (255, 0, 0), \
             thickness = 3)
  return joined_image

# If you want to output your image, this basic code should work.
image_1 = cv2.imread("image3.jpg")
image_2 = cv2.imread("1.jpg")
kp1, kp2, matches = findMatchesBetweenImages(image_1, image_2)
output = drawMatches(image_1, kp1, image_2, kp2, matches)
# cv2.imshow("Image", output)
# cv2.waitKey(0)
cv2.imwrite("output.png", output)
