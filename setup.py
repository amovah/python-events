from setuptools import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
    name="events",
    version="1.0.0",
    description="Simple event emitter library",
    url="https://github.com/amovah/python-events",
    author="Ali Movahedi",
    author_email="ali_movahedi@aol.com",
    license="MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5'
    ],
    keywords="event emitter",
    packages=['events'],
    long_description=long_description
)
