import cv2
import numpy as np


def main():

    file_path = 'fingerprints/101_1.tif'
    img = cv2.imread(file_path)
    img_skeleton = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    corners = cv2.goodFeaturesToTrack(img_skeleton, 100, 0.01, 10)
    corners = np.int0(corners)

    for i in corners:
        x, y = i.ravel()
        cv2.circle(img, (x, y), 3, 255, -1)

    cv2.imshow("skel", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
