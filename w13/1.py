from configparser import ConfigParser

parser = ConfigParser()
parser.read('database.ini')

db = {}
if parser.has_section('postrgresql'):
    params = parser.items('postrgresql')
    for param in params:
        db[param[0]] = param[1]
    print(db)
else:
    raise Exception('Section postrgresql not found!') 