import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gitpraise",
    version="0.0.1",
    author="Yoann Lamouroux",
    author_email="ylamouroux@ubuntu.com",
    description="Like 'git blame', except it's the opposite",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ylmrx/gitpraise",
    packages=setuptools.find_packages(),

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'gitpython',
        'emoji',
        'colorama',
        'click',
    ],
    entry_points = {
        'console_scripts': ['gitpraise=gitpraise.git_praise:praise'],
    },
)

