import mysql.connector
import tabulate

cnx = mysql.connector.connect(
    user='root',
    passwd='0018',
    database='12th_record',
    host='localhost'
)

cursor = cnx.cursor()

def run_and_show(cursor, query):
    cursor.execute(query)
    output = cursor.fetchall()
    print(tabulate.tabulate(output, tablefmt='grid'))


print(" PS 1 - display total earnings of each agency ")
q = 'SELECT Agency, SUM(Package_Amt) from Tourist group by Agency;'
run_and_show(cursor, q)

print(" PS 2 - display the name of the tourist and their destination ")
q = 'select Tourist.Name, Places.Name from Tourist, Places where Tourist.Tcode = Places.Tcode'
run_and_show(cursor, q)

print(" PS 3 - display the count of places where the name starts with 'a'")
q = "select count(Name) from Places where Name like 'A%';"
run_and_show(cursor, q)

print(" PS 4 - display the maximum, minimum and total package from tourist table ")
q = "SELECT MAX(Package_Amt), MIN(Package_Amt), SUM(Package_Amt) from Tourist;"
run_and_show(cursor, q)

print(" PS 5 - select all tourist where age is 21, 23 or 26 ")
q = 'SELECT * FROM TOURIST WHERE Age in (21, 23, 26);'
run_and_show(cursor, q)

print(" PS 6 show hardeep, kavita and Medha's package_amt and location")
q = 'select Tourist.Name, Places.Name, Tourist.Package_Amt from Tourist, Places where Tourist.Tcode = Places.Tcode and Tourist.Name in ("Hardeep", "Kavita", "Medha");'
run_and_show(cursor, q)

print(" PS 7 display the tourist details in descending order of their name")
q = 'SELECT * FROM TOURIST ORDER BY NAME DESC;'
run_and_show(cursor, q)

print(" PS 8 update the table tourist by increasing the package_amt by 10% as surcharge")
q = 'UPDATE Tourist set Package_Amt = Package_Amt + 0.1*Package_Amt;'
cursor.execute(q)
#cnx.commit()
print(" Updated Table ")


