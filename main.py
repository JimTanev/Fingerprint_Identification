import cv2
import numpy as np


def main():

    img1 = cv2.imread('fingerprints/101_1.tif', 0)  # queryImage
    img2 = cv2.imread('fingerprints/pic1.png', 0)  # trainImage

    # Initiate ORB detector
    orb = cv2.ORB_create()

    # find the keypoints and descriptors with ORB
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # FLANN parameters
    FLANN_INDEX_LSH = 0    # 6
    index_params = dict(algorithm=FLANN_INDEX_LSH, table_number=6, key_size=12, multi_probe_level=1)
    search_params = dict(checks=100)  # or pass empty dictionary

    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(np.asarray(des1, np.float32), np.asarray(des2, np.float32), 2)

    count_matches = 0
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            count_matches += 1

    print("The two pictures are matched:", count_matches/5, "%")


if __name__ == '__main__':
    main()
