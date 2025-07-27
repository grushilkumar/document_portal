import os
from utils.model_loader import ModelLoader
from exception.custom_exception import DocumentPortalException
from model.models import *
from langchain_core.output_parsers import JsonOutputParserer
from langchain.output_parsers import OutputFixingParser

class DocumentAnalyser:
    """
    A class to handle document analysis using loaded models.
    """

    def __init__(self):
        pass

    def analyse_metadata(self):
        """
        Analyse the document and return structured data.
        """

        pass
