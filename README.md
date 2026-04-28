# Communication Server — Python Socket Programming

A structured, hands-on exploration of low-level network communication using the Python socket module.
This repository focuses on building TCP and UDP communication systems from first principles, with an emphasis on clarity, correctness, and practical understanding.

---

## Overview

This project is designed to develop a deep understanding of how networked systems communicate at a fundamental level. Instead of relying on high-level abstractions, it works directly with sockets to demonstrate how data is transmitted, received, and managed across connections.

The implementation progresses from basic single-client setups to more extensible communication patterns, making it suitable for both learning and experimentation.

---

## Objectives

* Understand how socket-based communication works internally
* Implement TCP and UDP servers and clients from scratch
* Explore connection-oriented vs connectionless protocols
* Learn IP binding, ports, and network interfaces
* Build a foundation for real-world backend and distributed systems

---

## Features

* TCP server and client implementation
* UDP server and client implementation
* Bi-directional message exchange
* Basic multi-client handling concepts
* Network debugging and testing workflows
* Clear separation of protocol-specific logic

---

## Project Structure

```bash
communication-server/
│
├── tcp/
│   ├── tcp_server.py
│   └── tcp_client.py
│
├── udp/
│   ├── udp_server.py
│   └── udp_client.py
│
└── README.md
```

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/shashaaankkkkk/Socket_learning.git
cd communication-server
```

### Run TCP server

```bash
python tcp/tcp_server.py
```

### Run TCP client

```bash
python tcp/tcp_client.py
```

### Run UDP server

```bash
python udp/udp_server.py
```

### Run UDP client

```bash
python udp/udp_client.py
```

---

## Core Concepts

### Socket Creation

```python
socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # UDP
```

### Binding to Interface

```python
server.bind(("0.0.0.0", 12345))
```

### TCP Connection Handling

```python
server.listen()
connection, address = server.accept()
```

### Data Transmission

```python
connection.send(data)
connection.recv(1024)
```

### UDP Communication

```python
server.recvfrom(1024)
server.sendto(data, address)
```

---

## Networking Notes

* `0.0.0.0` binds the server to all available network interfaces
* `127.0.0.1` restricts communication to the local machine
* TCP ensures reliable, ordered delivery
* UDP prioritizes speed over reliability
* Port accessibility may depend on firewall configuration

---

## Learning Approach

This repository is intentionally minimal and transparent. Each implementation is designed to be readable and modifiable, encouraging experimentation and deeper analysis.

The focus is not just on making things work, but on understanding why they work.

---

## Future Enhancements

* Concurrent multi-client TCP server
* Asynchronous socket handling
* Real-time chat system
* File transfer over sockets
* Encryption and secure communication layers
* Integration with higher-level protocols

---

## Author

Shashank Shekhar
Computer Science Student | Backend and Systems Development Focus
