import json
from employee import employee_name, age, title, details


def create_dict(name, age, title):
    newDict = {"first_name": str(name), "age": int(age), "title": str(title)}
    return newDict


def write_json_to_file(json_obj, output_file):
    newfile = open(output_file, 'w')
    newfile.write(json_obj)
    newfile.close()


def main():
    details()
    employee_dict = create_dict(employee_name, age, title)
    print("employee_dict: " + str(employee_dict))
    json_object = json.dumps(employee_dict)
    print("json_object: " + str(json_object))
    write_json_to_file(json_object, "employee.json")


if __name__ == "__main__":
    main()
