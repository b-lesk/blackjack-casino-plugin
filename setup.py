from setuptools import setup, find_packages

setup(
    name='blackjack-casino-plugin',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A plugin for online gambling casinos that provides Blackjack advice based on detected cards.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'Pillow',
        'opencv-python',
    ],
    entry_points={
        'console_scripts': [
            'blackjack-advisor=blackjack_advisor:main',  # Adjust if you have a main function
        ],
    },
)