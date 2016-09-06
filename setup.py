from setuptools import setup


def readme():
      with open('README.rst') as f:
            return f.read()

setup(name='brein-api',
      version='1.1',
      description='Access to Breinify\'s DigitalDNA API',
      url='https://github.com/Breinify/brein-api-library-python',
      author='Breinify',
      author_email='toddbodnar@breinify.com',
      license='MIT',
      long_description=readme(),
      packages=['breinify'],
      install_requires=['requests'],
      classifiers=["Programming Language :: Python :: 3 :: Only",
                   "Development Status :: 5 - Production/Stable",
                   "License :: OSI Approved :: MIT License"],
      zip_safe=False,
      include_package_data=True)
