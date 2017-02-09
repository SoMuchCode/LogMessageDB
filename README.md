# LogMessageDB
Python 3.6 class for time-stamped logging to a sqlite3 DB.

To initialize LogMessageDB:
 message = LogMessage('log.db')

To read the log:
 message.read()

To write to the log:
 message.write('whatever you want to log.')
