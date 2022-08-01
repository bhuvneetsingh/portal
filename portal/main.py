class rent:
    def houses():

        area = input("which area you want: \n1:Jagdish Colony \n2:DLF \n3:Model Town \n")
        if area == "1":
            data = ["Locality:Jagdish Colony", "area:Rohtak", "square_feet:500", "Type:2BHK", "Rent:Rs.6000/mon", "owner_id=1"]
            for i in data:
                print(i)
        elif area == "2":
            data = ["Locality:DLF", "area:Rohtak" "square_feet:1000", "Type:3BHK", "Rent:Rs.15000/mon", "owner_id=2"]
            for i in data:
                print(i)
        elif area == "3":
            data = ["Locality:Model town", "area:Rohtak" "square_feet:560", "Type:1BHK", "Rent:Rs.5500/mon", "owner_id=1"]
            for i in data:
                print(i)

class tenant:
    def available():
        options = input("1:view houses  \n2:request  \n3:log out \n")
        if options == "1":
            data_ = rent
            content = data_.houses()
        elif options == "2":
            print("which area do you prefer: ")
            data_ = rent
            content = data_.houses()
        elif options == "3":
            print("THANK YOU for your vist, you are logged out now")

class owner:
    def owner_req():
        options=input("1:Can create a request to post  \n2:remove their house for rental \n")
        if options == "1":
            data_ = rent
            content = data_.houses()
        elif options == "2":
            print("NO houses are available, all are booked, we will let you know if there is an availabilty")

class user_details:
    def details():
        data = input("chose users details: \n1:1st user \n2:2nd user \n3:3rd user  \n")
        if data == "1":
            datas = ["User Id:1", "Name:Lucifer", "Email:lucifer@gmail.com", "Mobile:9876543210", "Aadhaar:123412341234"]
            for i in datas:
                print(i)
        elif data == "2":
            datas = ["User Id:2", "Name:Peter Parker", "Email:perterparker@gmail.com", "Mobile:1234567890", "Aadhaar:567856785678"]
            for i in datas:
                print(i)
        elif data == "3":
            datas = ["User Id:3", "Name:Tony Stark", "Email:tonystark@gmail.com", "Mobile:1234509876", "Aadhaar:345634563456"]
            for i in datas:
                print(i)

class approver:
    def app():
        options=input("choose the options: \n1:Can view all the User details \n2:Decline the request \n")
        if options =="1":
            data_ = user_details
            content = data_.details()
        elif options == "2":
            print("your request is declined")

if __name__ == "__main__":
    print("WELCOME TO HOUSE RENTING PORTAL \nHow may i help you")
    user = input("1:Tenant \n2:Owner \n3:Approver \n")
    if user == "1":
        check = tenant
        object = check.available()
    elif user == "2":
        check = owner
        object = check.owner_req()
    elif user == "3":
        check = approver
        object = check.app()