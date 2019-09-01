from setuptools import setup, find_packages

setup(
    name='botball',
    packages=find_packages(),
    version='0.1.3',
    license='MIT',
    description='Typed Python wrappers for useful Botball components',
    author='Wilson Gramer',
    author_email='wgramer03@gmail.com',
    url='https://github.com/tyngsboroughrobotics/botball',
    download_url='https://github.com/tyngsboroughrobotics/botball/archive/v0.1.3.tar.gz',
    keywords=['botball', 'wallaby', 'libwallaby'],
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
