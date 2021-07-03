import requests


def fetch_rest_api():
    print("rest api call")
    response = requests.get("https://reqres.in/api/users?page=1")
    user_data = response.json()

    print(user_data)

    total = user_data["total"]
    print(total)

    data = user_data['data']
    for record in data:
        print(record["id"], record["email"], record["first_name"], record["last_name"])


if __name__ == '__main__':
    fetch_rest_api()
    try:
        f1 = open("student2.txt", "r")

    except:
        print("fie not Found")
    else:
        print(f1.read(10))
        print(f1.readline())
        f1.close()

    finally:
        print("Always going to execute")

        # Read data from user console
        First_name = input("enter your name")
        print(First_name)
        last_name = input("Enter your last name:")
        print(last_name)
        city = input("Enter your city name:")
        print(city)

        # write dta to file
        f1 = open("student2.txt", "w")
        f1.write("First_name    last_name     city  \n")
        f1.close()

        # appned data

        f1 = open("student2.txt", "a")
        f1.write(First_name + ",    " + last_name + ",    " + city)
        f1.close()

    f1 = open("student2.txt", "r")
    for row in f1:
        print(row)
        print(row.split(","))

    f1.close()
