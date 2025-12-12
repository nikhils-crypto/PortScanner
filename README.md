🔍 PortScanner — Multi‑Threaded TCP Port Scanner (Python2  )

A lightweight, fast, and beginner‑friendly TCP port scanner built using Python sockets and multithreading.
This project is inspired by concepts from Violent Python but fully rewritten, improved, and modernized.

Designed for:

•Cybersecurity students
•Ethical hackers
•Networking beginners
•Anyone wanting to understand how port scanning works internally

🚀 Features:

✅ Multi‑threaded scanning
Scans multiple ports simultaneously for high performance.

✅ Banner Grabbing
Extracts service banners (e.g., FTP, SSH, HTTP) for fingerprinting.

✅ Hostname Resolution
Converts domain → IP and performs reverse DNS lookup.

✅ Custom Port Input
Scan one port or multiple ports separated by commas:
80,443,21,22

✅ Timeout Handling
Ensures fast execution even on closed/filtered ports.

✅ Clear Colored Output
Shows open/closed ports with service banner info.

📦 Installation
Clone the repository:

git clone https://github.com/nikhils-crypto/PortScanner.git
cd PortScanner


Run the script:
python port_scanner.py -H <target> -p <ports>

🛠 Usage Examples:
🔹 Scan a single port
python port_scanner.py -H scanme.nmap.org -p 80

🔹 Scan multiple ports
python port_scanner.py -H 192.168.1.10 -p 21,22,80,443

📂 Project Structure
PortScanner/
│── port_scanner.py     # Main scanner script
│── README.md           # Project documentation


🧠 How It Works (Technical Overview)

Parses CLI arguments using OptionParser
Resolves hostname → IP
Attempts reverse DNS lookup
Creates a thread for each port
Thread runs a TCP connect() attempt
If connection succeeds:
Sends a banner request
Receives up to 100 bytes
Prints OPEN port + banner
If connection fails:
Prints CLOSED port

⚠️ Legal / Ethical Disclaimer

This tool is for educational and ethical testing only.
Do NOT scan systems you do not own or do not have permission to test.

🤝 Contributing

Pull requests and feature suggestions are welcome.
Feel free to fork the repo and build your own tools!
