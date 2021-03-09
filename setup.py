from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name='Export2D',
    version='0.1.0',
    description='A utility for Fusion 360 to import multiple DXF files.',
    long_description=long_description,
    packages=['Export2D', 'Export2D.apper.apper', 'Export2D.commands'],
    package_data={
        "": ["resources/*", "resources/**/*", "*.manifest", "LICENSE", "lib/Place_3rd_Party_libraries_here.txt"],
    },
    url='https://github.com/tapnair/Export2D',
    license='MIT',
    author='Patrick Rainsberry',
    author_email='patrick.rainsberry@autodesk.com',
)
