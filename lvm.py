import os
import getpass
os.system("clear")
os.system("tput setaf 3")
os.system("tput setaf 7")
print("\t\t\t\t---------------------")

password = getpass.getpass('Enter password : ')
if password != "lvm":
    print('wrong password')
    exit()
ch='y'
while ch=='y':
    print("""\n
            Enter 1 to check Total Disk: 
            ENter 2 to Creation of PV 
            Enter 3 to display PV
            Enter 4 to Creation Of VG
            Enter 5 to display VG
            Enter 6 to Creation of LV
            Enter 7 to display LV
            Enter 8 to extend the size of LV
            Enter 9 to reduce the size of LV
            Enter 10 to remove the LV
            Enter 11 to remove the VG
            Enter 12 to remove the PV
            Enter 13 to exit
    """)
    choice = int(input('Enter choice : '))
    if  choice==1:
        os.system("fdisk -l")
    elif choice==2:
        HD=input("Enter the Hard Disk :  ")
        os.system("pvcreate  {}".format(HD))
    elif choice==3:
        HD=input("Enter the Hard Disk :  ")
        os.system("pvdisplay {}".format(HD))
    elif choice==4:
        name=input("Enter The name of Volume group :  ")
        HDs=input("Enter the Hard Disks by space between : ")
        os.system("vgcreate  {} {}".format(name,HDs))
    elif choice==5:
        name=input("Enter the name of volume group :")
        os.system("vgdisplay {}".format(name))
    elif choice==6:
        name=input("Enter the name of Logical Volume : ")
        VGname=input("Enter the name volume group : ")
        size=input("Enter the size ")
        os.system("lvcreate  --size {} --name {} {}".format(size,name,VGname))
        os.system("mkfs.ext4 /dev/{}/{}".format(VGname,name))
        FOLD=input("Enter the name folder to mount ")
        os.system("mkdir /{}".format(FOLD))
        os.system("mount /dev/{}/{} /{}".format(VGname,name,FOLD))
    elif choice==7:
        name=input("Enter the name of Logical volume :")
        VGname=input("Enter the name volume group : ")
        os.system("lvdisplay /dev/{}/{}".format(VGname,name))
    elif choice==8:
        name=input("Enter the name of LOgical volume ")
        VGname=input("Enter the volume group associated with Logical VOulme ")
        size=input("Enter the size to extend ")
        os.system("lvextend --size +{} /dev/{}/{} ".format(size,VGname,name))
        os.system("resize2fs /dev/{}/{} ".format(VGname,name))
    elif choice==9:
        name=input("Enter the name of LOgical volume ")
        VGname=input("Enter the volume group associated with Logical VOulme ")
        FOLD=input("Enter the name existing folder to mount ")
        os.system("umount /dev/{}/{} ".format(VGname,name))
        os.system("e2fsck -f /dev/mapper/{}-{} ".format(VGname ,name ))
        size=input("Enter the reduce size ")
        os.system("resize2fs /dev/{}/{} {} ".format(VGname,name,size))
        os.system("lvreduce --size {} /dev/{}/{}".format(size,VGname ,name ))
        os.system("mount /dev/{}/{} /{} ".format(VGname,name,FOLD))
    elif choice==10:
        name=input("Enter the name of LOgical volume ")
        VGname=input("Enter the volume group associated with Logical VOulme ")
        FOLD=input("Enter the name existing folder to mount ")
        os.system("umount /dev/{}/{} ".format(VGname,name))
        os.system("lvremove /dev/{}/{} ".format(VGname,name))
    elif choice==11:
        VGname=input("Enter the volume group associated with Logical VOulme ")
        os.system("vgremove {} ".format(VGname))
    elif choice==12:
        PV=input("Enter the name of PV  ")
        os.system("pvremove {} ".format(PV))
    elif choice==13:
        exit()
    ch=input("do you want to continue press  y otherwise n ")
    if ch=='y':
        os.system("clear")




    




