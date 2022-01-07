key_location="chair"
locations=["garage","living","chair","closet"]
for i in locations:
    if i==key_location:
        print("key is found",i)
        break
    else:
        print("key is not found",i)