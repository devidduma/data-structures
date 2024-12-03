import random

class Message:
    def __init__(self, message):
        self.message = message
        self.packets = []
    
    # create n packets with same length if possible, if not then difference of length between packets at most 1
    def prepare_n_packets(self, n):
        packets = []
        packet_length = len(self.message) / n
        for i in range(n):
            start = int(round(packet_length*i))
            end = int(round(packet_length*(i+1)))
            packets.append(self.message[start:end])
        self.packets = packets


class User:
    def emulate_send_message(self, message, n):
        message.prepare_n_packets(n)
        unshuffled_packets = message.packets
        shuffled_packets = []
        s = list(range(n))
        random.shuffle(s)
        for i in s:
            shuffled_packets.append([i, unshuffled_packets[i]])
        print("Packets ready to be sent: ", shuffled_packets)
        return shuffled_packets
    
    def emulate_get_message(self, packets):
        print("Packets received: ", packets)
        sorted_packets = []

        # insertion sort the packages. O(n^2)
        for new_packet in packets:
            sorted_packets.append(new_packet)

            # iterate from the end
            for idx in range(len(sorted_packets)-2,-1, -1):
                if sorted_packets[idx+1][0] < sorted_packets[idx][0]:
                    #swap elements
                    sorted_packets[idx+1], sorted_packets[idx] = sorted_packets[idx], sorted_packets[idx+1]
                else:
                    break
            
        print("Packets sorted: ", sorted_packets)

ben = User()
shuffled_packets = ben.emulate_send_message(Message("Hello World! Hello World!"), 16)
alice = User()
alice.emulate_get_message(shuffled_packets)