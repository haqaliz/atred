from setuptools import setup

setup(name='atred',
      version='0.0.1',
      description='Atred',
      url='http://github.com/storborg/funniest',
      author='Ali Alizade Haqiqi',
      author_email='haqaliz@aol.com',
      license='MIT',
      packages=['atred'],
      install_requires=[
            'torch',
            'spacy',
            'gensim',
            'transformers',
            'adaptnlp',
            'grpcio',
            'python-dotenv',
            'en_core_web_sm @ https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz'
      ],
      zip_safe=False)