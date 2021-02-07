from setuptools import setup, find_packages

setup(
    name='CountVision',
    version='2021.05.01',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=['numpy', 'imutils', 'opencv-python', 'setuptools', 'cvlib', 'PyQt5', 'pynput', 'pyshortcuts'],
    url='https://github.com/VP1606/CountVision/tree/master',
    license='APACHE LICENSE V2.0',
    author='VARCO',
    author_email='vpremakantha@gmail.com',
    description='Computer Vision Project',
)
