import os
import chardet
import opencc

'''
    繁体转简体
'''

t2s = opencc.OpenCC('t2s')

def traditional_to_simple(source_path: str, destination_path: str):
    file_ls = os.listdir(source)
    for file_name in file_ls:
        file = source_path + '\\' + file_name
        preview = open(file, 'rb')
        encoding_format = chardet.detect(preview.read())['encoding']
        # file_real_name = os.path.splitext(file)[0]
        file_extension = os.path.splitext(file)[1]
        print(file_extension)
        try:
            with open(file, 'r', encoding=encoding_format) as f:
                content = f.read()
                simplified_text = t2s.convert(content)
                traget_file_name = file_name.replace(file_extension, '.simple' + file_extension)
                with open(destination_path + '//' + traget_file_name, "w",
                          encoding=encoding_format) as file:
                    file.write(simplified_text)
                    file.close()
        except Exception:
            print("%s convert fail".format(file))
            pass
    pass


if __name__ == '__main__':
    source = 'C:\\Users\\heisenberg\\Desktop\\test'
    destination = 'C:\\Users\\heisenberg\\Desktop\\sim'
    traditional_to_simple(source, destination)
