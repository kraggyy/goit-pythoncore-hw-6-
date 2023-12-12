from setuptools import setup, find_namespace_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='clean_folder',
    version='1.0.0',
    description='Code which cleans and sorts your directories',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/kraggyy/goit-pythoncore-hw-7',
    author='Daniil Tymoshenko',
    author_email='dan.tym@icloud.com',
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    python_requires=">=3.8",
    entry_points={'console_scripts': ["clean-folder=clean_folder.clean:main"]}
)


