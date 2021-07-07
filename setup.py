# coding=utf-8


from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(name='ucnumber',
      version='0.1.2',
      description='Validate UC alumni identifier numbers.',
      url='https://github.com/mrpatiwi/uc-numero-alumno-python',
      author='Patricio López',
      long_description=readme,
      long_description_content_type= 'text/markdown',
      author_email='patricio@lopezjuri.com',
      license='MIT',
      packages=['ucnumber'],
      keywords=['uc', 'puc', 'chile', 'numero', 'alumno'],
      zip_safe=False)
