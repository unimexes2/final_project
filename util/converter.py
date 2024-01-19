
    
class Converter:
  
   def convert_csv_cachier(self, data_frame,data, *args) -> list:
        obj_list = []
        for index, row in data_frame.iterrows():
       
            el = data(row['name'], row['dni'], row['age'], row['timetable'], row['salary']) 
            obj_list.append(el)
        return obj_list

   def convert_csv_user(self, data_frame,data, *args) -> list:
        obj_list = []
        for index, row in data_frame.iterrows():
       
            el = data(row['name'], row['dni'], row['age'], row['email'], row['postalcode']) 
            obj_list.append(el)
        return obj_list
   
   def convert_csv_product(self, data_frame,data, *args) -> list:
        obj_list = []
        for index, row in data_frame.iterrows():
       
            el = data(row['id'], row['name'], row['price']) 
            obj_list.append(el)
        return obj_list

    
   def print(self, obj_list):
        for obj in obj_list:
            obj.describe()
            print()
            

class CSVConverter(Converter):
    
    def convert(self, data_frame, *args) -> list:
        obj_list = []
        for index, row in data_frame.iterrows():
            obj = args[0](row['id'], row['name'], row['price'])  
            obj_list.append(obj)
        return obj_list 