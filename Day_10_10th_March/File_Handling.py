'''
File Handling

File is a type of container in which we contain or store some data
By using extension name, we can identify what type of data is there inside of it.
Ex :- .py, .mp4, .html, ..mp3, .png, .jpg, .jpeg, etc.
Before Handling any file, taking the permission is very much important
open():
    open('filename.ext'/'absolute_path', mode)

close():
    var_name.close()

Here. total 3 different modes are present,
    1.write(w)
    2.read(r)
    3.append(a)


write mode:
    1.only write(w)
    2.write + read (wr)
    3.write binary (wb)
    4.write & read binary (wb+)

read mode:
    1.only read(w)
    2.read + write (rw)
    3.read binary (wb)
    4.read & write binary (rb+)

append mode:
    1.only append(a)
    2.append + read (a+)
    3.append binary (ab)
    4.append & read binary (ab+)

For write operation, 
    1. write(str_data): Single line of data.
    2. writelines([line1, line2, .... , linen]) Multiple line of data.

NOTE: 
1. In this, if the file is not present, it will create one then perform write operations.
2. If the file is already present, then it will override the prev data with the new one.
'''