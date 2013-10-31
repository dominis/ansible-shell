from distutils.core import setup

setup(
    name='ansible-shell',
    version='0.0.2',
    author='Nandor Sivok',
    author_email='dominis@haxor.hu',
    scripts=['ansible-shell'],
    url='https://github.com/dominis/ansible-shell',
    description='Interactive shell for ansible',
    install_requires=[
        "ansible >= 1.3"
    ],
)
