import matcher_images as mi
import glob


def main():
    mypath = 'DB1/*'
    file_names = glob.glob(mypath)
    for file_name in file_names:
        match = mi.compare_two_images('fingerprints/101_8.tif', file_name)
        if match > 90.0:
            print(file_name)

if __name__ == '__main__':
    main()
