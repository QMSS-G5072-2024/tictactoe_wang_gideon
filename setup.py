from setuptools import setup, find_packages

setup(
    name='tictactoe_zw3055',
    version='0.1',
    author='Zack Wang',
    author_email='zw3055@columbia.edu',
    description='A Tic Tac Toe game package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/QMSS-G5072-2024/tictactoe_wang_zack',
    packages=find_packages(),
    install_requires=[],  # 依赖库，例如 ['numpy', 'pandas']
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

