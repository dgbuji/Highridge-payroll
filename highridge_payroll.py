import random
# Creating a dynamic list of workers and storing the data in form of a dictionary
workers = []
genders = ["Male", "Female"]

try: 
    for i in range (1,401):
        worker = {
            "ID": i,
            "Name": f"Worker_{i}",
            "Gender": random.choice(genders),
            "Salary": random.randint(5000, 35000), #Salary range is between 5000 and 35000
        }
        workers.append(worker)
except Exception as e:
    print("Error generating worker list:", e)

# Generate payment slips and assign employee level

for worker in workers:

    try: 
        employee_level = "Regular" # Default level for those without a specific level
    # Condition 1 for salary between $10,000 and $20,000 = A1
        if 10000 < worker["Salary"] < 20000:
            employee_level = "A1"
    # Condition 2 for salary between $7,500 and #30,000 + Female employee = A5-F
        elif 7500 < worker["Salary"] < 30000 and worker ["Gender"] ==  "Female":
            employee_level = "A5-F"
# Generate payment slip
        print (f"Payment Slip for {worker['Name']} (ID: {worker['ID']})")
        print (f"Gender: {worker['Gender']}")
        print (f"Salary: ${worker['Salary']}")
        print (f"Employee Level: {employee_level}")
        print ("-" * 30)
    
    except KeyError as e:
        print("Error generating payment slip for worker ID", worker["ID"], ":", e)
    except Exception as e:
        print("Unexpected Error generating payment slip for worker ID", worker["ID"], ":", e)
    except Exception as e:  
        print("Error generating payment slip in payment system:", e)
    
    

                