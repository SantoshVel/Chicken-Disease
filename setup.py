import setuptools

# Read the contents of README file for the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Package metadata
__version__ = "0.0.0"
REPO_NAME = "Chicken-Disease"
AUTHOR_USER_NAME = "SantoshVel"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "santoshvel555@gmail.com"

# Setup configuration
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small Python package for a CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    )
