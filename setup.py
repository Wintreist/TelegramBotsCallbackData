from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='TelegramBotsCallbackData',
  version='16.10.2023',
  author='Wintreist',
  author_email='wintreist1811@gmail.com',
  description='This is a library for storing a lot of information in callback data',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='files speedfiles ',
  project_urls={
    'GitHub': 'your_github'
  },
  python_requires='>=3.6'
)