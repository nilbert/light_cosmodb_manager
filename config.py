class Config(object):
    def __init__(self, host, master_key, database_id, collection_id):
        self.host = host
        self.master_key = master_key
        self.database_id = database_id
        self.collection_id = collection_id

    @property
    def database_link(self):
        return 'dbs/' + self.database_id

    @property
    def collection_link(self):
        return self.database_link + '/colls/' + self.collection_id


    def document_link(self, id):
        return self.collection_link + '/docs/' + id
