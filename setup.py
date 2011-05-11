from setuptools import setup

setup(name='django_books',
      version='0.0.1',
      author='John Weaver',
      author_email='john@pledge4code.com',
      description='A reusable Django app for managing books.',
      url='http://github.com/saebyn/django-books/',
      package_dir={'': 'books'},
      install_requires=[],
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: New BSD License',
        'Programming Language :: Python :: 2.6',
      ],
      platforms=('Any',),
     )
