from setuptools import setup, find_packages

setup(
    name='AssessmentFramework',
    version='0.1',
    license='MIT',
    packages=find_packages{'realisticAF'},
    package_dir={'': 'realisticAF'},
    install_requires=[
        'opencv-python',
        'numpy',
        'pillow',
    ]
)