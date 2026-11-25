# Mission 7 — How computers communicate

## 1. Mission title
Mission 7 — How computers communicate

## 2. Task / objective
The objective of this mission was to understand key networking concepts (LAN, MAN, WAN, DNS, router, protocol, packet switching and client-server), run real connectivity and DNS lookup commands, and explain step-by-step what happens when a web page is opened in a browser.

## 3. Work completed
- [x] Explain LAN, MAN, WAN, DNS, router, protocol, packet switching and client-server.
- [x] Run a connectivity check for `example.com`.
- [x] Perform a DNS lookup for `example.com`.
- [x] Explain what each command checks and record privacy-safe results.
- [x] Write a 5–7 step explanation of what happens when a website opens.

---

### Key networking terms

| Term | Explanation |
|---|---|
| **LAN** (Local Area Network) | A network connecting devices within a small area — for example, all the computers and phones in one home or classroom connected to the same Wi-Fi router |
| **MAN** (Metropolitan Area Network) | A network spanning a city or campus — larger than a LAN but smaller than a WAN. Example: a university network connecting buildings across a campus |
| **WAN** (Wide Area Network) | A network covering a large geographic area — countries or continents. The internet itself is the largest WAN |
| **DNS** (Domain Name System) | The internet's "phone book". It translates human-readable domain names (like `example.com`) into IP addresses (like `172.66.147.243`) that computers use to find each other |
| **Router** | A device that connects different networks and decides the best path for each packet of data to travel from sender to receiver |
| **Protocol** | A set of agreed rules for how data is formatted and exchanged. Examples: HTTP (web pages), TCP/IP (reliable delivery), DNS (name resolution) |
| **Packet switching** | Data is broken into small packets, each sent independently across the network, possibly via different routes, and reassembled at the destination |
| **Client-server model** | A client (e.g. my browser) sends a request; a server (e.g. a web server) processes it and sends a response back. The server holds resources; the client uses them |

---

### Connectivity check — ping example.com

```bash
$ ping -c 4 example.com
PING example.com (172.66.147.243): 56 data bytes
64 bytes from 172.66.147.243: icmp_seq=0 ttl=54 time=41.115 ms
64 bytes from 172.66.147.243: icmp_seq=2 ttl=54 time=22.141 ms
64 bytes from 172.66.147.243: icmp_seq=3 ttl=54 time=25.142 ms

--- example.com ping statistics ---
4 packets transmitted, 3 packets received, 25.0% packet loss
round-trip min/avg/max/stddev = 22.141/29.466/41.115/8.328 ms
```

*(My own IP address is not shown in this output.)*

**What `ping` checks:** It sends ICMP echo-request packets to the target host and waits for echo-reply packets. The round-trip time (in ms) shows how long data takes to travel from my machine to the server and back. 3 out of 4 packets were received — the 25% packet loss is likely due to some servers rate-limiting ICMP requests, not a real network problem.

---

### DNS lookup — nslookup example.com

```bash
$ nslookup example.com
Server:   8.8.8.8
Address:  8.8.8.8#53

Non-authoritative answer:
Name:  example.com
Address: 172.66.147.243
Name:  example.com
Address: 104.20.23.154
```

**What `nslookup` checks:** It queries a DNS server (`8.8.8.8` — Google's public DNS) and asks what IP address the domain `example.com` maps to. The result shows two IP addresses because `example.com` uses load balancing — different servers can handle requests, increasing reliability and speed.

---

### What happens when I open a website (step-by-step)

1. **I type `https://example.com` in my browser and press Enter.**
   The browser needs to find the server for this domain.

2. **DNS resolution.**
   The browser asks the DNS server "What is the IP address for `example.com`?" The DNS server replies with `172.66.147.243`.

3. **TCP connection established.**
   The browser uses TCP/IP to connect to that IP address on port 443 (HTTPS). A three-way handshake (SYN, SYN-ACK, ACK) sets up the connection.

4. **TLS handshake (HTTPS security).**
   The browser and server agree on encryption keys so the data transfer is private and secure.

5. **HTTP GET request sent.**
   The browser sends an HTTP GET request asking for the webpage: `GET / HTTP/1.1`. This is the client making a request to the server.

6. **Server sends a response.**
   The server processes the request and sends back an HTTP response with a status code (e.g. `200 OK`) and the HTML content of the page. The data travels as packets through the internet.

7. **Browser renders the page.**
   The browser receives and assembles the packets, parses the HTML, downloads any CSS, JavaScript or images referenced in it, and displays the finished page on screen.

## 4. Commands / tools used

| Command | Purpose |
|---|---|
| `ping -c 4 example.com` | Send 4 ICMP echo packets to `example.com` and measure round-trip time |
| `nslookup example.com` | Query DNS to find the IP address(es) for `example.com` |

## 5. My understanding
Computer networks work by breaking data into small packets and routing each one independently to its destination. DNS is crucial because humans use names but computers need numbers — DNS bridges that gap. The client-server model underlies almost everything on the internet: my browser is always a client, and every website runs on a server. Protocols like HTTP and TCP are just agreed rules so both sides know exactly how to format and send data, regardless of what hardware or operating system they use.

## 6. Difficulties faced
One ping packet (icmp_seq=1) timed out. This was expected because many public servers rate-limit or block ICMP ping requests as a security measure. It does not mean the site is down — the subsequent pings succeeded.

## 7. How I resolved them
I noted the packet loss in the evidence and confirmed the site was reachable from the other three replies and from the successful DNS lookup.

## 8. Evidence / files
- `ping -c 4 example.com` output recorded above (personal IP not shown).
- `nslookup example.com` output recorded above (shows only public DNS and server info).

## 9. Commit details
- Commit message: Explain networking concepts and website communication
- Short commit hash: 0d13673
- Pushed to GitHub: Yes
