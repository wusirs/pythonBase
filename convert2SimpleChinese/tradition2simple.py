import os
from typing import BinaryIO

import chardet
import opencc
import traceback

'''
    繁体转简体
'''

t2s = opencc.OpenCC('t2s')
SOURCE: str = 'C:\\Users\\heisenberg\\Desktop\\test'
DESTINATION: str = 'C:\\Users\\heisenberg\\Desktop\\sim'


def traditional_to_simple(source_path: str, destination_path: str) -> None:
    file_absolutely_path: str = None
    try:
        file_ls: [str] = os.listdir(source_path)
        for file_name in file_ls:
            file_absolutely_path = source_path + '\\' + file_name
            preview: BinaryIO = open(file_absolutely_path, 'rb')
            encoding_format: str = chardet.detect(preview.read())['encoding']
            # file_real_name = os.path.splitext(file_absolutely_path)[0]
            file_extension: str = os.path.splitext(file_absolutely_path)[1]
            with open(file_absolutely_path, 'r', encoding=encoding_format) as f:
                content: str = f.read()
                simplified_text: str = t2s.convert(content)
                target_file_name: str = file_name.replace(file_extension, '.simple' + file_extension)
                with open(destination_path + '\\' + target_file_name, "w",
                          encoding=encoding_format) as file:
                    file.write(simplified_text)
                    file.close()
    except FileNotFoundError as e:
        print("文件不存在: {0}".format(traceback.format_exc()))
        pass
    except Exception as e:
        print("{0} convert fail: {1}".format(file_absolutely_path, traceback.format_exc()))
    pass


if __name__ == '__main__':
    traditional_to_simple(SOURCE, DESTINATION)
