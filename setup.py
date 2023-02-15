from setuptools import setup, find_packages

setup(
  name='gpt-blog-writer',
  version='1.0',
  packages=find_packages(
    include=['connector', 'connector.*', 'entity', 'entity.*', 'repository', 'repository.*', 'service', 'service.*']),
  install_requires=[
    'aiohttp==3.8.4'
    'aiosignal==1.3.1',
    'async-timeout==4.0.2',
    'attrs==22.2.0',
    'certifi==2022.12.7',
    'charset-normalizer==3.0.1',
    'colorama==0.4.6',
    'frozenlist==1.3.3',
    'idna==3.4',
    'Markdown==3.4.1',
    'multidict==6.0.4',
    'openai==0.26.5',
    'requests==2.28.2',
    'tqdm==4.64.1',
    'urllib3==1.26.14',
    'yarl==1.8.2',
  ]
)