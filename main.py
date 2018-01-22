import cv2
import skeletonization as skel


def main():
    cv2.imshow("skel", skel.execute('fingerprints/pic1.png'))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
