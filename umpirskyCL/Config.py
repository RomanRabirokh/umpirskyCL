import os


class Config:
    def __init__(self):
        self.path = os.getcwd() + '/'
        self.folder_name = 'data'
        self.name_sql_file = 'country.mysql.sql'
        self.file_save_name = 'country.sql'
        self.table_name_in_db = 'country_language'
        self.name_id = ''
        self.name_value = ''
        self.name_language = 'language'
