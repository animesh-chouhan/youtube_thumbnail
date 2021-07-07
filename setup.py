import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="youtube_thumbnail",
    version="0.1.0",
    author="Animesh Singh Chouhan",
    author_email="animeshsingh.iitkgp@gmail.com",
    description="CLI tool to download YouTube thumbnails",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/animesh-chouhan/youtube_thumbnail",
    project_urls={
        "Bug Tracker": "https://github.com/animesh-chouhan/youtube_thumbnail/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": ["youtube_thumbnail=youtube_thumbnail.cli:main"]
    },
)
