from setuptools import setup, find_packages

setup(
    name='core',
    version='0.1',
    packages=["core", "blog", "media", "profile"],
    # packages=find_packages(),
    include_package_data=True,  # to include non-Python files like templates, static
    install_requires=[
        'django>=3.2',  # specify your dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
)
