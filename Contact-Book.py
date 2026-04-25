contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("✅ Contact Added Successfully!")


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\n📒 Contact List:")
    for c in contacts:
        print(f"Name: {c['name']}, Phone: {c['phone']}")


def search_contact():
    key = input("Enter name or phone to search: ")

    for c in contacts:
        if key in c["name"] or key in c["phone"]:
            print("🔍 Contact Found:")
            print(c)
            return

    print("❌ Contact not found.")


def update_contact():
    name = input("Enter name to update: ")

    for c in contacts:
        if c["name"] == name:
            c["phone"] = input("New Phone: ")
            c["email"] = input("New Email: ")
            c["address"] = input("New Address: ")
            print("✅ Contact Updated!")
            return

    print("❌ Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ")

    for c in contacts:
        if c["name"] == name:
            contacts.remove(c)
            print("🗑️ Contact Deleted!")
            return

    print("❌ Contact not found.")


# Main Menu
while True:
    print("\n===== 📒 Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("👋 Exiting...")
        break
    else:
        print("❌ Invalid choice!")