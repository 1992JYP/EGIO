from setuptools import setup

setup(
    name='script',          # 이건 설치툴 이름
    version='0.1.0',
    py_modules=['yourscript'],  # 여기가 파일이름인듯
    install_requires=[      # 설치필요 모듈
        'Click',
    ],
    entry_points={
        'console_scripts':[
            'script = script:cli'
        ]
    }
)