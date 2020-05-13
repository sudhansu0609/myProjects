#@author: ad622b
import ijson
import json, ast
import yaml
from _io import open


class json_implementation:

    def search_data_in_file(self, file_path, key):
        file_data=open(file_path, 'r')
        value_dict=dict()
        final_line="No Values found"
        status=False
        for line in file_data:
            if line.__contains__(key)==True:
                print("Data found")
                final_line=line
                status=True
                break
            else:
                print("Data Not found")
                status=False
                continue
        value_dict['status']=status
        value_dict['line_recieved']=final_line
        return value_dict
    
    def replace_txt_in_json(self, file_input_path, file_out_path, key_path, replace_with):
        json_data= open(file_input_path,'r')
        abc = ijson.items(json_data, key_path) 
        columns = list(abc) 
        str_value = str(columns[0])
        print(str_value)        
        json_data = open(file_input_path, 'r')
        data = json.load(json_data)
        data = ast.literal_eval(json.dumps(data))
        print(type(data))
        print(data)
        str_data = str(data)
        updated_json = str_data.replace(str_value, replace_with, 1)
        print(updated_json)
        outfile= open(file_out_path, 'w')
        json.dump(yaml.load(updated_json), outfile)
        return "pass"      
    
    def findjsonkeyval(self, file_input_path, json_key, data_key_num): 
        int_data_key_num = int(data_key_num)
        json_data= open(file_input_path,'r')
        json_items= ijson.items(json_data,json_key)
        #column=list(json_items)
        list_convert=list(json_items)
        output = list_convert[int_data_key_num]
        return output
        
    def getListLength(self, list_val):
        total_count =     len(list_val)
        return    total_count
        
    def write_json_in_File(self, file_path, data):
        json_string=json.dumps(data, sort_keys=True, indent=4)
        datastore=json.loads(json_string)
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(datastore, json_file)
            #json.dumps(yaml.load(data),json_file, ensure_ascii=False)
    def    Remove_Whitespace(self, instring):
        return instring.replace(" ","")
    
    def mergeDictionary(self,dict1,dict2):
        dict1.update(dict2)
        print(dict1)
        return    dict1
