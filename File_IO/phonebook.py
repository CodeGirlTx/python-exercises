#Phone App
phonebook_data = {

'Jessica':
    {
      'phone': '555-555-5555'
    },
'Seth':
    {
    'phone': '999-999-9999'
    }
}

choice = int(input("What do you want to do (1-5)?\n1. Look up an entry\n2. Set an entry\n3. Delete an entry\n4. List all entries\n5. Quit"))

if choice == 1:
    name = input("Name? ")
    print(name + "'s phone number is: " + phonebook_data[name]['phone'])

if choice == 2:
    entry_name = input("Entry: name? ")
    entry_phone = input("Entry: phone? ")
    phonebook_data.append({entry_name: entry_phone})

if choice == 3:
    del_person = input("Who do you want to delete? ")
    if 'del_person' in phonebook_data:
        del phonebook_data['del_person']
        print("Deleted entry for " + del_person)

if choice == 4:
    print(phonebook_data)

print("Done")
