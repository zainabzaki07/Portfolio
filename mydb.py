import sqlite3
conn = sqlite3.connect('portfolio.db')
# data=["ABC","CS-9618","As-Level",4,""]
def query_db(query, args=(), one=False):
    cur = conn.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv
# conn.execute('INSERT INTO reviews (name,subject,level,rating,comments) VALUES (?, ? ,? ,? ,?)',
# (data[0],data[1],data[2],data[3],data[4]))
users={}
for user in query_db('select * from reviews'):
    users[user[0]]=user
# conn.execute('DELETE FROM reviews WHERE id>=11')
# conn.execute('UPDATE sqlite_sequence SET seq=(SELECT count(*) from reviews) WHERE name="reviews"')
# conn.execute('UPDATE reviews SET name="Hitesh Essarani",subject="Computer Science" WHERE id=8')

conn.commit()
conn.close()
for i in users.keys():
    print(users[i])