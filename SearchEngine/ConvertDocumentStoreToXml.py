import os
from os import listdir
from os.path import isfile, join
import shutil

document_store_path = './DocumentStore/papers_to_index'
document_store_path_xml = './DocumentStore/papers_to_index_xml'

if os.path.exists(document_store_path_xml):
    shutil.rmtree(document_store_path_xml)  # , ignore_errors=False, onerror=None)

os.mkdir(document_store_path_xml)

only_files = [f for f in listdir(document_store_path) if isfile(join(document_store_path, f))]

for only_file in only_files:
    file = join(document_store_path, only_file)
    with open(file, 'r') as content_file:
        content = content_file.read()

    with open(join(document_store_path_xml, only_file), 'a') as new_file:
        new_file.write('<data>')
        new_file.write(content)
        new_file.write('</data>')
