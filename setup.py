from setuptools import setup

setup(
    name="doge-art",
    version="3.7.3",
    url="https://github.com/MUTLCC/doge-art",
    author="Mutlu",
    author_email="",
    description=("wow very terminal doge"),
    license="MIT",
    packages=["doge"],
    package_data={"doge": ["static/*.txt"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
    ],
    entry_points={"console_scripts": ["doge = doge.core:main"]},
)
