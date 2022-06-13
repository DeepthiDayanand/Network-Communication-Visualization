# Author: Mouad Lasri - 67887


# importing the packages we need from "pcapfile"
from pcapfile import savefile
from pcapfile.protocols.linklayer import ethernet
from pcapfile.protocols.network import ip

# import the module I will need from scapy package
from scapy.all import rdpcap

# import the modules I will need from py2neo package
from py2neo import Graph, Node, Relationship

# read pcap file in binary format
pcapfile = open('pcapfile.dump', 'rb')
# load the pcapfile into a variable
capfile = savefile.load_savefile(pcapfile, layers=2, verbose=True)

# To get an overall view of the dump file, we read it with scapy
packets = rdpcap("pcapfile.dump")
print(packets)

# An overall summary that is not very detailed of data in PCAP file, it does not tell us if the TCP packet is IPv4 or IPv6
print(packets.summary())

# A more detailed view of the pcap file
# It tells us whether the packet an IPv4 address type of IPv6
for number, packet in enumerate(packets.sessions()):
    print(capfile.packets[number].packet.payload)


# A more detailed summary of the packets
packets.sessions()


# Create a graph with password = 123
# not mentioning the URL will automatically connect to the localhost Neo4j database
neo4jGraph = Graph(password="123")


for number, packet in enumerate(packets.sessions()):
    # split the Packet object to extract the information we need from it
    pkt = packet.split()

    # check the first element of the list to see what type it is
    if "TCP" in pkt[0]:
        firstNode = Node("Host", name=pkt[1].split(":")[0])
        secondNode = Node("Host", name=pkt[3].split(":")[0])
        # check if it's IPv4 or IPv6
        # convert the IP object into a string, splitting it and reading the first element of the array
        if(str(capfile.packets[0].packet.payload).split()[0] == 'ipv4'):
            # create a relationshipt of type TCP - IPv4
            SENDtcp = Relationship.type("TCP - IPv4")
        else:
            # create a relationshipt of type TCP - IPv6
            SENDtcp = Relationship.type("TCP - IPv6")

        # connect the relationship between the two nodes created above (loading into the database)
        neo4jGraph.merge(SENDtcp(firstNode, secondNode), "Host", "name")

    # check the first element of the list to see what type it is
    elif "UDP" in pkt[0]:
        # the second element in the packet object list is the sender address
        firstNode = Node("Host", name=pkt[1].split(":")[0])

        # the fourth element in the packet object list is the sender address
        secondNode = Node("Host", name=pkt[3].split(":")[0])

        # convert the UDP packet object into a string, splitting it and reading the first element of the array
        SENDudp = Relationship.type("UDP")

        # connect the relationship between the two nodes created above (loading into the database)
        neo4jGraph.merge(SENDudp(firstNode, secondNode), "Host", "name")

    # check the first element of the list to see what type it is
    elif "ICMP" in pkt[0]:
        # the second element in the packet object list is the sender address
        firstNode = Node("Host", name=pkt[1].split(":")[0])
        # the fourth element in the packet object list is the sender address

        secondNode = Node("Host", name=pkt[3].split(":")[0])

        # convert the ICMP packet object into a string, splitting it and reading the first element of the array
        SENDicmp = Relationship.type("ICMP")

        # connect the relationship between the two nodes created above (loading into the database)
        neo4jGraph.merge(SENDicmp(firstNode, secondNode), "Host", "name")

    # check the first element of the list to see what type it is
    elif "ARP" in pkt[0]:
        # the second element in the packet object list is the sender address
        firstNode = Node("Host", name=pkt[1].split(":")[0])

        # the fourth element in the packet object list is the sender address
        secondNode = Node("Host", name=pkt[3].split(":")[0])

        # convert the ARP packet object into a string, splitting it and reading the first element of the array
        SENDarp = Relationship.type("ARP")

        # connect the relationship between the two nodes created above (loading into the database)
        neo4jGraph.merge(SENDarp(firstNode, secondNode), "Host", "name")
