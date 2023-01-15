import os
import sys

path = r'C:/'
os.chdir('C:/')
prev_path = r'C:/'

while True:
    print(path)
    base_path = os.path.basename(path)
    command = input()

    if command == 'exit':
        sys.exit()

    elif command == 'dir':
        with os.scandir(f'{path}') as entries:
            for entry in entries:
                if entry.is_dir() or entry.is_file():
                    print(os.path.join(base_path, entry.name))

    elif command.startswith('cd'):
        try:
            prev_path = path
            os.chdir(command[3:])
            path = os.getcwd()
        except FileNotFoundError:
            print('Системе не удается найти указанный путь.')

    elif command == 'cd..':
        try:
            os.chdir(os.path.join(path,os.pardir))
            prev_path = path
            path = os.getcwd()
        except FileNotFoundError as f:
            print(f)

    elif command.startswith('mkdir'):
        try:
            os.mkdir(os.path.join(path,command[6:]))
        except FileExistsError:
            print('Подпапка или файл Pictures уже существует.')

    elif command.startswith('open'):
        try:
            os.startfile(command[5:])
        except FileNotFoundError as f:
            print(f)

    elif command.startswith('del'):
        try:
            os.remove(command[4:])
        except FileNotFoundError:
            print(fr'Не удается найти {os.path.join(path, command[4:])}')

    elif command.startswith('ren'):
        try:
            old, new = command[7:].split()
            os.rename(old, new)
        except FileNotFoundError:
            print(fr'Не удается найти {os.path.join(path, old)}')
        except Exception:
            print('Ошибка в синтаксисе команды.')

    elif command.startswith('rmdir'):
        try:
            os.rmdir(os.path.join(path, command[6:]))
        except FileNotFoundError:
            print(fr'Не удается найти {os.path.join(path, command[4:])}')

    else:
        print(fr'{command} не является внутренней или внешней командой, исполняемой программой или пакетным файлом.')