from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    author='John McClary',
    author_email='jmcgue@gnosiscompanies.com',
    description='A Python API wrapper for interacting with Knack applications.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
      'pytz',
      'requests'
    ],
    keywords='knack api api-client integration python',
    license='Public Domain',
    name='knackpy',
    packages=['knackpy'],
    test_suite='nose.collector',
    tests_require=['nose'],
    url='https://github.com/gnosisfreight/knackpy',
    version='0.2.0',
)