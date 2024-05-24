from setuptools import setup, find_packages

setup(
    name='goit-phone-book-bot',
    version='0.0.8',
    author='Vasyl Martyniv',
    author_email='doc.people97@gmail.com',
    description='Phone Book bot developed by team #5 - CREATORS',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/VasylMartyniv/GoIT_Phone_Book_bot',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'pyreadline3',
        'tabulate',
    ],
    entry_points={
        'console_scripts': [
            'goit-phone-book-bot=src.main:main',
        ],
    },
)
