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

    def __init__(self, bytestring=None, bitstring=None):
        if bytestring:
            self.bitstring = BitArray(bytestring).bin
        else:
            self.bitstring = bitstring

        self.version = self.get_version()
        self.ptype = self.get_type()
        print("Init packet, version=", self.version, " ptype=", self.ptype)
        self.sub_packets = []

        if self.ptype == 4:
            # Literal value packet
            """
            TODO refactor:
                - divide into groups of five
                - iterate over groups
                - add group to "bucket"
                - until and including group starting with 0
                - mark end of parsing and return it as that is another packet

                rest = self.get_literal_value()
                if rest:
                    return rest
            """

            self.literal_value = self.get_literal_value()
            print("  literal_value:", self.literal_value)
        else:
            # Operator packet
            ltype = self.bitstring[6]
            print("  ltype=", ltype)
            if int(ltype) == 0:
                # Length type: Bits
                sub_packets_length = int(self.bitstring[7:22], 2)
                sub_packet_bits = self.bitstring[22:22 + sub_packets_length]
                print("  sub_packets_length:", sub_packets_length)
                self.subpackets = self.get_sub_packets(sub_packet_bits)
            else:
                # Length type: Packets
                print("  sub_packet_no:")


    def get_version(self):
        version = self.bitstring[0:3]
        return int(version, 2)

    def get_type(self):
        ptype = self.bitstring[3:6]
        return int(ptype, 2)

    def get_literal_value(self):
        val_string = self.bitstring[6:]
        val_string = val_string[0:(len(val_string) % 5) * -1]  # Remove padding
        print("    val_string: ", val_string)

        # Remove leading last byte indicator bit from each group of five
        val_bytes = [
            val_string[i] for i in range(0, len(val_string)) if i % 5 > 0
        ]

        print("    val_bytes: ", val_bytes)

        return int("".join(val_bytes), 2)

    def get_sub_packets(self, bitstring):
        print("  Get sub packets from ", bitstring)
        subs = [Packet(bitstring=bitstring)]
        
        return []



# hexstring = "38006F45291200"  # 1, 6, ... subs
# hexstring = "EE00D40C823060"  # 7, 3
hexstring = "D2FE28"  # 6, 4, 2021

message = bytes.fromhex(hexstring)
packet = Packet(bytestring=message)

# print(packet.version)
# print(packet.ptype)
# if packet.literal_value:
#     print(packet.literal_value)
