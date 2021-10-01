from setuptools import setup, find_packages
import versioneer

# read the contents of your README file
with open('README.md') as f:
    long_description = f.read()
    
setup(
    name='yeast-spotifier',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    test_suite="tests",
    url='https://github.com/mmagnus/yeast-spotifier',
    scripts=['spotifier.py',
             'digitifier.py',
             'spotifier_prep.py',
             ],
    license='GPLv3',
    author='Marcin Magnus',
    author_email='mag_dex@o2.pl',
    description='a script to process yeast plate image into figures',
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[
        'pillow',
        'psd-tools3',
       ],
)
