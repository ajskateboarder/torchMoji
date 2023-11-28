from setuptools import setup

setup(
    name='torchmoji',
    version='1.0',
    packages=['torchmoji'],
    description='torchMoji',
    include_package_data=True,
    install_requires=[
        'emoji==0.4.5',
        'numpy',
        'scipy',
        'scikit-learn',
        'text-unidecode==1.0',
        'torch==1.13.1+cpu'
    ],
    dependency_links=["https://download.pytorch.org/whl/torch_stable.html"]
)
