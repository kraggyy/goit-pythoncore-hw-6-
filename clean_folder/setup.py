from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0.0',
    description='Code which cleans and sorts your directories',
    url='https://github.com/kraggyy/goit-pythoncore-hw-7',
    author='Daniil Tymoshenko',
    author_email='dan.tym@icloud.com',
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': ["clean-folder=clean_folder.clean:organize_files"]}
)