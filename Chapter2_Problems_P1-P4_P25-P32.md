# Kurose & Ross - Computer Networking: A Top-Down Approach
# Chapter 2 (Application Layer) - Problems P1-P4, P25-P32 Solutions

---

## Problem 1 (True or False)

**a)** A user requests a Web page that consists of some text and three images. For this page, the client will send one request message and receive four response messages.

**Answer: FALSE**

The client sends **four** request messages (one for the base HTML and one for each of the three images) and receives four response messages. Each embedded object requires a separate HTTP request.

**b)** Two distinct Web pages (e.g., www.mit.edu/research.html and www.mit.edu/students.html) can be sent over the same persistent connection.

**Answer: TRUE**

With HTTP/1.1 persistent connections, multiple requests and responses can be sent over the same TCP connection. The client can request multiple objects from the same server without opening new connections.

**c)** With non-persistent connections between browser and origin server, it is possible for a single TCP segment to carry two distinct HTTP request messages.

**Answer: FALSE**

With non-persistent connections, each HTTP request uses a separate TCP connection. After each request-response, the connection is closed. A single TCP segment cannot carry two distinct HTTP requests in this model.

**d)** The Date: header in the HTTP response message indicates when the object in the response was last modified.

**Answer: FALSE**

The Date: header indicates when the **response** was generated/sent by the server, not when the object was last modified. The Last-Modified: header indicates when the object was last modified.

**e)** HTTP response messages never have an empty message body.

**Answer: FALSE**

HTTP response messages CAN have empty bodies. For example, responses to HEAD requests and 204 No Content responses have empty bodies.

---

## Problem 2

**a) What are the main differences between HTTP and FTP?**

- **FTP** uses **two parallel TCP connections**: (1) a control connection for commands (user ID, password, directory changes, etc.) and (2) a data connection for the actual file transfer. FTP sends control information **out-of-band**.

- **HTTP** uses a **single TCP connection** for both request/response headers and the data transfer. HTTP sends control information **in-band** within the same connection that carries the data.

**b) How does SMTP mark the end of a message body?**

SMTP uses a line containing only a period (.) to mark the end of a message body. When the SMTP client sends a line with just ".", the server knows the message body has ended.

---

## Problem 3

Referring to Example 2, suppose the HTML file references eight very small objects on the same server. Neglecting transmission times, how much time elapses with:

**a) Non-persistent HTTP?**

With non-persistent HTTP, each object requires a separate TCP connection: 1 RTT to establish connection + 1 RTT to request and receive.

- 1 RTT for initial TCP + 1 RTT for base HTML = 2×RTT₀ for base object
- 8 objects × 2×RTT₀ = 16×RTT₀ for embedded objects

**Total: RTT₁ + ... + RTTₙ + 2×RTT₀ + 8×2×RTT₀ = RTT₁ + ... + RTTₙ + 18×RTT₀**

(Where RTT₁...RTTₙ are DNS RTTs, RTT₀ is the RTT to the server)

**b) Persistent HTTP?**

With persistent HTTP, one TCP connection is used for all objects. Each additional object needs 1 RTT.

- 1 RTT for TCP + 1 RTT for base HTML = 2×RTT₀
- 8 objects × 1 RTT each = 8×RTT₀

**Total: RTT₁ + ... + RTTₙ + 2×RTT₀ + 8×RTT₀ = RTT₁ + ... + RTTₙ + 10×RTT₀**

---

## Problem 4 (DNS - dig tool)

**a) Delegation chain for www.cse.yorku.ca:**

1. a.root-servers.net (root)
2. j.ca-servers.ca (for .ca TLD)
3. dns11.ipns.yorku.ca (for yorku.ca)
4. ns2.cse.yorku.ca (authoritative for cse.yorku.ca)

**Commands:**
```
dig +norecurse @a.root-servers.net any www.cse.yorku.ca
dig +norecurse @j.ca-servers.ca any www.cse.yorku.ca  
dig +norecurse @dns11.ipns.yorku.ca any www.cse.yorku.ca
```

**b) For www.google.com:** d.root-servers.net → d.gtld-servers.net → ns2.google.com

**For www.yahoo.com:** h.root-servers.net → k.gtld-servers.net → ns1.yahoo.com

*Use: dig www.domain.com +trace* to show the full delegation chain.

---

## Problems P25-P32

*Note: Problem numbering varies by textbook edition. These cover common Chapter 2 Application Layer topics.*

### P25 - DNS Caching

**Problem:** Can a local DNS server determine if an external website was accessed recently from a computer in the department?

**Answer:** Yes. Query the site using dig against the local DNS server. If the site was accessed recently, it may be in the local cache, resulting in a very short (near-zero) query time. If not cached, the query takes longer as it traverses the DNS hierarchy.

---

### P26 - HTTP Conditional GET

**Problem:** What is the purpose of the If-Modified-Since header?

**Answer:** It enables conditional GET. The client sends the Last-Modified date it received previously. If the object hasn't changed, the server responds with "304 Not Modified" and an empty body, saving bandwidth. If modified, the server sends the full object with 200 OK.

---

### P27 - SMTP vs HTTP

**Problem:** Why does SMTP use CRLF.CRLF to signal end of message while HTTP uses Content-Length?

**Answer:** SMTP was designed for 7-bit ASCII and uses the period on a line by itself (CRLF.CRLF) as a simple delimiter. HTTP supports binary data and variable encoding, so Content-Length provides the exact byte count of the body, which is more reliable for non-ASCII content.

---

### P28 - File Transmission Delay

**Problem:** Two hosts are 20,000 km apart, connected by a 2 Mbps link. A 5 MB file is to be transferred. Propagation speed is 2.5×10⁸ m/s.

**a) Transmission delay:** 
- D_trans = L/R = (5×10⁶×8 bits) / (2×10⁶ bps) = 20 seconds

**b) Propagation delay:**
- D_prop = d/s = (20×10⁶ m) / (2.5×10⁸ m/s) = 0.08 seconds = 80 ms

**c) End-to-end delay (ignoring processing):**
- D = D_trans + D_prop ≈ 20.08 seconds

---

### P29 - Web Caching

**Problem:** How does a web cache reduce delay for requested objects?

**Answer:** The cache stores copies of previously requested objects. When a request arrives, if the object is in the cache (and valid), the cache serves it directly without contacting the origin server. This reduces delay because the round-trip to the cache (often on the same LAN) is much shorter than to the origin server.

---

### P30 - HTTP Methods

**Problem:** List the main HTTP request methods.

**Answer:** GET (retrieve), POST (submit data), HEAD (headers only), PUT (upload/replace), DELETE (remove), OPTIONS (supported methods), TRACE (echo request), CONNECT (tunnel).

---

### P31 - Persistent vs Non-Persistent HTTP

**Problem:** Compare persistent and non-persistent HTTP in terms of connections.

**Answer:** 
- **Non-persistent:** Each request-response uses a new TCP connection. High overhead due to repeated connection setup.
- **Persistent:** Single TCP connection for multiple requests. Lower overhead, faster for pages with multiple objects.

---

### P32 - DNS Records

**Problem:** What are the main types of DNS resource records?

**Answer:**
- **A:** Hostname to IPv4 address
- **AAAA:** Hostname to IPv6 address  
- **NS:** Authoritative name server for a zone
- **CNAME:** Canonical name (alias)
- **MX:** Mail server for domain
- **PTR:** Reverse lookup (IP to hostname)

---

*Solutions based on Kurose & Ross "Computer Networking: A Top-Down Approach"*
