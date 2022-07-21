import os
def find_child(dir_path):
    for item in os.listdir(dir_path):
        # print(item)
        if os.path.isfile("{}/{}".format(dir_path,item)):
            print(item)
        else:
            find_child("{}/{}".format(dir_path,item))
if __name__ == '__main__':
    file_root_path  ="/Users/meta/lam/test/python_test/ob_test"
    find_child(file_root_path)


