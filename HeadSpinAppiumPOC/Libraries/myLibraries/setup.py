import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
    
setuptools.setup(
     name='myLibraries',  
     version='0.1',
     scripts=['__init__.py'] ,
     author="Sudhansu Kumar Singh",
     author_email="kumarsis@amdocs.com",
     description="Authentication encryption & other features library",
     long_description=long_description,
   long_description_content_type="text/markdown",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )