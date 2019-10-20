import xml.etree.ElementTree as ElementTree
import os


class DocumentReader:

    def __init__(self):
        self.documents = dict()

    def get_document(self):
        return self.documents

    def load_docs(self):

        document_dir_path = "./DocumentStore/papers_to_index_xml"

        xml_files = os.listdir(document_dir_path)

        for xml_file in xml_files:
            file_path = os.path.join(document_dir_path, xml_file)
            tree = ElementTree.parse(file_path)
            root = tree.getroot()

            abstract = ""
            introduction = ""
            title = ""

            for child in root:
                if child.text is None:
                    continue

                if child.tag == 'abstract':
                    abstract = child.text
                elif child.tag == 'introduction':
                    introduction = child.text
                elif child.tag == 'title':
                    title = child.text
                else:
                    raise ValueError(f"{child.tag} tag is not considered in {xml_file}")

            doc = {
                'title': f"{title}",
                'abstract': f"{abstract}",
                'introduction': f"{introduction}",
            }

            self.documents[xml_file] = doc



