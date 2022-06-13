# datapipeline-TCP-UDP-neo4j
This project is about building a data pipeline to move network traces from a dataset to a Neo4J data store using Python. Each trace over TCP and UDP as well as their subtraces (ARP and ICMP) need to be modelized and stored in Neo4J. The purpose is to visualize each sender and receiver as Nodes, as well as the type of the protocol used as a relationship.

Libraries used: 
- Pypcapfile: Python library for handling, reading and parsing packets from a pcap file.
- Scapy: A Python program that enables the user to send, read, dissect and forge network packets.
“scapy” will be used alongside “pypcapfile” for more flexibility and better results.
- Py2neo: A client library for working with Neo4Jj from within Python applications and within
the command line. I will use this library’s API to interact with my Neo4j database (hosted locally)
without having to write Cypher SQL manually. Instead, I will only use Python code for all Cypher
SQL operations
