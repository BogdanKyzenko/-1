def TOH ( disk , s, d, other):
    if disk == 1:
    print("Розмістити диск 1 3 " ,s,"to",d)
    TOH(disk-1, s, other, d)
    print( "Розмістити диск,",диск,"3",s,"to",d)
    TOH(disk-1. other, d, s)
    ip_ndisk = int(input("Введіть кшлькість дисків: "))
    TOH(ip_ndisk 'A', 'B', 'C')
