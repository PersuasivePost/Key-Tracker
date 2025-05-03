[01:50, 04/05/2025] ASHVATTH JOSHI: mini cctv for keyboards

add
react dashboard to view multiple screens (unique id to each screen)
oaut2 for authentication 
docker support
prisma orm maybe to store updated data each time
to scale to next level: kafka apache, kubernets and maybe go server instead of typescript
[01:50, 04/05/2025] ASHVATTH JOSHI: python script ready
[01:51, 04/05/2025] ASHVATTH JOSHI: make socket server, add dashboard, authentication remaining, docker and prisma for storage, maybe integrate with cloud


..
keystroke-monitor/
├── client/                        # Python Client Agent (runs on desktops)
│   ├── tracker_sync.py            # Main tracker + sync to server
│   ├── requirements.txt           # Python dependencies
│   ├── README.md                  # How to setup client
│   └── .desktop_template          # (optional) Autostart template for Ubuntu
│
├── server/                        # WebSocket Server (central collector)
│   ├── server.js                  # Node.js WebSocket server
│   ├── package.json               # Node dependencies
│   ├── logs.json                  # Stores all received keystrokes
│   └── README.md                  # How to run server
│
├── viewer/                        # Viewer (Admin panel to view data)
│   ├── cli_viewer.py              # Simple CLI viewer (optional)
│   └── react-dashboard/           # (optional) Fancy React dashboard
│       ├── package.json
│       ├── src/
│       └── public/
│
├── .gitignore                     # Ignore Python/Node modules/logs
├── LICENSE                        # Choose your license (MIT recommended)
└── README.md                      # Top level project doc

..


..
keystroke-monitor/
├── client/
│   ├── tracker.py          # (Your tracker.py here)
│   ├── encryptor.py        # (Your encryptor.py here)
│   ├── tracker_sync.py     # (NEW: we’ll build this for server sync)
│   ├── requirements.txt
│   ├── README.md
│   └── .desktop_template
│
├── server/
│   ├── server.js
│   ├── package.json
│   ├── logs.json
│   └── README.md
│
├── viewer/
│   ├── cli_exporter.py     # (Your export_logs.py here, renamed optional)
│   ├── cli_viewer.py       # (Your view_logs.py here)
│   └── react-dashboard/
│       ├── package.json
│       ├── src/
│       └── public/
│
├── .gitignore
├── LICENSE
└── README.md
..

# Ill continue some day later but will make this spy thing fs!!