from setuptools import setup, find_packages
from pathlib import Path

root_path = Path(__file__).parent.resolve()
long_description = Path.joinpath(root_path, "README.md").read_text(encoding="utf-8")

setup(
    name="snake",
    version="0.0.1",
    description="Classic snake game written in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/carlosjasso/pygame-snake",
    author="Carlos Jasso",
    author_email="contact@carlosjasso.dev",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    entry_points={
        "console_scripts": [
            "snake=snake:main"
        ]
    }
)