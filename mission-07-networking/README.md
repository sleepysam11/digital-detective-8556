# Mission 7 — How computers communicate

## 1. Mission title
Mission 7 — How computers communicate

## 2. Task / objective
Explain fundamental computer networking concepts, observe actual connectivity and DNS lookup outputs, and describe the complete step-by-step communication lifecycle when opening a website.

## 3. Work completed
- [x] Completed the network concepts table with explanations and real-world examples.
- [x] Executed a connectivity check (`ping -c 4 example.com`) and recorded verified privacy-safe results.
- [x] Executed a DNS resolution test (`nslookup example.com`) and recorded resolved addresses.
- [x] Answered all three questions regarding connectivity testing, DNS outputs, and the browser lookup role.
- [x] Documented the 7-step website loading sequence using correct networking terminology.

### Task 7.1 — Network concepts table

| Concept | Explain it in your own words | Example |
|---|---|---|
| **LAN** | Local Area Network: Connects computing devices across a small, confined geographic area such as a residence, classroom, or office building | A home Wi-Fi network connecting laptops, smartphones, and a wireless printer |
| **MAN** | Metropolitan Area Network: Connects multiple networks across an entire municipality, town, or university campus | A connected city-wide smart utility network or multi-campus university network |
| **WAN** | Wide Area Network: Interconnects computer systems across broad geographic distances including regions, countries, and continents | The global Internet connecting millions of private and public networks worldwide |
| **DNS** | Domain Name System: Translates human-friendly alphanumeric domain names into numeric IP addresses that routers navigate | Resolving `example.com` into IPv4 addresses `172.66.147.243` / `104.20.23.154` |
| **Router** | A networking device that routes and forwards data packets across distinct networks based on IP routing tables | A home wireless gateway router forwarding packets between the home LAN and the ISP |
| **Protocol** | A standardized set of syntactic and semantic rules governing how devices format, transmit, and acknowledge data | HTTP/HTTPS for web documents, TCP for reliable transmission, IP for addressing |
| **Packet switching** | Splitting message payloads into discrete digital packets that travel independently across network paths and reassemble at the destination | Web requests broken into small IP packets that navigate distinct hops before reassembly |
| **Client-server** | An architecture where client systems request resources or processing from a centralized host (server) | A web browser (client) requesting an HTML page from a remote web server (server) |

### Task 7.2 — Observe network information

**Connectivity test (`ping -c 4 example.com`):**

```bash
$ ping -c 4 example.com
PING example.com (104.20.23.154): 56 data bytes
64 bytes from 104.20.23.154: icmp_seq=0 ttl=56 time=23.345 ms
64 bytes from 104.20.23.154: icmp_seq=1 ttl=56 time=41.446 ms
64 bytes from 104.20.23.154: icmp_seq=2 ttl=56 time=39.192 ms
64 bytes from 104.20.23.154: icmp_seq=3 ttl=56 time=117.962 ms

--- example.com ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 23.345/55.486/117.962/36.739 ms
```

*(Personal IP address and local Wi-Fi gateway redacted.)*

**DNS resolution (`nslookup example.com`):**

```bash
$ nslookup example.com
Server:     [DNS-Server-Redacted]
Address:    [DNS-IP-Redacted]#53

Non-authoritative answer:
Name:   example.com
Address: 172.66.147.243
Name:   example.com
Address: 104.20.23.154
```

**Questions answered:**
- **What a connectivity test helps check:** A connectivity test (`ping`) verifies whether two network endpoints can establish basic two-way communication using ICMP packets. It confirms route reachability, estimates round-trip latency in milliseconds, and identifies packet drops.
- **What information a DNS lookup displays:** An `nslookup` query reveals the responding DNS nameserver and the canonical host record, along with the resolved IP addresses (in this test, `172.66.147.243` and `104.20.23.154`) associated with the queried domain name.
- **The role of DNS when entering a website name:** Web browsers require numeric IP addresses to open network sockets. When a user types a human-readable domain like `example.com`, the browser queries the DNS system to resolve that name into an IP address before any web page data can be requested.

### Task 7.3 — What happens when you open a website?

1. **User input:** The user types `https://example.com` into the web browser (the client) and presses Enter.
2. **DNS name resolution:** The client checks its local cache; if not found, it queries a configured recursive DNS server using the DNS protocol to look up the destination IP address (`104.20.23.154`).
3. **Packet routing:** The client constructs network packets addressed to the resolved IP. The local router examines the destination headers and forwards the packets across intermediate autonomous systems.
4. **Transport layer connection (TCP Handshake):** The client initiates a reliable Transmission Control Protocol (TCP) three-way handshake (`SYN`, `SYN-ACK`, `ACK`) with the destination server over port 443.
5. **Security handshake (TLS):** Because HTTPS is specified, the client and server complete a TLS (Transport Layer Security) handshake to authenticate the server and negotiate cryptographic keys for encryption.
6. **HTTP request and server response:** The client issues an HTTP `GET /` request protocol payload. The destination web server processes the request, locates the resource, and transmits an HTTP `200 OK` response payload containing the HTML document across packet-switched paths.
7. **Rendering:** The client's browser receives and reassembles the incoming packets, parses the HTML/CSS/JavaScript structure, and renders the visual web page on the user's screen.

## 4. Commands / tools used
- `ping -c 4 example.com`: Measures network reachability and round-trip transmission latency.
- `nslookup example.com`: Performs DNS resolution against recursive nameservers.

## 5. My understanding
Computer networks function as layered systems governed by common protocols. Packet switching enables resilient, shared transmission. DNS bridges human terminology with binary IP routing, and the client-server paradigm underpins modern internet applications.

## 6. Difficulties faced
No difficulties. All four ICMP echo packets were acknowledged with 0.0% packet loss and an average latency of 55.486 ms.

## 7. How I resolved them
Not applicable. Network connectivity and DNS resolution succeeded on the first attempt.

## 8. Evidence / files
- Privacy-safe outputs of `ping -c 4 example.com` and `nslookup example.com` recorded in Section 3 and in `evidence/mission-07-network-tests.txt`.

## 9. Commit details
- Commit message: Complete Mission 7 networking notes
- Short commit hash: 5ef15b4
- Pushed to GitHub: Yes
