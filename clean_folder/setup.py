from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.1.0',
    description='Hw 7. Clean folder',
    author='Anastasiia Ivanytska',
    author_email='a.titova.wk@gmail.com',
    license='MIT',
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': [
            'clean_folder=clean_folder.main:start']}
)