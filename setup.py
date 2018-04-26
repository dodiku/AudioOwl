from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='audioowl',
      version='0.0.4',
      description='Fast and simple music and audio analysis using RNN in Python',
      long_description=readme(),
      classifiers=[
          'Development Status :: 2 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Topic :: Audio Analysis :: Music',
      ],
      keywords='Fast and simple music and audio analysis using RNN in Python',
      url='https://github.com/dodiku/AudioOwl',
      author='Dror Ayalon',
      author_email='d.stamail@gmail.com',
      license='MIT',
      packages=['audioowl'],
      install_requires=[
        'llvmlite>=0.22.0,<0.22.1',
        'numba>=0.37.0<0.37.1',
        'numpy>=1.13.3,<1.13.4',
        'scipy>=1.0.0,<1.0.1',
        'cython',
        'madmom>=0.15.1,<0.15.2',
        'librosa>=0.5.1,<0.5.2',
      ],
      include_package_data=True,
      zip_safe=False)
