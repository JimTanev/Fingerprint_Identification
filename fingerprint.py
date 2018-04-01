import cv2
import numpy as np
import const
import glob
from os import path


class Fingerprint:
    __id = None
    __file_name = None

    def __init__(self, file_name):
        self.set_file_name(file_name)

    def get_id(self):
        return self.__id

    def get_file_name(self):
        return self.__file_name

    def set_file_name(self, rel_file_name):
        self.__file_name = path.abspath(rel_file_name)
        self.__id, _ = path.basename(rel_file_name).split('.')


def construct_fingerprint(image):
    db_images = glob.glob(const.DB_PATH + '*')
    print(db_images)
    file_names = []
    for db_image in db_images:
        match = __compare_two_images(image, db_image)
        if match > 95.0:
            file_names.append(db_image)
    if len(file_names) < 1:
        return None
    return Fingerprint(file_names[0])


# Compare two images and return percentage match
# @param file_path for the first image
# @param file_path_other for the second image
# @return match as percentage
def __compare_two_images(query_image, train_image):
    img1 = cv2.imread(query_image, 0)
    img2 = cv2.imread(train_image, 0)
    # Initiate ORB detector
    orb = cv2.ORB_create()
    # find the keypoints and descriptors with ORB
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)
    # FLANN parameters
    FLANN_INDEX_LSH = 0  # 6
    index_params = dict(algorithm=FLANN_INDEX_LSH, table_number=6, key_size=12, multi_probe_level=1)
    search_params = dict(checks=100)  # or pass empty dictionary
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(np.asarray(des1, np.float32), np.asarray(des2, np.float32), 2)
    count_matches = 0
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            count_matches += 1
    return count_matches / 5
