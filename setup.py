from setuptools import find_packages, setup
setup(
    name='insightsprocessor',
    packages=find_packages(),
    version='1.3.39.1',
    description='Service Insights Engine',
    author='Aquant',
    license='MIT',
    install_requires=['pandas', 'numpy', 'scipy', 'matplotlib', 'sklearn', 'PyYAML'],
)