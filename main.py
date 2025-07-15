# БЭМ с SQL
import sqlite3

class Crud:
    def __init__(self, db_path: str) -> None:
        self._conn = sqlite3.connect(db_path)
        self._cur = self._conn.cursor()

    def create(self, table_name, name, age):
        self._cur.execute(f"""
                          INSERT INTO {table_name} (name,age)
                          VALUES(?, ?)
                          """, (name, age))
        self._conn.commit()

    def read(self, table_name: str) -> None:
        res = self._cur.execute(
            f'SELECT * FROM {table_name}'
            ).fetchall()

        for num, name, age in res:
            print(num, name, age)

    def update(self, table_name: str, id_num: int, name: str, age: int) -> None:
        self._cur.execute(f"""
                          UPDATE {table_name} 
                          SET name='{name}', age={age}
                          WHERE id={id_num} 
                          """)
        self._conn.commit()

    def delete(self, id_num: int, table_name: str) -> None:
        self._cur.execute(f'DELETE FROM {table_name} WHERE id = {id_num}')
        self._conn.commit()


    # method override(переопределяем метод уничтожения объекта)
    def __del__(self):
        self._cur.close()  # отключаем курсор
        self._conn.close()  # отключаемся от БД


db = Crud('./db/movies.sqlite')
db.create('users','Mary', 48)
db.read('users')
db.update('users',8, 'Udjine', 26)
db.delete(10,'users')
