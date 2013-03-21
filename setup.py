import setuptools

entry_points = '''
[console_scripts]
myscript = somecode:main
'''

setuptools.setup(
    name="mydemo",
    version="0",
    author="Fred",
    author_email="fred@zope.com",
    description="Demo package",
    install_requires=[
        'setuptools',
        'zc.buildout',
        ],
    entry_points=entry_points,
    package_dir={'': 'src'},
    zip_safe=False,
    pymodules=["somecode"],
    )
