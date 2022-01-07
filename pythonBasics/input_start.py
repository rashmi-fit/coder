indian=["samosa","puri","dal","naan"]
chinese=["egg  role","pot sticker","friedrice"]
italian=["pizza","pasta","risotto"]

dish=input("enter a dish name")
if dish in indian:
    print("indian")
elif dish in italian:
    print("italian")
elif dish in chinese:
    print("chinese")
else:
    print("based on my knowledge i dont know what is this cuisine", dish)