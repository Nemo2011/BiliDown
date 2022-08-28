import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", "r", encoding="utf8") as f:
    requires = f.read()

setuptools.setup(
    name="BiliDown",
    version="1.1.0",
    license="GPLv3+",
    author="Nemo2011",
    description="哔哩哔哩命令行下载器",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=[
        "bilidown"
    ],
    keywords=["bilibili", "download", "api"],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: Chinese (Simplified)",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=requires.splitlines(),
    url="https://github.com/nemo2011/BiliDown",
    python_requires=">=3.8",
    entry_points={
        'console_scripts': [
            'bilidown = bilidown.__main__:main',
        ],
    },
)
