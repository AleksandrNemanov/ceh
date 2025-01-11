import os
import re
import subprocess

import chardet


def get_all_ui_files():
    path_all_files = os.path.join(os.getcwd(), 'files', 'UI files')
    all_files = os.listdir(path_all_files)
    all_ui_files_name = []
    for i in all_files:
        if re.fullmatch(r"^.+\.ui$", i):
            all_ui_files_name.append(i)
    print("Все UI файлы:", all_ui_files_name)
    return all_ui_files_name


def delete_file(ui_files):
    path_all_files = os.path.join(os.getcwd(), 'libs', 'py_from_ui')
    all_deleted_files = []
    for i in ui_files:
        file = f"{path_all_files}{os.sep}{i.removesuffix('.ui')}.py"
        if os.path.exists(file):
            all_deleted_files.append(f"{i.removesuffix('.ui')}.py")
            os.remove(file)
    print("Удаляем файлы:", all_deleted_files)


def create_ui2py_files(all_ui_files_name):
    # time.sleep(1)
    created_files = []
    path_py_files = f"{os.path.join(os.getcwd(), 'libs', 'py_from_ui')}{os.sep}"
    path_ui_files = f"{os.path.join(os.getcwd(), 'files', 'UI files')}{os.sep}"
    for i in all_ui_files_name:
        file = i.removesuffix('.ui')
        cmd = f'pyside6-uic "{path_ui_files}{i}" > "{path_py_files}{file}.py"'
        subprocess.run(cmd, shell=True, check=True)
        created_files.append(f"{file}.py")
    print("Создаем файлы:", created_files)
    return created_files


def change_encoding(files):
    changed_encoding = []
    for i in files:
        file = os.path.join(os.path.join(os.getcwd(), 'libs', 'py_from_ui'), i)
        encoding = get_encoding(file)
        if encoding not in ('ASCII', 'UTF-8'):
            with open(file=file, encoding=encoding, mode='r') as f:
                all_content = f.read()
            with open(file=file, encoding='UTF-8', mode='w') as f:
                f.write(all_content)
            changed_encoding.append(i)
    print("Сменил кодировку файлов:", changed_encoding)


def get_encoding(file):
    with open(file=file, mode='rb') as f:
        result = chardet.detect(f.read())
        return result["encoding"].upper()


if __name__ == '__main__':
    all_ui_files = get_all_ui_files()
    delete_file(all_ui_files)
    # Создаем файлы .py и возвращаем список созданных py файлов
    all_changed_files = create_ui2py_files(all_ui_files)
    # Меняем кодировку
    change_encoding(all_changed_files)
