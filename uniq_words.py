

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                        database='spsta_nepali',
                                        user='root',
                                        password='')


except Error as e:
    print("Error while connecting to MySQL", e)
# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")

file_path=input("Enter path of folder")
from tqdm import tqdm
import glob
import os
count = 0
def database(query):
  if connection.is_connected():
      db_Info = connection.get_server_info()
      print("Connected to MySQL Server version ", db_Info)
      cursor = connection.cursor()
      cursor.execute(query)
      cursor.close()
      record = cursor.commit()
x=[]
# INSERT INTO `dictionary`(`id`, `word_name`) VALUES ('[value-1]','[value-2]')
for root_dir, cur_dir, files in os.walk(file_path): 
      for each_file in files:
        if each_file.split(".")[-1]=="txt" :
          count+=1
          x.append(os.path.join(root_dir, each_file))
print('file count:', count,x)
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        reads=f.read()
    for _ in reads.split():
      query=f"Insert into dictionary('word_name') values ({_.strip()})"
      database(query)

print(x)
# for each_file in x:
  # read_text_file(each_file)
if connection.is_connected():
  # cursor.close()
  connection.close()
  print("MySQL connection is closed")