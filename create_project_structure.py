import os
import sys
from pathlib import Path

structure = [
    'data/',
    'data/raw/',
    'data/processed/',
    'data/external/',
    
    'notebooks/',
    'notebooks/exploration/',
    'notebooks/modeling/',
    
    'src/',
    'src/data/',
    'src/models/',
    'src/features/',
    'src/utils/',
    
    'tests/',
    'configs/',
    'models/',
    'logs/',
    
    'Readme.md',
    '.gitignore',
]

def create_project_structure(project_path):
    for item in structure:
        if item[-1] == '/':
            if not os.path.exists(project_path / item):
                os.makedirs(project_path / item)
            else:
                print(f'Directory {project_path / item} already exists')
        else:
            if not os.path.exists(project_path / item):
                with open(project_path / item, 'w') as f:
                    f.write('')
            else:
                print(f'File {project_path / item} already exists')


if __name__ == '__main__':
    location = input('Project location: ')
    if location[-1] != '/':
        location += '/'
        
    project_name = input('Project name: ')
    
    project_path = Path(location) / project_name
    
    print()
    create_project_structure(project_path)
    print()
    
    print('Project structure created successfully')