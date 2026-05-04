# Week 4: Sockets Lab

link to the repository: https://github.com/yinonY/week4

Here is the explanation of what I did, according to the assignment.
i am explaining all i have done step by step for each proof picture.

1: I ran the Python UDP server and client (`1_udp_s.py` and `1_udp_c.py`). The client sent "Hello" and the server returned it in uppercase.

2: I changed the UDP code so the client now sends "Testing new message!". The server adds an "ACK:" prefix (meaning Acknowledgment' thats what i got recommended to do) instead of making the text uppercase.

3: I compiled and ran the C++ UDP files (`2_udp_s.cpp` and `2_udp_c.cpp`) using WSL. The client sent "hello" and the server echoed it back.

4: I changed the C++ UDP code. The client sends "C++ UDP Test!" and the server sends a custom string "ACK from C++ Server" instead of echoing the buffer.

5: I ran the Python TCP server and client (`3_tcp_s.py` and `3_tcp_c.py`). I sent messages in a loop and the server returned them in uppercase.

6: I changed the Python TCP client code. I changed the loop exit word from "quit" to "exit" and updated the input text.

7: I changed the Python TCP server code. Instead of uppercase, the server adds "Server ACK:" before the message.

8: I compiled and ran the C++ TCP files (`4_tcp_s.cpp` and `4_tcp_c.cpp`). The client sent "Im a message" and the server echoed it. The output was messy because there was no newline in the print functions.

9: I changed the C++ TCP code. I added newlines (`endl`) to fix the prints. I changed the client message to "Hello from C++ TCP!" and the server now replies with "Message received by TCP server!".
