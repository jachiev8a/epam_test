# Overview
**validator.py** is the main script

python version required: **2.7.8** or **higher**

# Dependencies
- lxml
- pytest

## How to install dependencies
You have to use pip in order to install python dependencies
```
python -m pip install lxml
python -m pip install pytest
```

# Script Parameters

There are 3 script parameters:

1. **-x**/**--xml_file**: xml file to validate and replace version
2. **-g**/**--github_org**: Name of the GitHub Organisation
2. **-b**/**--git_branch_name**: Name of the Git branch

## How to execute script?
```
python validator.py -x pom.xml -g MY_ORG -b MY_BRANCH
```
or
```
python validator.py --xml_file pom.xml --github_org MY_ORG --git_branch_name MY_BRANCH
```

## Script Output
This script will not overwrite the loaded xml file, this will write a new one instead. 
This new file is called **NEW_POM.xml** on the root of the project

# Unit test
There are unit tests contained inside 'tests' directory and they are axecuted with pytest

## How to run unit tests?
in the root of the folder, open a command line window and type:
```
python -m pytest -v
```
This will autorecursive the directories, looking for python test files
