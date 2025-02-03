from setuptools import find_packages,setup # type: ignore

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='msswaroop',
    author_email='santhiswaroop8040@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)