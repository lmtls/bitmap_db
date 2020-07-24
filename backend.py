import sqlite3
import numpy as np
import cv2

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS bitmap (id INTEGER PRIMARY KEY,name TEXT,row0 TEXT,row1 TEXT,row2 TEXT,row3 TEXT,row4 TEXT,row5 TEXT,row6 TEXT,row7 TEXT)")
        self.con.commit()

    def view_simple(self, name):
        self.cur.execute("SELECT id,name FROM bitmap")
        rows=self.cur.fetchall()
        return rows

    def view_all(self):
        self.cur.execute("SELECT * FROM bitmap")
        rows=self.cur.fetchall()
        return rows

    def add(self, name, r0, r1, r2, r3, r4, r5, r6, r7):
        self.cur.execute("INSERT INTO bitmap (name,row0,row1,row2,row3,row4,row5,row6,row7) VALUES (?,?,?,?,?,?,?,?,?)", (name,r0,r1,r2,r3,r4,r5,r6,r7))
        self.con.commit()

    def delete(self, id):
        self.cur.execute("DELETE FROM bitmap WHERE id=?", (id,))
        self.con.commit()

    def update(self, id, name, r0, r1, r2, r3, r4, r5, r6, r7):
        self.cur.execute("UPDATE bitmap SET name=?,row0=?,row1=?,row2=?,row3=?,row4=?,row5=?,row6=?,row7=? WHERE id=?", (name,r1,r2,r3,r4,r5,r6,r7,id))
        self.con.commit()

    def search_by_name(self, name):
        self.cur.execute("SELECT FROM bitmap WHERE name=?", (name,))
        rows=self.cur.fetchall()
        return rows

    def search_by_id(self, id):
        self.cur.execute("SELECT * FROM bitmap WHERE id=?", (id,))
        rows=self.cur.fetchall()
        return rows[0]

    def delete_all(self):
        self.cur.execute("DELETE FROM bitmap")
        self.con.commit()

    def __del__(self):
        self.con.close()

class BitMapImage():
    def create(self, tuple):
        data = [list(row) for row in list(tuple[2:])]
        new_data = [[255 if num=='1' else 0 for num in row] for row in data]
        image = np.asarray(new_data)
        cv2.imwrite('{}.png'.format(tuple[1]), image)
        return tuple[1] + '.png'
    