from setuptools import find_packages, setup

import django_keygen


def load_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


setup(name='django-keygen',
      version=django_keygen.__version__,
      author=django_keygen.__author__,
      packages=find_packages(),
      keywords='Django Secret Key',
      description='A secure secret key generator for Django',
      long_description=django_keygen.__doc__,
      long_description_content_type='text/rst',
      classifiers=[
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python'
          'Intended Audience :: Developers',
          'Environment :: Web Environment',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
      ],
      license='GPL v3',
      python_requires='>=3.5',
      install_requires=load_requirements(),
      include_package_data=True
      )
