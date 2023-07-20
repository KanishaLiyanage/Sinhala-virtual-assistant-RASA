import mysql.connector

def get_balance(customer_name):
    # Replace with your database credentials
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": None,
        "database": "mobitel_customers",
    }

    try:
       # Connect to the database
       connection = mysql.connector.connect(**db_config)
       cursor = connection.cursor()

       # Execute the query to fetch the balance for the customer with the specified name
       query = "SELECT balance FROM customers WHERE name = %s;"
       cursor.execute(query, (customer_name,))

        # Fetch the balance from the result
       result = cursor.fetchone()
       if result:
        balance = result[0]
        return balance
       else:
        return None

    except mysql.connector.Error as err:
        # Handle any errors that occur during database connection or query execution
        print("An error occurred while fetching the balance from the database:", err)

    finally:
        # Close the database connection
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_package(customer_name):
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": None,
        "database": "mobitel_customers",
    }

    try:
       connection = mysql.connector.connect(**db_config)
       cursor = connection.cursor()

       query = "SELECT package FROM customers WHERE name = %s;"
       cursor.execute(query, (customer_name,))

       result = cursor.fetchone()
       if result:
        package = result[0]
        return package
       else:
        return None

    except mysql.connector.Error as err:
        print("An error occurred while fetching the balance from the database:", err)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_loyalty(customer_name):

    db_config = {
        "host": "localhost",
        "user": "root",
        "password": None,
        "database": "mobitel_customers",
    }

    try:

       connection = mysql.connector.connect(**db_config)
       cursor = connection.cursor()

       query = "SELECT loyalty_points FROM customers WHERE name = %s;"
       cursor.execute(query, (customer_name,))

       result = cursor.fetchone()
       if result:
        loyalty_points = result[0]
        return loyalty_points
       else:
        return None

    except mysql.connector.Error as err:
        print("An error occurred while fetching the balance from the database:", err)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_usage(customer_name):
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": None,
        "database": "mobitel_customers",
    }

    try:
       connection = mysql.connector.connect(**db_config)
       cursor = connection.cursor()

       query = "SELECT usage_report FROM customers WHERE name = %s;"
       cursor.execute(query, (customer_name,))

       result = cursor.fetchone()
       if result:
        usage_report = result[0]
        return usage_report
       else:
        return None

    except mysql.connector.Error as err:
        print("An error occurred while fetching the balance from the database:", err)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def get_payment_history(customer_name):
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": None,
        "database": "mobitel_customers",
    }

    try:
       connection = mysql.connector.connect(**db_config)
       cursor = connection.cursor()

       query = "SELECT payment_history FROM customers WHERE name = %s;"
       cursor.execute(query, (customer_name,))

       result = cursor.fetchone()
       if result:
        payment_history = result[0]
        return payment_history
       else:
        return None

    except mysql.connector.Error as err:
        print("An error occurred while fetching the balance from the database:", err)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()