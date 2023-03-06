import os

project_main = 'Program files'
path_to_project = os.path.abspath(os.path.join('..','..','..',
                                               project_main ))
print('\nСодержимое директории', project_main)
for i in os.listdir(path_to_project):
    path = os.path.join(path_to_project, i)
    print('    ', path)

