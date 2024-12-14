from mongodb_connect import MongoDBConnection

class booksDB(MongoDBConnection):
    def __init__(self, db_name):
        super().__init__()  # MongoDBConnection sınıfının __init__ metodunu çağırır
        self.collection = self.database_getir(db_name)['Books']  # Veritabanındaki 'Books' koleksiyonuna erişim

    def kitaplar_ekleme(self, data: dict):
        self.collection.insert_many(data)  # Birden fazla belge ekler

    def kitap_id_ve_isim_sorgulama(self):
        # 'aggregate()' metodunu doğru bir şekilde kullanarak 'title' ve 'isbn' alanlarını döndürme
        return self.collection.aggregate([
            {'$project': {'title': 1, 'isbn': 1}}  # Sadece 'title' ve 'isbn' alanlarını döndürür
        ])
