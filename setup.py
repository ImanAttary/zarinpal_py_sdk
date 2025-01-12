from setuptools import setup, find_packages

setup(
    name='zarinpal-py-sdk',               
    version='0.1.3',                      
    packages=find_packages(where="src"), 
    include_package_data=True,  
    py_modules=['zarinpal'],   
    package_dir={"": "src"},              
    install_requires=[
        "anyio==4.7.0",
        "attrs==24.2.0",
        "certifi==2024.8.30",
        "cffi==1.17.1",
        "charset-normalizer==3.3.2",
        "chromedriver-autoinstaller==0.6.4",
        "colorama==0.4.6",
        "crypto==1.4.1",
        "cryptography==44.0.0",
        "dnspython==2.7.0",
        "docutils==0.21.2",
        "email_validator==2.2.0",
        "h11==0.14.0",
        "httpcore==1.0.7",
        "httpx==0.28.1",
        "idna==3.10",
        "iniconfig==2.0.0",
        "jaraco.classes==3.4.0",
        "jaraco.context==6.0.1",
        "jaraco.functools==4.1.0",
        "jsonschema==4.23.0",
        "jsonschema-specifications==2024.10.1",
        "keyring==25.6.0",
        "logging==0.4.9.6",
        "markdown-it-py==3.0.0",
        "mdurl==0.1.2",
        "more-itertools==10.5.0",
        "Naked==0.1.32",
        "nh3==0.2.20",
        "outcome==1.3.0.post0",
        "packaging==24.2",
        "pkginfo==1.12.0",
        "pluggy==1.5.0",
        "psutil==6.1.0",
        "pycparser==2.22",
        "pycryptodome==3.21.0",
        "Pygments==2.19.1",
        "pyotp==2.9.0",
        "pyperclip==1.9.0",
        "PySocks==1.7.1",
        "pytest==8.3.4",
        "pytest-order==1.3.0",
        "python-dotenv==1.0.1",
        "PyYAML==6.0.2",
        "readme_renderer==44.0",
        "referencing==0.35.1",
        "requests==2.32.3",
        "requests-mock==1.12.1",
        "requests-pkcs12==1.25",
        "requests-toolbelt==1.0.0",
        "responses==0.25.3",
        "rfc3986==2.0.0",
        "rich==13.9.4",
        "rpds-py==0.20.0",
        "selenium==4.27.1",
        "setuptools==75.8.0",
        "shellescape==3.8.1",
        "sniffio==1.3.1",
        "sortedcontainers==2.4.0",
        "trio==0.27.0",
        "trio-websocket==0.11.1",
        "twine==6.0.1",
        "typing_extensions==4.12.2",
        "urllib3==2.2.3",
        "webdriver-manager==4.0.2",
        "websocket-client==1.8.0",
        "wheel==0.45.1",
        "wsproto==1.2.0",
    ],
    author='Iman Attary',                   
    author_email='imanattary@gmail.com',
    description='A Python SDK for Zarinpal Payment Gateway',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ImanAttary/zarinpal_py_sdk',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',              
)