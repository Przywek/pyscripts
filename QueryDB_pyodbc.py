import pyodbc
import datetime

def Query (driver,select):
    connection = pyodbc.connect(driver)
    cursor = connection.cursor()
    cursor.execute(select)
    sf = []
    for row in cursor:
        sf.append(row)
    return sf

def Query_concept_db(db_name):
    driver_db = 'Driver={SQL Anywhere 16};'' \
    ''Server=servo;'' \
    ''Database='+db_name+';'' \
    ''UID=user;'' \
    ''pwd=user;'
    a_rest = []
    rest= Query(driver_db,'select obj_num,ob_active from micros.em_store_def where obj_num != 1')
    for x,y in rest:
        if len(x)>4 and y == 1:
          a_rest.append(list(x))
    return a_rest

def Query_db_name():
    driver = 'Driver={SQL Anywhere 16};'' \
    ''Server=servo;'' \
    ''Database=db;'' \
    ''UID=custom;'' \
    ''pwd=custom;'
    db_name = Query(driver,"select db_name from micros.em_concept_def where  server_name ='servo' and db_name !='db' and db_available=1")
    return db_name

def Query_last_dep(db_name, mpk):
    driver_db = 'Driver={SQL Anywhere 16};'' \
    ''Server=servo;'' \
    ''Database=' + db_name + ';'' \
    ''UID=db;'' \
    ''pwd=db;'
    yesterday = (datetime.datetime.now() - datetime.timedelta(1)).strftime('%Y-%m-%d')
    pack_infos = Query(driver_db,  "select package_name, deployed_on, status, status_text from package_transport_dtl where deployed_on>'" + yesterday + "%'  and status!=1")
    check_mecu = []
    while True:
        if len(pack_infos) == 0:
            return ("ALL PACKAGES LOADED" + db_name)
            break
        else:
            for a in mpk:
                that = str("S1_D" + a)
                for list in pack_infos:
                    for x, y, z, v in zip(list[0::1],list[1::2],list[2::3],list[3::4]):
                        if that in x and z != 1:
                            if z == -1:
                                check_mecu.append(list(a,x, y[:9], z, 'NOT LOADED'))
                            elif z == 2:
                                check_mecu.append(list(a,x, y[:9], z, 'PACKAGES OUT OF SYNC'))
                            else:
                                check_mecu.append(list(a,x, y[:9], z, v))
            break
    return check_mecu
