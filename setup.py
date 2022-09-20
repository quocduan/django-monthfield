'''Still needs some work to properly include the test_site and sqlite db'''
import month as meta
import setuptools
from setuptools import setup

setup(
    # name='django-monthfield',
    name=meta.__title__,
    # version='1.0.0',
    version=meta.__version__,
    author=u'Quoc Duan',
    author_email='quocduan@gmail.com',
    # packages=['month'],
    packages=setuptools.find_packages(),
    include_package_data=True,
    url='https://github.com/quocduan/django-monthfield.git',
    license='BSD licence, see LICENCE',
    description='Provides a field for storing months (YYYY-MM) on django models.',
    long_description=open('README.rst').read(),
    zip_safe=False,
    python_requires='>=3.7, <4',
    install_requires=[
        'djangorestframework>=3.9,<4',
    ],
)
