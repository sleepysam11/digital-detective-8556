# Mission 7 — How computers communicate

## 1. Mission title
Mission 7 — How computers communicate

## 2. Task / objective
Understand common network types and services, run a basic connectivity check and DNS lookup, and explain the steps involved in opening a website.

## 3. Work completed

### Networking terms
| Term | Meaning |
|---|---|
| LAN | Local Area Network: connects devices in a limited area such as a home, school, or office. |
| MAN | Metropolitan Area Network: connects networks across a town or city-sized area. |
| WAN | Wide Area Network: connects networks over large geographic areas. The Internet is the best-known example. |
| DNS | Domain Name System: looks up information such as the IP address associated with a domain name. |
| Router | A device that forwards packets between networks. |
| Protocol | Agreed rules that devices use to communicate, such as TCP, IP, and HTTP. |
| Packet switching | Breaks data into packets that can travel across networks and be reassembled at the destination. |
| Client-server | A model where a client requests a service or resource and a server responds. |

### Connectivity and DNS checks
Run these commands on the Mac:

```bash
ping -c 4 example.com
nslookup example.com
```

- `ping -c 4 example.com` sends four test packets and reports whether replies arrive and the measured round-trip times. Some networks block or limit ping, so no reply does not always mean a website is unavailable.
- `nslookup example.com` asks DNS to resolve the domain and displays the DNS response.

Record only whether the commands succeeded and a short, privacy-safe summary. Do not publish your own IP address, Wi-Fi name, local network details, or full terminal output. DNS answers can vary by time and network.

### What happens when a website opens
1. The user enters a website address in a browser.
2. The browser checks whether it already has useful cached information.
3. DNS resolves the domain name to an IP address.
4. The device sends network packets through its local network and router toward the destination.
5. The browser and server establish a connection; HTTPS also performs a TLS security handshake.
6. The browser sends an HTTP request and the server returns a response.
7. The browser interprets the returned HTML, CSS, JavaScript, and other resources and displays the page.

## 4. Commands / tools used
`ping -c 4 example.com` checks basic network reachability. `nslookup example.com` checks DNS name resolution.

## 5. My understanding
A network allows devices to exchange data using shared protocols. DNS makes domain names easier to use than numeric IP addresses. Routers forward packets between networks, and client-server communication lets a browser request web content from a server.

## 6. Difficulties faced
The connectivity and DNS commands have not yet been run on the student's network. Network filtering may affect ping results.

## 7. How I resolved them
Run both commands locally. If ping receives no replies, note that the network may block ICMP traffic and use the DNS lookup as a separate test. Redact all private network information before sharing evidence.

## 8. Evidence / files
- This README — networking definitions and website-loading sequence.
- Pending: privacy-safe summary of local ping and DNS results.

## 9. Commit details
- Commit message: Complete Mission 7 networking notes
- Short commit hash: See the commit history for the `update-about` branch.
- Pushed to GitHub: Yes, after the branch update is confirmed.
