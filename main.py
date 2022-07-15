import os
from ya_disk import YandexDisk


TOKEN = ""

"""Задание 2"""
if __name__ == '__main__':
    ya = YandexDisk(token=TOKEN)
    path_to_file  = input("Введите полное имя файла ")
    base_name = os.path.basename(path_to_file)
    disk_file_path = "netology/"+base_name
    ya.upload_file_to_disk(disk_file_path=disk_file_path, filename=path_to_file)
