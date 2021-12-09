from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
    # noinspection SpellCheckingInspection
    setup(
        name="mysql-orm",
        version="1.0.0",
        description=(
            "MySQL query tool class used by python."
        ),
        keywords="mysql orm",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author='lyoshur',
        author_email='1421333878@qq.com',
        maintainer='lyoshur',
        maintainer_email='1421333878@qq.com',
        license='MIT License',
        packages=find_packages(),
        platforms=["ubuntu", 'windows'],
        url='https://github.com/lyoshur/myorm',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Operating System :: OS Independent',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: Implementation',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Topic :: Software Development :: Libraries'
        ],
        install_requires=[
            'superorm==1.0.0',
            'PyMySQL',
        ],
        zip_safe=False
    )
