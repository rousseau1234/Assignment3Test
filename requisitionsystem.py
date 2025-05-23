"""
Software Development Fundamentals Assessment Task 1
Author: Rousseau Bhattacharjee
"""

# Start requisition counter
requisition_counter = 10000

def staff_info():
    global requisition_counter
    requisition_counter += 1

    # Collect staff information
    date = input("Date: ")
    staff_id = input("Staff ID: ")
    staff_name = input("Staff Name: ")

    # Store staff data
    staff_data = {
        "Date": date,
        "Staff ID": staff_id,
        "Staff Name": staff_name,
        "Requisition ID": requisition_counter
    }

    # Display information
    print("\nPrinting Staff Information: ")
    print("Date: " + date)
    print("Staff ID: " + staff_id)
    print("Staff Name: " + staff_name)
    print("Requisition ID: " + str(requisition_counter))

    return staff_data

def requisitions_total():
    
    staff_data = staff_info()

    print("\nPlease enter your requisition items (type 'done' when finished):")
    total = 0 
    while True:
        print("Please enter in format: Item $Price")
        item_input = input()

        if item_input.lower() == 'done':
            break

        try:
   # Add price from the input
            price = float(item_input.split('$')[-1])
            total += price
        except:
            print("Invalid Format") 

    # Combine staff and total requisition data
    requisition_data = {
        "Date": staff_data["Date"],
        "Requisition ID": staff_data["Requisition ID"],
        "Staff ID": staff_data["Staff ID"],
        "Staff Name": staff_data["Staff Name"],
        "Total": total
    }

    print("$" + str(total))  # Print the total cost

    return requisition_data

def requisition_approval():
    requisition_data = requisitions_total()
    status = "Pending"
    approval_ref = "Not assigned"

    # Approve if total is more than $500 and generate approval reference
    if requisition_data["Total"] > 500:
        status = "Approved"
        approval_ref = requisition_data['Staff ID'] + str(requisition_data['Requisition ID'])[-3:]

    # Store approval details
    approval_data = {
        "Date": requisition_data["Date"],
        "Requisition ID": requisition_data["Requisition ID"],
        "Staff ID": requisition_data["Staff ID"],
        "Staff Name": requisition_data["Staff Name"],
        "Total": requisition_data["Total"],
        "Status": status,
        "Approval Reference": approval_ref,
    }

    # Display approval information
    print("Total: $" + str(requisition_data["Total"]))
    print("Status: " + status)
    if status == "Approved":
        print("Approval Reference Number: " + approval_ref)

    return approval_data

def display_requisitions():
    approval_data = requisition_approval()

    # Print final requisition summary
    print("\nPrinting Requisitions:")
    print("Date: " + approval_data["Date"])
    print("Requisition ID: " + str(approval_data["Requisition ID"]))
    print("Staff ID: " + approval_data["Staff ID"])
    print("Staff Name: " + approval_data["Staff Name"])
    print("Total: " + str(approval_data["Total"]))
    print("Status: " + approval_data["Status"])

    if approval_data["Status"] == "Approved":
        print("Approval Reference Number: " + approval_data["Approval Reference"])

# Loop taking inputs until the user decides to finish
while True:
    display_requisitions()
    t = input("Do you want to finish? Type 'Yes' or 'No': ")
    if t.lower() == 'yes':
        break
