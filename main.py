print("\n ##### Paging Calculator ##### \n")

# Request input
kb = input(" Enter kb [i.e., 4, 8]: ")
virtual_address = input(" Enter virtual address [i.e., 20000]: ")

# Operating functions
page_kd = (int(kb) * 1024)
virtual_page_number = (int(virtual_address) / page_kd)
offset = (int(virtual_address) % page_kd)

# Display operations
print("\n ##### Operations ##### \n")
print(" Note: 1kb = 1024\n")
print(" You entered: "+kb+"kb and virtual address - "+virtual_address)
print(" "+virtual_address+"/"+kb+"k")
print(" "+virtual_address+"/"+str(page_kd)+" = "+str(int(virtual_page_number))+" rem "+str(offset))

# Display result
print("\n ##### Answer ##### \n")
print(" Virtual Page Number = " + str(int(virtual_page_number)))
print(" Offset = " + str(offset))


print("\n\n Thanks for using! \n\n Made by Fedorae Education a Fedorae company. \n\n For more visit https://github.com/edu-fedorae")
