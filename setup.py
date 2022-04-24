from setuptools import setup, find_packages

setup(
    name="census-consumer-complaint-rk",
    license="MIT",
    version="0.0.0",
    description="Project has been start",
    author="Ravindr Kr",
    packages=find_packages(),
    install_requires=['tfx==1.6.1', 'apache-beam[interactive]', 'apache-airflow']
)
