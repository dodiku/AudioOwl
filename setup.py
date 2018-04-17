from setuptools import setup

setup(name='audioanalyzer',
      version='0.0.2',
      description='Fast analysis of music files in Python',
      url='https://github.com/dodiku/audioanalyzer',
      author='Dror Ayalon',
      author_email='d.stamail@gmail.com',
      license='MIT',
      packages=['audioanalyzer'],
      install_requires=[
        'madmom>=0.15.1,<0.15.2',
        'librosa>=0.5.1,<0.5.2',
      ],
      zip_safe=False)
