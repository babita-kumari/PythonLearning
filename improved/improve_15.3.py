"""
Write a program to create table Artist, Album,Genre and Track. Parse the artist,album,genre and track detail
from given xml file and prepare a database by joining all the table and
sort the contents based  on and artist name and print it till limit 3.

"""

import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('assignment12_sql.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''

CREATE TABLE IF NOT EXISTS Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

print("Tables created successfully")


def lookup(d, key):
    found = False
    for child in d:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

class MultipleSqlDatabaseLink:

    def get_input(self):
        fname = input('Enter file name: ')
        if (len(fname) < 1): fname = 'Library.xml'
        return fname

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>

    def parse_file(self,fname):
        stuff = ET.parse(fname)
        all = stuff.findall('dict/dict/dict')
        for entry in all:
            if (lookup(entry, 'Track ID') is None): continue
            name = lookup(entry, 'Name')
            artist = lookup(entry, 'Artist')
            album = lookup(entry, 'Album')
            genre = lookup(entry, 'Genre')
            count = lookup(entry, 'Play Count')
            rating = lookup(entry, 'Rating')
            length = lookup(entry, 'Total Time')


            if name is None or artist is None or genre is None or album is None :
                continue

            print(name, artist,genre, album, count, rating, length)

            cur.execute('''INSERT OR IGNORE INTO Artist (name) 
                VALUES ( ? )''', ( artist, ) )
            cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
            artist_id = cur.fetchone()[0]

            cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
                VALUES ( ?, ? )''', ( album, artist_id ) )
            cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
            album_id = cur.fetchone()[0]

            cur.execute('''INSERT OR IGNORE INTO Genre (name) 
                    VALUES ( ? )''', ( genre, ) )
            cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
            genre_id = cur.fetchone()[0]

            cur.execute('''INSERT OR REPLACE INTO Track
                (title, genre_id, album_id, len, rating, count) 
                VALUES ( ?, ?, ?, ?, ?, ? )''',
                ( name,genre_id, album_id, length, rating, count ) )

        conn.commit()
        return conn

    def print_result(self):

        sqlstr = ( '''SELECT Track.title, Artist.name, Album.title, Genre.name 
        FROM Track JOIN Genre JOIN Album JOIN Artist 
        ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
            AND Album.artist_id = Artist.id
        ORDER BY Artist.name LIMIT 3''')

#cur.execute(sqlstr)
        for row in cur.execute(sqlstr):
            print(row[0], row[1], row[2], row[3])

        cur.close()

    def processes(self):
        input=self.get_input();
        file=self.parse_file(input)
        self.print_result()

song_dict=MultipleSqlDatabaseLink()
song_dict.processes()

