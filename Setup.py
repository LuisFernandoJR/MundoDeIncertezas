from sys import executable
from cx_Freeze import Executable, setup
import os


path = "./asset"
asset_list = os.listdir(path)
asset_list_completa = [os.path.join(path, asset).replace('\\', "/") for asset in asset_list]
print(asset_list_completa)

executables = [Executable('main.py')]


include_files = asset_list_completa


setup(
    name='Quebrando a Nostalgia',
    version='1.0',
    description='Trabalho da Faculdade',
    options={
        'build_exe': {
            'packages': ['pygame'],  # Pacotes a serem incluídos no build
            'include_files': include_files  # Arquivos a serem incluídos no build
        }
    },
    executables=executables
)