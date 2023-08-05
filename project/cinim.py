# import csv

# # Read the CSV data and create a dictionary to store region hierarchies
# region_data = {}
# with open('regions.csv', newline='', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         region_data[row[0]] = row[1:]

# def is_region_included(region, city):
#     return city.startswith(region)

# def is_subset(subset, superset):
#     for sub_item in subset:
#         if sub_item not in superset:
#             return False
#     return True

# def is_authorized(distributor_permissions, city):
#     for permission in distributor_permissions:
#         region_type = permission['type']
#         region_code = permission['code']
#         region_hierarchy = region_data.get(region_code)

#         if region_hierarchy is None:
#             continue

#         if region_type == 'INCLUDE':
#             if is_region_included(region_hierarchy[-1], city) and is_subset(region_hierarchy, city.split('-')):
#                 return True
#         elif region_type == 'EXCLUDE':
#             if is_region_included(region_hierarchy[-1], city) and is_subset(region_hierarchy, city.split('-')):
#                 return False

#     return True

# def write_permissions_to_csv(distributor_name, distributor_permissions):
#     with open(f'{distributor_name}_permissions.csv', 'w', newline='', encoding='utf-8') as csvfile:
#         fieldnames = ['type', 'code']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#         writer.writeheader()
#         for permission in distributor_permissions:
#             writer.writerow(permission)

# # Sample distributor permissions data
# distributor1_permissions = [
#     {'type': 'INCLUDE', 'code': 'IN'},  # INDIA
#     {'type': 'INCLUDE', 'code': 'US'},  # UNITED STATES
#     {'type': 'EXCLUDE', 'code': 'IN-TN'},  # TAMILNADU-INDIA
#     {'type': 'EXCLUDE', 'code': 'IN-KA'}  # KARNATAKA-INDIA
# ]

# distributor2_permissions = [
#     {'type': 'INCLUDE', 'code': 'IN'},  # INDIA
#     {'type': 'EXCLUDE', 'code': 'IN-TN'},  # TAMILNADU-INDIA
# ]

# distributor3_permissions = [
#     {'type': 'INCLUDE', 'code': 'IN-KA-HUBLI'}  # HUBLI-KARNATAKA-INDIA
# ]

# # Sample cities to check authorization
# cities_to_check = ['MUMBAI-INDIA', 'CHICAGO-ILLINOIS-UNITEDSTATES', 'CHENNAI-TAMILNADU-INDIA', 'BANGALORE-KARNATAKA-INDIA', 'HUBLI-KARNATAKA-INDIA']

# # Check permissions for distributor1
# for city in cities_to_check:
#     authorized = is_authorized(distributor1_permissions, city)
#     if authorized:
#         print(f"DISTRIBUTOR1 is authorized to distribute in {city}.")
#     else:
#         print(f"DISTRIBUTOR1 is not authorized to distribute in {city}.")

# # Check permissions for distributor2
# for city in cities_to_check:
#     authorized = is_authorized(distributor2_permissions, city)
#     if authorized:
#         print(f"DISTRIBUTOR2 is authorized to distribute in {city}.")
#     else:
#         print(f"DISTRIBUTOR2 is not authorized to distribute in {city}.")

# # Check permissions for distributor3
# for city in cities_to_check:
#     authorized = is_authorized(distributor3_permissions, city)
#     if authorized:
#         print(f"DISTRIBUTOR3 is authorized to distribute in {city}.")
#     else:
#         print(f"DISTRIBUTOR3 is not authorized to distribute in {city}.")

# # Write permissions to CSV files
# write_permissions_to_csv('DISTRIBUTOR1', distributor1_permissions)
# write_permissions_to_csv('DISTRIBUTOR2', distributor2_permissions)
# write_permissions_to_csv('DISTRIBUTOR3', distributor3_permissions)

import csv

# Read the CSV data and create a dictionary to store region hierarchies
region_data = {}
with open('regions.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        region_data[row[0]] = row[1:]

def is_region_included(region, city):
    return city.startswith(region)

def is_subset(subset, superset):
    for sub_item in subset:
        if sub_item not in superset:
            return False
    return True

def is_authorized(distributor_permissions, city):
    for permission in distributor_permissions:
        region_type = permission['type']
        region_code = permission['code']
        region_hierarchy = region_data.get(region_code)

        if region_hierarchy is None:
            continue

        if region_type == 'INCLUDE':
            if is_region_included(region_hierarchy[-1], city) and is_subset(region_hierarchy, city.split('-')):
                return True
        elif region_type == 'EXCLUDE':
            if is_region_included(region_hierarchy[-1], city) and is_subset(region_hierarchy, city.split('-')):
                return False

    return True

def write_permissions_to_csv(distributor_name, distributor_permissions):
    with open(f'{distributor_name}_permissions.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['type', 'code']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for permission in distributor_permissions:
            writer.writerow(permission)

# Sample distributor permissions data
distributor1_permissions = [
    {'type': 'INCLUDE', 'code': 'IN'},  # INDIA
    {'type': 'INCLUDE', 'code': 'US'},  # UNITED STATES
    {'type': 'EXCLUDE', 'code': 'IN-TN'},  # TAMILNADU-INDIA
    {'type': 'EXCLUDE', 'code': 'IN-KA'}  # KARNATAKA-INDIA
]

# Prompt the user to input the distributor name
input_distributor = input("Enter distributor name: ")

if input_distributor == 'distributor1':
    # Sample cities to check authorization for distributor1
    cities_to_check = ['MUMBAI-INDIA', 'CHICAGO-ILLINOIS-UNITEDSTATES', 'CHENNAI-TAMILNADU-INDIA', 'BANGALORE-KARNATAKA-INDIA', 'HUBLI-KARNATAKA-INDIA']

    # Check permissions for distributor1
    for city in cities_to_check:
        authorized = is_authorized(distributor1_permissions, city)
        if authorized:
            print(f"DISTRIBUTOR1 is authorized to distribute in {city}.")
        else:
            print(f"DISTRIBUTOR1 is not authorized to distribute in {city}.")
else:
    print(f"{input_distributor} is not recognized or authorized as a distributor.")




