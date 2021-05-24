import struct

B_SIZE = 9
C_SIZE = 4
F_SIZE = 8
E_SIZE = 12
D_SIZE = 4 + 4 + 2 + 4 + 4
A_SIZE = 4 + 2 * 5 + 4 + 4 + 2 + 1 + 1


def parse_b(offset, byte_string):
    b_bytes = byte_string[offset:offset + B_SIZE]
    b_parsed = struct.unpack('>Bq', b_bytes)
    return {'B1': b_parsed[0], 'B2': b_parsed[1]}


def parse_c(offset, byte_string):
    c_bytes = byte_string[offset:offset + C_SIZE]
    c_parsed = struct.unpack('>hh', c_bytes)
    return {'C1': c_parsed[0], 'C2': c_parsed[1]}


def parse_f(offset, byte_string):
    f_bytes = byte_string[offset:offset + F_SIZE]
    f_parsed = struct.unpack('>iHh', f_bytes)
    return {'F1': f_parsed[0],
            'F2': f_parsed[1],
            'F3': f_parsed[2]}


def parse_e(offset, byte_string):
    e_bytes = byte_string[offset:offset + E_SIZE]
    e_parsed = struct.unpack('>III', e_bytes)
    e1_bytes = byte_string[e_parsed[1]:e_parsed[1] + e_parsed[0] * 4]
    e1_parsed = struct.unpack('>' + 'i' * e_parsed[0], e1_bytes)
    return {
        'E1': list(e1_parsed),
        'E2': e_parsed[2]
    }


def parse_d(offset, byte_string):
    d_bytes = byte_string[offset:offset + D_SIZE]
    d_parsed = struct.unpack('>ccccIHII', d_bytes)
    d3_bytes = byte_string[d_parsed[6]:d_parsed[6] + d_parsed[5]]
    d3_parsed = struct.unpack('>' + 'b' * d_parsed[5], d3_bytes)
    return {
        'D1': (b''.join(d_parsed[0:4])).decode('utf-8'),
        'D2': parse_e(d_parsed[4], byte_string),
        'D3': list(d3_parsed),
        'D4': parse_f(d_parsed[7], byte_string)
    }


def parse_a(offset, byte_string):
    a_bytes = byte_string[offset:offset + A_SIZE]
    a_parsed = struct.unpack('>iHHHHHfIHbb', a_bytes)
    print(a_parsed)

    return {
        'A1': a_parsed[0],
        'A2': [parse_b(a_parsed[1], byte_string),
               parse_b(a_parsed[2], byte_string),
               parse_b(a_parsed[3], byte_string),
               parse_b(a_parsed[4], byte_string),
               parse_b(a_parsed[5], byte_string)],
        'A3': a_parsed[6],
        'A4': parse_c(a_parsed[7], byte_string),
        'A5': parse_d(a_parsed[8], byte_string),
        'A6': a_parsed[9],
        'A7': a_parsed[10]
    }


def f31(byte_string):
    return parse_a(5, byte_string)


print(f31(b'\x8fPXRG<\x04\x06X\x00\x1f\x00(\x001\x00:\x00C?\x0f\xa8\xa0\x00\x00\x00L\x00'
          b'r\x93\xebh\x13\xca\\\xcf\xcf\x03 (\x93\xb1\x93Qs\xdc\x93\xdb[\x11MJ'
          b'\x01UZ\xfc\xe5D\xa2\x14\x0b\x94\xd4{\x8d\x92\xf5\xc4\t\xa0\x18{\xec<\xc8\x8b'
          b'\xe0wSI\xaeG^\x08\x9f\nhs\xfbH\x8c\xd7\x00\x00\x00\x03\x00\x00\x00P'
          b'\x1b\x12\\\xa4\x11\xc0\x1e\xf2\x91q\x07\x08\xd7\xb4oqlv\x00\x00'
          b'\x00\\\x00\x02\x00\x00\x00h\x00\x00\x00j'))

# print(f31
# (b'\x8fPXRGK\x04Z#\x00\x1f\x00(\x001\x00:\x00C>\x98\xda\xc5\x00\x00\x00L\x00'
# b'o\xa6e\t^\xc2\xf0+\xc9\x03\xba\x08"7\x81\x8f\xcaB\x1f8b\xdf\x14\xff'
# b'\x1f\xf4\x9d\xd3?.\xf1\x04z\x9d\xb7A\xf7\xfdHQ>\xc5k\xdd\x86\xdf\xbb\xd6'
# b'\xfb\xaa\xdf4\x8a"\xae\xbea\xed\x87\xa6\x00\x00\x00\x02\x00\x00\x00P'
# b'\xb1\x8b{7\xe5\x93\x1f\xfca\xed\xab!\x97\x85Yyzrb\x00\x00\x00X\x00'
# b'\x03\x00\x00\x00d\x00\x00\x00g')
# )
