#!/usr/bin/python
# _*_ coding:utf-8 _*_

from setuptools import setup, find_packages

# https://pic3.zhimg.com/v2-4563e810d05ec25ce283c7f54a271e2e_r.jpg
setup(
    name="fishratio",
    version="1.0.0",
    url="https://github.com/benben-miao/FishRatio",
    keywords=["CLI", "Biology", "Statistics"],
    description="Calculate the ratio and logarithmic value of species contained in several genus of a family to all species in this family.",
    long_description="Calculate the ratio and logarithmic value of species contained in several genus of a family to all species in this family.",
    download_url="https://pypi.python.org",

    author="benben-miao",
    author_email="benben.miao@outlook.com",
    maintainer="benben-miao",
    maintainer_email="benben.miao@outlook.com",
    license="MIT License",

    # include_package_data=True,
    platforms="any",
    install_requires=['pandas', 'numpy', 'openpyxl', 'xlrd'],
    # packages=find_packages(),
    packages=['fishratio'],
    entry_points={
        'console_scripts': ['fishratio=fishratio.fishratio:calculate'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    data_files=[
        ('', ['README.md'])
    ],
    package_data={
        '':['examples/*.xlsx']
    },
    include_package_data=True
    # exclude_package_data={
    # }
)

# python setup.py bdist_wheel
# pip install dist\*.whl

# python setup.py sdist
# python setup.py install

# pip install twine
# twine upload dist/*