import cv2
import skeletonization as skel


def main():

    img_skeleton = skel.execute('fingerprints/101_1.tif')

    # find harris corners
    dst = cv2.cornerHarris(img_skeleton, 2, 3, 0.04)
    ret, dst = cv2.threshold(dst, 0.01 * dst.max(), 255, 0)

    cv2.imshow("skel", img_skeleton)
    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
