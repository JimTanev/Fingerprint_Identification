import cv2
import numpy as np
import skeletonization as skel


def main():

    img_skeleton = skel.execute('fingerprints/pic2.tif')

    # find harris corners
    img_skeleton = np.float32(img_skeleton)
    dst = cv2.cornerHarris(img_skeleton, 2, 3, 0.04)
    dst = cv2.dilate(dst, None)
    ret, dst = cv2.threshold(dst, 0.01 * dst.max(), 255, 0)
    dst = np.uint8(dst)

    cv2.imshow("skel", img_skeleton)
    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
