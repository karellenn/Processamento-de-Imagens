from setuptools import setup, find_packages

setup(
    name="image_processor",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Pillow",  # Biblioteca para processamento de imagens
        "numpy",   # Biblioteca para operações numéricas
    ],
    author="Arruda",
    description="A image processing package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/karellenn/image_processor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
