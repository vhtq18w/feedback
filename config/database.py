class DatabaseConfig:
    USERNAME = 'burgess'
    PASSWORD = 'burgess'
    HOSTADDR = 'localhost'
    DBPORT = '3306'
    DBNAME = 'feedback'

    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(
        USERNAME, PASSWORD, HOSTADDR, DBPORT, DBNAME
    )
