# -*- coding: utf-8 -*-

import datetime
from models import *
from client_decorator import CosmoDbOperation
from pydocumentdb import document_client
from config import Config


class Repository(object):
    def __init__(self, client, config):
        """
         Repository
        :param client: CosmoDb Client
        :type client: DocumentClient
        :param config: Configuration
        :type config: Config
        """
        self.config = config
        self.client = client

    def save(self, entity):
        try:

            self.client.CreateDocument(self.config.collection_link, entity)
        except Exception as e:
            print e.message

    def update(self, entity):
        try:
            self.client.ReplaceDocument(self.config.document_link(entity['id']), entity)
        except Exception as e:
            print e.message

    def delete(self, id):
        try:

            self.client.DeleteDocument(self.config.document_link(id))
        except Exception as e:
            print e.message

    def get(self, doc_id):
        doc_link = self.config.document_link(doc_id)
        response = self.client.ReadDocument(doc_link)
        return response

    def query(self,query,parameters=None,options=None):
        query = {'query': query}
        result_iterable = self.client.QueryDocuments(self.config.collection_link, query)
        results = list(result_iterable);

