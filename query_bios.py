import pymysql


def connection():
    return pymysql.connect(host='127.0.0.1', user='root', passwd='16769thSQL', database='biography_search')

def find_relevant_bios(era, region, occupation):
    mydb = connection()

    mycursor = mydb.cursor()
    query = "select * from biographies where era = '{}' and region = '{}' and Occupation = '{}'".format(int(era), int(region), int(occupation))

    mycursor.execute(query)

    res = mycursor.fetchall()
    print(res)
    return res