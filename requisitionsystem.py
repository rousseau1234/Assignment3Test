class RequisitionSystem:
    #Starting requisition ID
    def __init__(self):
        self.requisitions = []
        self.requisition_id_counter = 10000  

    #Collecting staff information
    def staff_info(self):
        date = input("Enter date: ")
        staff_id = input("Enter Staff ID: ")
        staff_name = input("Enter Staff Name: ")
        return date, staff_id, staff_name

    #Taking item names and calculating the total
    def requisitions_details(self):
        total = 0.0
        while True:
            item_name = input("Enter item name (type 'done' to finish): ")
            if item_name.lower() == 'done':
                break
            else:
                cost = float(input("Enter cost: $"))
                total += cost

        return total

    #Deciding approval status based on the condition
    def requisition_approval(self, total):
        if total < 500:
            return "Approved"
        else:
            return "Pending"

    #Adding a new requisition and generating unique requisition ID
    def submit_requisition(self):
        date, staff_id, staff_name = self.staff_info()
        total = self.requisitions_details()
        status = self.requisition_approval(total)
        self.requisition_id_counter += 1
        req_id = self.requisition_id_counter

    #Generating approval status
        if status == "Approved":
            approval_ref = f"{staff_id}{str(req_id)[-3:]}"
        else:
            approval_ref = "Not available"

    #Creating requisition record    
        requisition = {
            "Date": date,
            "Requisition ID": req_id,
            "Staff ID": staff_id,
            "Staff Name": staff_name,
            "Total": total,
            "Status": status,
            "Approval Reference Number": approval_ref
        }
        self.requisitions.append(requisition)
        print(f"Requisition submitted successfully.\n")
        
    #Responding to pending requisition    
    def respond_requisition(self):
        pending_reqs = [req for req in self.requisitions if req["Status"] == "Pending"]
        if not pending_reqs:
            print("No pending requisitions.")
            return
        print("Pending Requisitions:")
        for req in pending_reqs:
            print(f"ID: {req['Requisition ID']}, Total: ${req['Total']:.2f}, Staff: {req['Staff Name']}")
        try:
            req_id = int(input("Enter Requisition ID to respond: "))
        except ValueError:
            print("Invalid ID. Please enter a number.")
            return
        for req in self.requisitions:
            if req["Requisition ID"] == req_id and req["Status"] == "Pending":
                response = input("Approve this requisition? (yes/no): ").lower()
                if response == 'yes':
                    req["Status"] = "Approved"
                    req["Approval Reference Number"] = f"{req['Staff ID']}{str(req_id)[-3:]}"
                elif response == 'no':
                    req["Status"] = "Not approved"
                else:
                    print("Invalid response. No changes made.")
                    return
                print("Requisition status updated.")
                return
        print("Requisition not found or not pending.")
        
    #Displaying all submitted requisitions
    def display_requisitions(self):
        if not self.requisitions:
            print("No requisitions to display.")
            return
        print("\nDisplaying all requisitions:")
        for req in self.requisitions:
            print(f"Date: {req['Date']}")
            print(f"Requisition ID: {req['Requisition ID']}")
            print(f"Staff ID: {req['Staff ID']}")
            print(f"Staff Name: {req['Staff Name']}")
            print(f"Total: ${req['Total']:.2f}")
            print(f"Status: {req['Status']}")
            print(f"Approval Reference Number: {req['Approval Reference Number']}\n")

    #Displaying requisition statistics
    def requisition_statistics(self):
        total_submitted = len(self.requisitions)
        approved = len([req for req in self.requisitions if req["Status"] == "Approved"])
        pending = len([req for req in self.requisitions if req["Status"] == "Pending"])
        not_approved = len([req for req in self.requisitions if req["Status"] == "Not approved"])
        print("\nRequisition Statistics:")
        print(f"Total submitted: {total_submitted}")
        print(f"Approved: {approved}")
        print(f"Pending: {pending}")
        print(f"Not approved: {not_approved}")

#Main Menu loop
def main():
    system = RequisitionSystem()
    while True:
        print("\nMenu:")
        print("1. Submit a Requisition")
        print("2. Respond to Pending Requisitions")
        print("3. Display All Requisitions")
        print("4. Show Statistics")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            system.submit_requisition()
        elif choice == '2':
            system.respond_requisition()
        elif choice == '3':
            system.display_requisitions()
        elif choice == '4':
            system.requisition_statistics()
        elif choice == '5':
            print("Exiting the Program!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

#Running the main fuction
main()
