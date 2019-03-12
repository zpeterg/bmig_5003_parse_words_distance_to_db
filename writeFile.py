import csv

csv.register_dialect('forCSV', delimiter=',', quoting=csv.QUOTE_NONE, escapechar='\\', lineterminator='\n')

def writeFile(content, file_name):
    with open(file_name, 'w') as file:
        file.write(content)

def writeCSV(content, file_name, columns=[]):
    new_content = [columns]
    # if is a dictionary, convert to list
    if isinstance(content, dict):
        for item in content:
            new_content.append([item, content[item]])
    else:
        for c in content:
            if isinstance(c, list):
                new_content.append(c)
            else:
                new_content.append([c])
    # wrist CSV
    with open(file_name, 'w') as file:
        writer = csv.writer(file, dialect='forCSV')
        writer.writerows(new_content)