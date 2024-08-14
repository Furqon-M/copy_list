# TEKNIK MENDUPLIKAT LIST

a = ["Angan","Kelana,","Petualang"]
print(f"a = {a}")

b = a
print(f"b = {b}")

# kita akan merubah member dari list a

# ini akan merubah kedua list
a[1] = "dira"
b.sort()

print(f"a = {a}")
print(f"b = {b}")

# addres dari list a dan b
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# MENDUPLIKAT LIST DENGAN COPY

print("membuat list c denga a.copy()")
c = a.copy() # full duplicate / membuat list data baru
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 0")
c[0] = "raka"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 1")
a[1] = "Chandra"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")