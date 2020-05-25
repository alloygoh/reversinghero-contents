from pwnlib.util.fiddling import rol, ror


counter = 0x40
start_string = 0xdeadfacedeadbeef
def in0(rdi_hex):
    global counter
    rdi_hex = rol(rdi_hex,counter,64)
    rdi_hex >>= 1
    rdi_hex <<= 1
    rdi_hex = ror(rdi_hex,counter,64)
    counter -= 1
    return rdi_hex

def in1(rdi_hex):
    global counter
    counter += 1
    rdi_hex = rol(rdi_hex,counter,64)
    rdi_hex >>= 1
    rdi_hex <<= 1
    rdi_hex = ror(rdi_hex,counter,64)
    return rdi_hex

def in2(rdi_hex):
    global counter
    counter += 1
    rdi_hex = rol(rdi_hex,counter,64)
    rdi_hex >>= 1
    rdi_hex <<= 1
    rdi_hex |= 1
    rdi_hex = ror(rdi_hex,counter,64)
    return rdi_hex

key = ''

while start_string != 0:
    if counter < 1:
        start_string = in1(start_string)
        key += '1'
    else:
        start_string = in0(start_string)
        key += '0'

print(key)

def run_simulation(count, hex_string):
    global counter
    counter_push = counter
    total = 0
    for i in range(count, count+20):
        counter = i
        new_hex = in2(hex_string)
        if new_hex & 0x123456701234567 == new_hex:
            print("FOUND")
            print(hex(new_hex))
            break
        total+=1
    # restore original counter
    #counter = counter_push
    return total, new_hex, counter
# run(counter,rdi_hex)
while True:
    num_one, start_string, _ = run_simulation(counter,start_string)
    print(counter)
    key += '1' * num_one
    key += '2'
    if start_string == 0x123456701234567:
        print(key)
        break
'''
key = '000000000000111111111111'
temp = start_string
for i in key:
    if i == '0':
        temp = in0(temp)
    elif i == '1':
        temp = in1(temp)
    else:
        temp = in2(temp)
    input(hex(temp))
'''
