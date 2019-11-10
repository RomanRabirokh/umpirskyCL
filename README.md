## umpirskyCL


## English

The script allows you to easily and quickly compile a list of countries into one slq file, taking into account the language in one table, from the repository [umpirsky/country-list](https://github.com/umpirsky/country-list)

### Launch
To start, you need to run the main.py script, set the necessary settings and download the folder data from the umpirsky/country-list project

### Settings

#### Config.py File

**path** absolute path to the file, do not change

**folder_name** name of the folder in which the data folder downloaded from umpirsky/country-list is contained, data folder

**name_sql_file** file name from the umpirsky/country-list project that contains the requests (do not change if the file name has not changed)

**file_save_name** name of the linked outgoing file

**name_id** new id name from umpirsky/country-list data sql file, leave empty if no change is needed

**name_value** new name value from umpirsky/country-list data sql file, leave empty if no change is needed

**name_language** name of the language parameter, which is taken from the name of the folders

### Example

For example, this configuration:
```python
    class Config:
    def __init __ (self):
        self.path = os.getcwd () + '/'
        self.folder_name = 'data'
        self.name_sql_file = 'country.mysql.sql'
        self.file_save_name = 'country.sql'
        self.table_name_in_db = 'country_language'
        self.name_id = ''
        self.name_value = ''
        self.name_language = 'language'
```
It will issue such requests:
```sql
    INSERT INTO `country_language` (` id`, `value`,` language`) VALUES ('UG', 'Uganda', 'en_GB');
    INSERT INTO `country_language` (` id`, `value`,` language`) VALUES ('UA', 'Ukraine', 'en_GB');
    INSERT INTO `country_language` (` id`, `value`,` language`) VALUES ('AE', 'United Arab Emirates', 'en_GB');
```

## Russian

Скрипт позволяет легко и быстро скомпоновать в один slq файл список стран, с учетом языка в одину таблицу, из репозитория 
[umpirsky/country-list](https://github.com/umpirsky/country-list)

### Запуск
Для запуска нужно запустить скрипт main.py, установить нужные настройки и скачать папку data из проекта umpirsky/country-list

### Настройки

#### Файл Config.py

**path** абсолютный путь к файлу, не менять

**folder_name** имя папки в которой соержится выкачанная из umpirsky/country-list, папка data

**name_sql_file** имя файла с проекта umpirsky/country-list, в котором содержется запросы( не менять, если имя фала не поменялось)

**file_save_name** имя скомпонованого исходящего файла

**name_id** новое имя id из файла umpirsky/country-list data sql, оставить пустым если не нужно изменение 

**name_value** новое имя value из файла umpirsky/country-list data sql, оставить пустым если не нужно изменение 

**name_language** имя параметра языка, который берется из названия папок

### Пример

Например такая конфигурация:
```python
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
```
Выдаст такие запросы:
```sql
    INSERT INTO `country_language` (`id`, `value`, `language`) VALUES ('UG', 'Uganda', 'en_GB');
    INSERT INTO `country_language` (`id`, `value`, `language`) VALUES ('UA', 'Ukraine', 'en_GB');
    INSERT INTO `country_language` (`id`, `value`, `language`) VALUES ('AE', 'United Arab Emirates', 'en_GB');
```
