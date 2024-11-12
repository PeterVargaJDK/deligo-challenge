from setuptools import setup, find_packages

PROD_PACKAGES = [
    'fastapi[standard]',
    'starlette',
    'pydantic',
    'pydantic-settings',
    'uvicorn',
    'numpy',
    'scikit-learn'
]

DEV_PACKAGES = [
]

TEST_PACKAGES = [
    'pytest',
    'pytest-asyncio',
    'locust'
]

setup(
    name='Deligo Challenge',
    version='0.0.0',
    packages=find_packages(),
    install_requires=PROD_PACKAGES,
    extras_require={
        'dev': PROD_PACKAGES + TEST_PACKAGES + DEV_PACKAGES,
        'test': PROD_PACKAGES + TEST_PACKAGES,
    },
)
