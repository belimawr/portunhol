from setuptools import setup


def readme():
    with open('README') as f:
        return f.read()

setup(name='portunhol',
      version='0.2',
      description='A translator from portuguse to portunhol',
      url='https://github.com/belimawr/portunhol/',
      author='Tiago Queiroz',
      author_email='contato@tiago.eti.br',
      license='GPLv3',
      packages=['portunhol'],
      zip_safe=False)
