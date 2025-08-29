from setuptools import setup, find_packages

setup(
    name="Medical-Chatbot-Langchain",
    version="0.1",
    author="Aditya Sharma",
    author_email="adicodehub@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "langchain",
        "langchain-pinecone",
        "langchain-openai",
        "langchain-community",
        "python-dotenv",
        "pypdf",
        "sentence-transformers",
        "flask",
    ],
)