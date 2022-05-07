from setuptools import setup
from cyeld import __version__

setup(name='cyeld',
      version=__version__,
      license='MIT License',
      install_requires=['numpy'],
      description='Deep Learning Framework from Cyeld',
      author='Kaito Oshiro',
      author_email='kaitooshiro7@gmail.com',
      url='https://github.com/kaitoohsiro/Cyeld',
      packages=['cyeld'],
      )