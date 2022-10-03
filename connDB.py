import cx_Oracle
import enviroments


class ConnOracle:
    def __init__(self, username, password, dsn, port = 1521, encoding = 'UTF-8'):
        self.username   = username;
        self.password   = password;
        self.dsn        = dsn;
        self.port       = port;
        self.encoding   = encoding;

 
    conn = cx_Oracle.connect(
            enviroments.username,
            enviroments.password,
            enviroments.dsn,
            encoding=enviroments.encoding)

    @staticmethod
    def query(select):
        try:
            cur = ConnOracle.conn.cursor()
            cur.execute(select)
            resp = cur.fetchall()
            for n in resp:
                print(n)
                   
        except cx_Oracle.Error as error:
            print(error)
        finally:
            if ConnOracle.conn:
                ConnOracle.conn.close()


ConnOracle.query('select * FROM COMUNA')