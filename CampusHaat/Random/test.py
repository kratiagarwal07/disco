import MySQLdb, time

conn = MySQLdb.connect(host="35.154.159.250", port=3306,user="admin",passwd="9251640269Guddu",db="campushaat_prod")
c = conn.cursor()

test = c.execute("select * from ads")
print test

for i in range(test):
	out = ""
	row = c.fetchone()
	for data in row:
		out = out + str(data).strip() + "$%"
	print out
