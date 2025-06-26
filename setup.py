from setuptools import setup, find_packages

setup(
    name='captcha-hydra',
    version='1.0',
    packages=find_packages(),
    install_requires=['requests', 'beautifulsoup4'],
    entry_points={
        'console_scripts': [
            'captcha-hydra = captcha_hydra.main:brute_force',
        ],
    },
    author='Your Name',
    description='A brute-force tool for login forms with arithmetic CAPTCHA solving',
    license='MIT',
    keywords='brute-force captcha kali-linux',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ]
)
