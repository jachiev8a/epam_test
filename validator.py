#!/usr/bin/env python
# coding=utf-8
"""
Main script validator
"""

from __future__ import print_function
import argparse
import re
import os
from lxml import etree


class XMLSyntaxError(Exception):
    pass


def validate_xml(xml_file):
    # type: (str) -> None
    """Validates XML file structure
    """
    # validate file exist
    if not os.path.exists(xml_file):
        raise IOError("file does not exists: {}".format(xml_file))
    # parse xml
    try:
        doc = etree.parse(xml_file)
        print('XML is well formed, syntax ok.')
    # check for file IO error
    except IOError:
        raise IOError('Invalid File')
    # check for XML syntax errors
    except etree.XMLSyntaxError as err:
        raise XMLSyntaxError("XML Syntax Error in file: {}".format(xml_file))
    except Exception:
        raise Exception('Unknown error, exiting...')


def build_version_name(github_org, git_branch):
    # type: (str, str) -> str
    """Builds a version string from given parameters
    """
    # validate arguments
    if not isinstance(github_org, str) or not isinstance(git_branch, str):
        raise Exception("'github_org' and 'git_branch' should be string type")
    # build version name
    version = 'ci_{organisation}_{branch_name}_SNAPSHOT'.format(
        organisation=github_org,
        branch_name=git_branch)
    return version


def get_file_content(file_name):
    # type: (str) -> str
    """Retrieves the content of a file
    """
    if not os.path.exists(file_name):
        raise IOError("file does not exists: {}".format(file_name))
    with open(file_name) as file_obj:
        content = file_obj.read()
    return content


def validate_snapshot_version(xml_file):
    # type: (str) -> None
    """Validates that xml file contains a valid snapshot version
    """
    xml_content = get_file_content(xml_file)
    #
    version_pattern = re.compile(r'<version>(\d*\.\d*)-SNAPSHOT</version>', re.MULTILINE)
    if not re.search(version_pattern, xml_content):
        raise Exception("invalid SNAPSHOT version at file '{}'".format(xml_file))
    print("XML file '{}' has a valid SNAPSHOT version".format(xml_file))


def replace_version_on_xml(xml_file, new_version):
    # type: (str, str) -> str
    """
    """
    xml_content = get_file_content(xml_file)
    new_xml_content = re.sub(r'\d*\.\d*-SNAPSHOT', new_version, xml_content)
    return new_xml_content


# ---------------
# MAIN
# ---------------
def main():
    """Main Function
    """

    # Script Argument Parser
    parser = argparse.ArgumentParser(description='POM.xml validator')
    parser.add_argument(
        '-x', '--xml_file', required=True,
        help='pom xml file to validate')
    parser.add_argument(
        '-g', '--github_org', required=True,
        help='name of the github organisation')
    parser.add_argument(
        '-b', '--git_branch_name', required=True,
        help='name of the git branch')
    args = parser.parse_args()

    # perform validations on xml file
    try:
        validate_xml(args.xml_file)
    except Exception as detail:
        exit(detail)

    # perform validations on xml content
    try:
        validate_snapshot_version(args.xml_file)
    except Exception as detail:
        exit(detail)

    # build version from parameters given
    version = build_version_name(args.github_org, args.git_branch_name)
    print("New Version built: '{}'".format(version))

    # replace version and retrieve new string
    new_xml_content = replace_version_on_xml(args.xml_file, version)

    with open('NEW_POM.xml', 'w') as file_obj:
        file_obj.write(new_xml_content)
        print("New XML file created: '{}'".format(file_obj.name))


if __name__ == "__main__":
    main()
