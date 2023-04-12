class Database:
    def __init__(self, name):
        self._conn = db.connect(**name)
        self._cursor = self._conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self._cursor.close()
        self._conn.close()

    @property
    def connection(self):
        return self._conn
    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def desc(self):
        return self.cursor.description
    
    def query_tbl(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        self.cursor.description
        return pd.DataFrame.from_records(self.fetchall(), columns = [column[0] for column in self.cursor.description])