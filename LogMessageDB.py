#!/usr/bin/env python
#
# LogMessageDB class
#  For writing a timestamped log to a sqlite3 database.
#  version 0.1
# 
# Python 3.6
# CLM 20170208
#
# To initialize LogMessageDB
# message = LogMessage('log.db')
#
# To read the log
# message.read()
#
# To write to the log
# message.write('Whatever you want to log.')
#

try:
    import sqlite3, os.path, datetime
except Exception as errorCaught:
    print('Error: Cannot load module')
    print('Error:', errorCaught)

def timeStamped(fmt='%Y%m%d-%H:%M:%S'):
    return datetime.datetime.now().strftime(fmt)

class LogMessageDB:
    def __init__(self, dbName):
        self.dbn = dbName
        if os.path.isfile(self.dbn):    # DB Exists
            try:
                self.db = sqlite3.connect(self.dbn)
            except:
                print('Error: Problem connecting to database', self.dbn)
        else:                           # No DB file, create one
            try:
                self.db = sqlite3.connect(self.dbn)
                self.db.execute('create table errlog (tstamp text, errmsg text)')
                self.db.execute('insert into errlog (tstamp, errmsg) values ("Timestamp:" , "Error Message:")')
                self.db.commit() #this saves it
                self.db.close()
            except:
                print('Error: Problem creating database', self.dbn)
    def read(self):
        self.db = sqlite3.connect(self.dbn)
        self.table = self.db.execute('select * from errlog')
        for self.each in self.table:
            print(self.each)
        self.db.close()
    def write(self, texT):
        try:
            self.db = sqlite3.connect(self.dbn)
            self.appendMe = timeStamped() , texT
            self.db.execute("insert into errlog values (?,?)", (self.appendMe))
            self.db.commit()
            self.db.close()
        except lite.Error as errorCaught:
            print('Error:', errorCaught)
            if self.db:
                self.db.rollback()
                 self.db.close()
        except Exception as errorCaught:
            print('Error:', errorCaught)
            if self.db:
                self.db.rollback()
                 self.db.close()

# Initialize LogMessageDB class
message = LogMessageDB('logs.db')


## Example code to show how it works
import time
logMessage = 'This is the message we want to log.'
message.write(logMessage)
print('....')
time.sleep(1)
message.write(logMessage)
print('....')
time.sleep(2)
message.write(logMessage)

# Read the log
message.read()
