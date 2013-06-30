from distutils.core import setup

setup(
    name='AnsibleShell',
    version='0.0.1',
    author='Nandor Sivok',
    author_email='dominis@haxor.hu',
    scripts=['ansible-shell.py'],
    url='https://github.com/dominis/ansible-shell',
    description='Interactive shell for ansible',
    long_description=open('README.md').read(),
    install_requires=[
        "ansible >= 1.2"
    ],
)
