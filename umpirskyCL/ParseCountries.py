import os

from umpirskyCL.Config import Config


class ParseCountries:
    def __init__(self):
        self.Config = Config()

    def get_list_folders(self, name_folder):
        return os.listdir(self.Config.path + name_folder)

    def parse_line(self, line, folder):
        if line.find('CREATE TABLE') != -1:
            return ''
        if line.isspace() is True:
            return ''

        if self.Config.table_name_in_db:
            line = line.replace('list', self.Config.table_name_in_db)

        if self.Config.name_id:
            line = line.replace('id', self.Config.name_id)

        name = 'value'
        if self.Config.name_value:
            name = self.Config.name_value
            line = line.replace('value', name)

        index = line.find(name)
        index = index + len(name) + 1
        part = line[0:index]
        part = part + ', `' + self.Config.name_language + '`'
        line = part + line[index: len(line)]

        index = line.find(';')
        index = index - 1
        part = line[0:index]
        part = part + ', ' '\'' + folder + '\''
        line = part + line[index: len(line)]

        return line

    def parse(self):
        for folder in self.get_list_folders(self.Config.folder_name):
            file_msql = open(
                self.Config.path + self.Config.folder_name + '/' + folder + '/' + self.Config.name_sql_file)
            file_save = open(self.Config.path + self.Config.file_save_name, 'a')
            print(folder)
            for line in file_msql:
                line = self.parse_line(line, folder)
                file_save.write(line)
