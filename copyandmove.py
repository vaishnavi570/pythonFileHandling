import os
import argparse

def check_for_empty_or_none(*args):
    for arg in args:
        if arg is None:
            raise Exception("One of the argument is None")
        if arg == "":
            raise Exception("One of the argument is empty")


def copy(source_file, target_file):
    """
    copy source file to target file
    :param source_file:  absolute/relative path to source file
    :type source_file: String
    :param target_file: absolute/relative path to target file
    :type target_file: String
    :return:  None
    :rtype: None
    :raises Exception when inputs or bad or cannot copy a file
    """
    check_for_empty_or_none(source_file, target_file)

    if not os.path.exists(source_file):
        raise Exception(f"{source_file} not found")

    with open(source_file, "r") as sfp:
        source_file_contents = sfp.read()

    with open(target_file, 'w') as tfp:
        tfp.write(source_file_contents)


def move(source_file, target_file):
    """
    moving from source file path to target file path
    :param source_file: name of the source file
    :type source_file: String
    :param target_file: name of the target file
    :type target_file: String
    :return: None
    :rtype: None
    :raises Exception
    """
    check_for_empty_or_none(source_file,target_file)
    if not os.path.exists(source_file):
        raise Exception(f"{source_file} not found")
    # with open(source_file, "r") as sfp:
    #     source_file_contents = sfp.read()
    #
    # with open(target_file, 'w') as tfp:
    #     tfp.write(source_file_contents)

    with open(source_file, "rb") as sfp, open(target_file, 'wb') as tfp:
        for line in sfp.readlines():
            tfp.write(line)
    os.remove(source_file)

if __name__ == '__main__':
    # source_file_path = "C:\\Users\\dines\\PycharmProjects\\pythonfilehandling\\sample.txt"
    # target_file_path = "C:\\Users\\dines\\PycharmProjects\\pythonfilehandling\\sample1.txt"
    parser = argparse.ArgumentParser(
        prog='Copy and Move file',
        description='this program copies or moves files.',
        epilog='file operations')
    parser.add_argument('action',choices=['copy','move'])
    parser.add_argument('--source_path',default='',help="SOURCE file path")
    parser.add_argument('--target_path',default='',help="target file path")
    args = parser.parse_args()
    if args.action == "copy":
        copy(source_file=args.source_path, target_file=args.target_path)
    elif args.action == "move":
        move(source_file=args.source_path, target_file=args.target_path)
    else:
        raise ValueError("invalid action chosen")