from persistence.idisposable import IDisposable
from repository import *
from models import DTE
import datetime
from config import Config
from pydocumentdb import document_client

# HOST = 'https://localhost:8081'
# MASTER_KEY = 'C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw=='
# DATABASE_ID = 'cosmosdb-ocgeneral-fc-qa'
# COLLECTION_ID = 'Dte'

HOST = 'https://cosmosdb-ocgeneral-fc-qa.documents.azure.com:443'
MASTER_KEY = 'Zvl2blh8ej3Q6lseWVMgWZ6g1NnYNOam1oxyLa00Mmb40fSHR6SubmdPL7tAd2jCOqdZzGkW4KjZziKFsEVCmg=='
DATABASE_ID = 'cosmosdb-ocgeneral-fc-qa'
COLLECTION_ID = 'Dte'

order = {
          'account_number': 'Account1',
          'purchase_order_number': 'PO18009186470',
          'order_date': datetime.date(2005, 1, 10).strftime('%c'),
          'subtotal': 419.4589,
          'tax_amount': 12.5838,
          'freight': 472.3108,
          'total_due': 985.018,
          }
#


class Order(Entity):
    account_number='',
    purchase_order_number=''
    order_date=''
    subtotal=''
    tax_amount=''
    freight=''
    total_due=''

config =Config(HOST,MASTER_KEY,DATABASE_ID,COLLECTION_ID)
with IDisposable(document_client.DocumentClient(config.host, {'masterKey': config.master_key})) as client:
    repo =Repository(client,config)
    repo.save(entity=order)
    ee=repo.get('1ef33be2-0d5f-4cfc-bb7e-a0b15425780e')
    order=Order().from_dict(ee)
    order.account_number='111111111111111111111111111111111'
    repo.update(order.to_dict())
    tt=repo.query(query='')
    print order.account_number

