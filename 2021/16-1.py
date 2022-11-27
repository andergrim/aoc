from bitstring import BitArray


with open('16.txt') as fp:
    hexstring = fp.read()
    hexstring = hexstring.strip()


class Packet:
    bitstring = ""
    version = 0
    ptype = 0
    literal_value = None

    sub_packets = []

    def __init__(self, bytestring):
        self.bitstring = BitArray(bytestring).bin
        self.version = self.get_version()
        self.ptype = self.get_type()

        if self.ptype == 4:
            self.literal_value = self.get_literal_value()
        else:
            if self.bitstring[6]:
                sub_packets_length = int(self.bitstring[7:22], 2)
                sub_packet_bits = self.bitstring[22:22 + sub_packets_length]
            else:
                pass



    def get_version(self):
        version = self.bitstring[0:3]
        return int(version, 2)

    def get_type(self):
        ptype = self.bitstring[3:6]
        return int(ptype, 2)

    def get_literal_value(self):
        val_string = self.bitstring[6:]
        val_string = val_string[0:(len(val_string) % 5) * -1]  # Remove padding

        # Remove leading last byte indicator bit from each group of five
        val_bytes = [
            val_string[i] for i in range(0, len(val_string)) if i % 5 > 0
        ]

        return int("".join(val_bytes), 2)

    def get_sub_packets(self):
        return []



hexstring = "38006F45291200"  # 1, 6, ... subs
# hexstring = "EE00D40C823060"  # 7, 3
# hexstring = "D2FE28"  # 6, 4, 2021

message = bytes.fromhex(hexstring)
packet = Packet(message)

print(packet.version)
print(packet.ptype)
if packet.literal_value:
    print(packet.literal_value)
