import os
import shutil

from_dir = "C:/Users/jm/Downloads"
to_dir = "C:/Users/jm/Arquivos_Documentos"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    name, extension = os.path.splitext(i)

    if extension == '':
        continue
    if extension in['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + i
        path2 = to_dir + '/' + "Arquivos_Documentos"
        path3 = to_dir + '/' + "Arquivos_Documentos" + '/' + i

if os.path.exists(path2):
    print("Movendo " + i + ". . .")
    shutil.move(path1, path3)

else:
    os.makedirs(path2)
    print("Movendo " + i + ". . .")
    shutil.move(path1, path3)