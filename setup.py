from setuptools import setup

setup(name = 'django-books',
      version = '0.0.1',
      author = 'John Weaver',
      author_email = 'john@saebyn.info',
      description = 'A Django reusable app for managing books.',
      long_description = open('README.rst').read(),
      url = 'http://github.com/saebyn/django-books/',
      packages = ['django_books'],
      license = 'BSD',
      classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
      ],
)
