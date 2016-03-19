from setuptools import setup

setup(
    name='ansible-shell',
    version='0.0.5',
    author='Nandor Sivok',
    author_email='dominis@haxor.hu',
    scripts=['ansible-shell'],
    url='https://github.com/dominis/ansible-shell',
    description='Interactive shell for ansible',
    install_requires=[
        "ansible >= 1.9",
        "markupsafe"
    ],
)
