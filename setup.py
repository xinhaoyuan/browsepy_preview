import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "browsepy_preview",  
    version ="0.1",
    scripts = [],
    author = "Xinhao Yuan",
    author_email = "xinhaoyuan@gmail.com",
    description = "browsepy plugin to preview files in iframes",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/xinhaoyuan/browsepy_preview",
    packages = setuptools.find_packages(),
    package_data = {"browsepy_preview" :
                    [ "static/javascript/main.js",
                      "static/css/styles.css",
                      "templates/preview_parent_window.html"
                    ]},
    install_requires = ["browsepy"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License"
        "Operating System :: OS Independent",
    ]
)
