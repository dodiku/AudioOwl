from setuptools import setup

setup(name='audioowl',
      version='0.0.3',
      description='Fast analysis of music files in Python',
      keywords='Fast audio analysis of music files',
      url='https://github.com/dodiku/AudioOwl',
      author='Dror Ayalon',
      author_email='d.stamail@gmail.com',
      license='MIT',
      packages=['audioowl'],
      install_requires=[
        'madmom>=0.15.1,<0.15.2',
        'librosa>=0.5.1,<0.5.2',
      ],
      zip_safe=False)
