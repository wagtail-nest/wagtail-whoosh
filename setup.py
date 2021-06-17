import os

from setuptools import find_packages, setup
from wagtail_whoosh import __version__

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='wagtail-whoosh',
    version=__version__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    license='BSD License',
    description='Whoosh backend for Wagtail CMS',
    long_description='Whoosh backend for Wagtail CMS',
    url='https://github.com/wagtail/wagtail-whoosh',
    author='Michael Yin',
    author_email='admin@michaelyin.info',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        "Django>=2.0,<3.0",
        "Wagtail>=2.3,<2.12",
        "Whoosh>=2.7,<2.8",
    ],
    test_suite='runtests.runtests'
)
