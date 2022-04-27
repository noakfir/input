from setuptools import find_packages, setup
setup(
    name='insightsprocessor',
    packages=find_packages(),
    version='1.3.40',
    description='creating a wheel',
    author='noakfir',
    license='MIT',
    install_requires=['pandas', 'numpy', 'scipy', 'matplotlib', 'sklearn', 'PyYAML'],
)
