#Provide a program to create tables(Employee,Department,Project)
#in sqllite and insert the data
'''There are 5 tables....1. Employee master-->employee
                         2. Department master-->department
                         3. Project master-->project
                         4. employee department relation --> emp_dept_transaction
                         5. emplloyee project relation --> emp_proj_transaction

    there is 1 to M relationship between employee and department...1 employee belongs to
    only 1 department... but department has more that 1 employees...

    M TO M relation between employee and project.... 1 employee can work on more than
    1 project, and 1 project has more than one employees'''

import sqlite3

def connect_database(dbname):
    #It connect to database, if database is not exists than it create new database
    conn = sqlite3.connect(dbname)
    return conn

def get_cursor(conn):
    # It return the cursor
    cursor = conn.cursor()
     
    return cursor
   

def create_table(cursor,sql_query):
    cursor.execute(sql_query)
    print("Table created")

def insert_table(cursor,sql_query):
    cursor.execute(sql_query)
    print("data inserted")

def main():
    
    conn = connect_database('Bizz.db')
    cursor = get_cursor(conn)

    sql_table_emp = '''CREATE TABLE IF NOT EXISTS employee(
                       EMP_CODE     VARCHAR(10) PRIMARY KEY
          	      ,EMP_NAME    VARCHAR(100)
	              ,DOB        DATE
          	      ,BLOOD_DROUP  VARCHAR(10)
	              ,ADDRESS    VARCHAR(100)
	              ,MOBILE_NO    VARCHAR(20)    
	             );'''
    sql_table_dept = '''CREATE TABLE IF NOT EXISTS department(
                       DEP_CODE     VARCHAR(10) PRIMARY KEY
          	      ,DEP_NAME    VARCHAR(100)
	              
	              );'''
    sql_table_proj = '''CREATE TABLE IF NOT EXISTS project(
                       PROJ_CODE     VARCHAR(10) PRIMARY KEY
          	      ,PROJ_NAME    VARCHAR(100)
	              
	              );'''
    sql_table_emptodept = '''CREATE TABLE IF NOT EXISTS emp_dept_transaction (
                             EMP_CODE     VARCHAR(10) 
          	            ,DEP_CODE    VARCHAR(10)
	                    ,FOREIGN KEY(EMP_CODE) REFERENCES employee(EMP_CODE)
	                    ,FOREIGN KEY(DEP_CODE) REFERENCES department(DEP_CODE)
	                   );'''
    sql_table_emptoproject = '''CREATE TABLE IF NOT EXISTS emp_proj_transaction(
                                EMP_CODE     VARCHAR(10) 
          	                ,PROJ_CODE    VARCHAR(10)
	                        ,FOREIGN KEY(EMP_CODE) REFERENCES employee(EMP_CODE)
	                        ,FOREIGN KEY(PROJ_CODE) REFERENCES project(PROJ_CODE)

	                     );'''
    sql_insert_emp1 = '''Insert into employee
                        (EMP_CODE, EMP_NAME, DOB, BLOOD_DROUP, ADDRESS, MOBILE_NO)
                        Values
                         ('AAA', 'A1A2A3', '01/01/1990 00:00:00', 'A+', 'A-101, OM Prakash App, Ahmedabad', '1234567899');'''
    sql_insert_emp2 =  '''Insert into employee
                        (EMP_CODE, EMP_NAME, DOB, BLOOD_DROUP, ADDRESS, MOBILE_NO)
                        Values
                         ('BBB', 'B1B2B3','01/01/1990 00:00:00', 'A+', 'A-101, OM Prakash App, Ahmedabad', '1234567899');'''
    sql_insert_emp3 =  '''Insert into employee
                        (EMP_CODE, EMP_NAME, DOB, BLOOD_DROUP, ADDRESS, MOBILE_NO)
                        Values
                         ('CCC', 'C1C2C3','01/01/1990 00:00:00', 'A+', 'A-101, OM Prakash App, Ahmedabad', '1234567899');
                         '''

    sql_insert_emp4 =  '''Insert into employee
                        (EMP_CODE, EMP_NAME, DOB, BLOOD_DROUP, ADDRESS, MOBILE_NO)
                        Values
                         ('DDD', 'D1D2D3','01/01/1990 00:00:00', 'A+', 'A-101, OM Prakash App, Ahmedabad', '1234567899');
                         '''

    sql_insert_dept1 = '''Insert into department
                        (DEP_CODE, DEP_NAME)
                        Values
                         ('PCS', 'PURCHASE');'''
    sql_insert_dept2 = '''Insert into department
                        (DEP_CODE, DEP_NAME)
                        Values
                         ('SALES', 'SALES AND MARKETING');'''
    sql_insert_dept3 = '''Insert into department
                        (DEP_CODE, DEP_NAME)
                        Values
                         ('MFG', 'MANUFACTURING');'''

    sql_insert_proj1 = '''Insert into project
                        (PROJ_CODE, PROJ_NAME)
                        Values
                         ('NIRMA', 'Nirma detergent powder');'''
    sql_insert_proj2 = '''Insert into project
                        (PROJ_CODE, PROJ_NAME)
                        Values
                         ('PEPSI', 'Pepsi co');'''
    sql_insert_proj3 = '''Insert into project
                        (PROJ_CODE, PROJ_NAME)
                        Values
                         ('CEMENT', 'Hathi cement');'''
    sql_insert_proj4 = '''Insert into project
                        (PROJ_CODE, PROJ_NAME)
                        Values
                         ('LAYS', 'Lays potatoes');'''
    
    sql_insert_emp_dept1 = '''Insert into emp_dept_transaction
                           (EMP_CODE, DEP_CODE)
                           Values
                           ('AAA', 'PCS');'''
    sql_insert_emp_dept2 = '''Insert into emp_dept_transaction
                           (EMP_CODE, DEP_CODE)
                           Values
                           ('BBB', 'SALES');'''
    sql_insert_emp_dept3 = '''Insert into emp_dept_transaction
                           (EMP_CODE, DEP_CODE)
                           Values
                           ('CCC', 'MFG');'''
    sql_insert_emp_dept4 = '''Insert into emp_dept_transaction
                           (EMP_CODE, DEP_CODE)
                           Values
                           ('DDD', 'MFG');'''

    sql_insert_emp_proj1 = '''Insert into emp_proj_transaction
                           (EMP_CODE, PROJ_CODE)
                           Values
                           ('CCC', 'PEPSI');'''
    sql_insert_emp_proj2 = '''Insert into emp_proj_transaction
                           (EMP_CODE, PROJ_CODE)
                           Values
                           ('CCC', 'CEMENT');'''
    sql_insert_emp_proj3 = '''Insert into emp_proj_transaction
                           (EMP_CODE, PROJ_CODE)
                           Values
                           ('AAA', 'PEPSI');'''
    sql_insert_emp_proj4 = '''Insert into emp_proj_transaction
                           (EMP_CODE, PROJ_CODE)
                           Values
                           ('BBB', 'LAYS');'''
    sql_insert_emp_proj5 = '''Insert into emp_proj_transaction
                           (EMP_CODE, PROJ_CODE)
                           Values
                           ('DDD', 'PEPSI');'''
    sql_insert_emp_proj6 = '''Insert into emp_proj_transaction
                           (EMP_CODE, PROJ_CODE)
                           Values
                           ('BBB', 'NIRMA');'''
    sql_insert_emp_proj7 = '''Insert into emp_proj_transaction
                           (EMP_CODE, PROJ_CODE)
                           Values
                           ('AAA', 'NIRMA');'''
    
    cursor.execute("DROP TABLE IF EXISTS employee")
    cursor.execute("DROP TABLE IF EXISTS department")
    cursor.execute("DROP TABLE IF EXISTS project")
    cursor.execute("DROP TABLE IF EXISTS emp_dept_transaction")
    cursor.execute("DROP TABLE IF EXISTS emp_proj_transaction")

   

    
        
    create_table(cursor,sql_table_emp)
    create_table(cursor,sql_table_dept)
    create_table(cursor,sql_table_proj)
    create_table(cursor,sql_table_emptodept)
    create_table(cursor,sql_table_emptoproject)
    
    insert_table(cursor,sql_insert_emp1)
    insert_table(cursor,sql_insert_emp2)
    insert_table(cursor,sql_insert_emp3)
    insert_table(cursor,sql_insert_dept1)
    insert_table(cursor,sql_insert_dept2)
    insert_table(cursor,sql_insert_dept3)
    insert_table(cursor,sql_insert_proj1)
    insert_table(cursor,sql_insert_proj2)
    insert_table(cursor,sql_insert_proj3)
    insert_table(cursor,sql_insert_proj4)
    insert_table(cursor,sql_insert_emp4)
    insert_table(cursor,sql_insert_emp_proj1)
    insert_table(cursor,sql_insert_emp_proj2)
    insert_table(cursor,sql_insert_emp_proj3)
    insert_table(cursor,sql_insert_emp_proj4)
    insert_table(cursor,sql_insert_emp_proj5)
    insert_table(cursor,sql_insert_emp_proj6)
    insert_table(cursor,sql_insert_emp_proj7)
    insert_table(cursor,sql_insert_emp_dept1)
    insert_table(cursor,sql_insert_emp_dept2)
    insert_table(cursor,sql_insert_emp_dept3)
    insert_table(cursor,sql_insert_emp_dept4)
    
    
    


if __name__ =='__main__':
    main()
