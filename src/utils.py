def readDbFile(filename, models):
    # Open the .sql file
    sqlFile = open(filename,'r')

    # Create an empty command string
    sqlCommand = ''

    # Iterate over all lines in the sql file
    for line in sqlFile:
        # Ignore commented lines
        if not line.startswith('--') and line.strip('\n'):
            # Append line to the command string
            sqlCommand += line.strip('\n')

            # If the command string ends with ';', it is a full statement
            if sqlCommand.endswith(';'):
                # Try to execute statement and commit it
                try:
                    print(sqlCommand)
                    models.executeRawSql(sqlCommand)

                # Assert in case of error
                except:
                    print('No insertion made. Check if there are primary key conflicts: ' + sqlCommand)

                # Finally, clear command string
                finally:
                    sqlCommand = ''