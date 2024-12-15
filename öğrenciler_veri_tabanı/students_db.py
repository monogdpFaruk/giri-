from mongodb_connect import MongoDBConnection

class StudentsDB(MongoDBConnection):
    def __init__(self, db_name):
        super().__init__()
        self.collection = self.database_getir(db_name)['ögrenciSkorları']
    
    def ogrenci_skorlarını_ekleme(self, data:dict):
        self.collection.insert_many(data)
    
    def toplam_puan_sorgulama(self):
        return self.collection.aggregate([
            {
                '$group':{
                    '_id':'$user',
                    "Toplam Puanlar":{'$sum':'$score'}
                }
            }
        ])
    
    # Öğrencilere göre gruplama yapın ve her öğrencinin kaç tane ders aldığını toplayın
    def toplam_ders_sorgulama(self):
        return self.collection.aggregate([
            {
                '$group':{
                    '_id':"$user",
                    "Toplam Dersler":{'$sum': 1}
                }
            }
        ])
     
    # Öğrencileri _id olarak tanımlayın ve öğrencilere göre gruplayın. Buna karşılık olarak her öğrencinin toplam derslerden aldığı ortalama puanı bulunuz.
    def ogrenci_ortalama_puan_hesaplama(self):
        return self.collection.aggregate([
            {
                "$group":{
                    '_id':'$user',
                    'Ortalama_Puanlar':{'$avg':'$score'}
                }
            }
        ])