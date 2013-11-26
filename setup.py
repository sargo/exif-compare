from setuptools import setup, find_packages
import os

name = "exif_compare"
version = "0.1.0"


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


setup(
    name=name,
    version=version,
    description="compare exif metadata",
    long_description=read('README.md'),
    classifiers=[],
    keywords="",
    author="",
    author_email='',
    url='',
    license='MIT',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Flask',
    ],
    entry_points="""
    [console_scripts]
    flask-ctl = exif_compare.script:run

    [paste.app_factory]
    main = exif_compare.script:make_app
    debug = exif_compare.script:make_debug
    """,
)
