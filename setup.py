from setuptools import setup, find_packages

setup(
    name="enhanced-retro-cricket",
    version="1.0.0",
    description="A comprehensive cricket batting simulation with realistic gameplay mechanics",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Cricket Game Developer",
    author_email="developer@cricketgame.com",
    url="https://github.com/yourusername/enhanced-retro-cricket",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Games/Entertainment :: Arcade",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pygame>=2.0.0",
        "numpy>=1.19.0",
    ],
    entry_points={
        "console_scripts": [
            "cricket-game=src.enhanced_cricket:main",
        ],
    },
)
