import setuptools

if __name__ == "__main__":
    with open("README.md") as f:
        long_description = f.read()
    setuptools.setup(
        name="czip",
        version="2.0.1",
        author="Nguyen Ngoc Khanh",
        author_email="khanh.nguyen.contact@gmail.com",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/khanh101/czip",
        packages=setuptools.find_packages(),
        license="MIT",
        install_requires=[
            "pycryptodomex==3.17",
            "zlib==1.2.13",
        ],
    )
