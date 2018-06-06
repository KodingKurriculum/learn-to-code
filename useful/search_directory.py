import os

def search(rootdir, file_name):
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file_name in file:
                print("found!! {0}".format(os.path.join(subdir, file)))
                return
            else:
                print("searching {0}".format(os.path.join(subdir, file)))
    print("Didn't find anything womp womp!")

# Run the script
if __name__ == '__main__':
    rootdir = 'D:\\test_folder\\'
    file_name = 'findme'
    search(rootdir, file_name)

