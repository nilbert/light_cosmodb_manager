from pydocumentdb import document_client

from persistence.idisposable import IDisposable
from functools import partial

HOST = 'https://cosmosdb-ocgeneral-fc-qa.documents.azure.com:443/'
MASTER_KEY = 'Zvl2blh8ej3Q6lseWVMgWZ6g1NnYNOam1oxyLa00Mmb40fSHR6SubmdPL7tAd2jCOqdZzGkW4KjZziKFsEVCmg=='


def cosmodb():
    with IDisposable(document_client.DocumentClient(HOST, {'masterKey': MASTER_KEY})) as client:
        def inner(func):
            return partial(func, client)

        return inner


class CosmoDbOperation(object):
    def __init__(self, config):
        self.config = config

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            kwargs_copy = kwargs.copy()
            with IDisposable(document_client.DocumentClient(self.config['HOST'],
                                                            {'masterKey': self.config['MASTER_KEY']})) as client:
                kwargs_copy.update({'client': client})
                return func(*args, **kwargs_copy)

        return wrapper
