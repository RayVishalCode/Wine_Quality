import setuptools

__version__ = '0.0.1'

REPO_NAME = "mlproject"
AUTHOR_USER_NAME = "Vishal"
SRC_REPO = "mlproject"
AUTHOR_EMAIL = "vishalray464407@gmail.com"


setuptools.setup(
name=SRC_REPO,
version=__version__,
author=AUTHOR_USER_NAME,
author_email=AUTHOR_EMAIL,
description="A small python package for ML Project",
long_description="This is a long description of the ML Project package.",
url=f"https;//github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
project_urls={
    "Bug Tracker": f"https;//github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
},
package_dir={"": "src"},
packages=setuptools.find_packages(where="src")
)