from setuptools import setup, find_packages

setup(
    name="wizard_tower",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pygame>=2.6.1",
        "opencv-python>=4.8.0",
        "numpy>=1.24.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A puzzle game where a wizard collects potions to defeat monsters",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/wizard_tower",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    include_package_data=True,
    package_data={
        "wizard_tower": [
            "assets/sprites/**/*",
            "assets/sounds/*",
            "assets/ui/*",
            "instances/*",
            "src/**/*"
        ]
    },
    entry_points={
        "console_scripts": [
            "wizard-tower=wizard_tower.main:main",
        ],
    },
)
