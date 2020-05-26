import os
import filetype
import sqlite3
from prettytable import PrettyTable

def dump(files, ftype, dest):

    fname = '{}/dump_{}.txt'.format(dest,ftype)
    f = open(fname, 'w')

    for file in files:
        kind = filetype.guess(file)
        if 'xml' in ftype:
            if '.xml' in file:
                fxml = open(file, 'r')
                xml = fxml.read()
                f.write("[+] Dump of %s \n\n" %file)
                f.write(xml)
                f.write("\n\n\n")
        elif 'sqlite' in ftype:
            try:
                if kind.mime == 'application/x-sqlite3':
                    db_data = dump_db(file)
                    f.write("[+] Dump of %s \n" %file)
                    for k, val in db_data.items():
                        f.write("[+] Table %s \n\n" % k)
                        f.write(val)
                        f.write("\n\n\n")

            except AttributeError:
                pass
    try:          
        fxml.close()
    except UnboundLocalError:
        pass
    
    print("[+] Content of the files dumped correctly in %s" % fname)
    f.close()
    


def fast_scandir(dirname):
    filelist = []
    for path, subdirs, files in os.walk(dirname):
        for name in files:
            filelist.append(os.path.join(path, name))
    return filelist

def dump_db(file):

    data = {}

    conn = sqlite3.connect(file)
    conn.text_factory = str
    cur = conn.cursor()

    res = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    table_names = sorted(list(zip(*res))[0])

    for table_name in table_names:
        table = PrettyTable()
        res = cur.execute("PRAGMA table_info('%s')" % table_name).fetchall()
        table.field_names = list(zip(*res))[1]

        res = cur.execute("SELECT * FROM %s;" % table_name).fetchall()

        for row in res:
            table.add_row(row)

        data[table_name] = table.get_string()

    return data

