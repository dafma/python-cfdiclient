import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='electroefoscfdi',
    version='1.2.0',
    author='electroefos',
    author_email='losefosmx@gmail.com',
    description='custom client descarga masiva sat  ver el codigo original,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dafma/python-cfdiclient',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    install_requires = [
        'lxml>=4.2.5',
        'requests>=2.21.0',
        'pycryptodome>=3.7.2',
        'pyOpenSSL>=18.0.0'
    ]
)
