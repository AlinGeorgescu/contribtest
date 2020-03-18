#!/usr/bin/env python3

'''
    generate site from static pages, loosely inspired by Jekyll
    run like this:
        ./generate.py test/source output
    the generated `output` should be the same as `test/expected_output`

    Repaired by: Georgescu Alin-Andrei
'''

import os
import logging
import sys
import json
import jinja2 as j2

LOG = logging.getLogger(__name__)

def list_files(folder_path):
    ''' List files' names and files' paths in folder '''
    for name in os.listdir(folder_path):
        base, ext = os.path.splitext(name)
        if ext != ".rst":
            continue

        yield os.path.join(folder_path, name), base

def read_file(file_path):
    ''' Read a file content and metadata '''
    with open(file_path, "r") as fin:
        raw_metadata = ""
        for line in fin:
            if line.strip() == "---":
                break
            raw_metadata += line

        content = ""
        for line in fin:
            content += line.rstrip().strip()

    return json.loads(raw_metadata), content

def write_output(name, html, output_path):
    ''' Write results in the specified file '''
    if not os.path.isdir(output_path):
        try:
            os.makedirs(output_path, exist_ok=True)
        except OSError:
            logging.error("Failed to create folder %r", output_path)

    with open(os.path.join(output_path, name + ".html"), "w") as fout:
        fout.write(html)

def generate_site(folder_path, output_path):
    '''
    Generate site by parsing input files and writing formated output to out
    files
    '''
    LOG.info("Generating site from %r", folder_path)
    jinja_env = j2.Environment(loader=j2.FileSystemLoader(
        os.path.join(folder_path, "layout")))

    for file_path, name in list_files(folder_path):
        metadata, content = read_file(file_path)
        template_name = metadata.get("layout")
        template = jinja_env.get_template(template_name)
        data = dict(metadata, content=content)
        html = template.render(**data)
        write_output(name, html, output_path)
        LOG.info("Writing %r with template %r", name, template_name)

def main():
    ''' Main '''
    generate_site(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    logging.basicConfig()
    main()
