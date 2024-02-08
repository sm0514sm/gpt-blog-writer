from setuptools import setup, find_packages

setup(
  name='gpt-blog-writer',
  version='1.0',
  packages=find_packages(
    include=['connector', 'connector.*', 'entity', 'entity.*', 'repository', 'repository.*', 'service', 'service.*']),
  install_requires=[
    'openai==1.11.1',
    'pip==24.0',
    'requests==2.31.0',
    'setuptools==69.0.3',
    'urllib3==2.2.0',
    'wheel==0.42.0',
    'beautifulsoup4~=4.12.3',
    'selenium~=4.17.2'
  ]
)
