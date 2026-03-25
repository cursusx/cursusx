# Cursusx

**Cursusx** is an open-source command-line tool for interacting with networks. It is built to be minimal, readable, and easy to extend. Currently it supports the following commands:

- `http` — query HTTP endpoints

---

## HTTP Command

The `http` command lets you query any network endpoint. It is designed to be straightforward and expressive, without requiring boilerplate configuration files.

### Supported options

| Flag | Description |
|---|---|
| `-method` | HTTP method (`get`, `post`, `put`, `delete`, …) |
| `-endpoint` | Target URL |
| `-headers` | Request headers as a JSON string |
| `-parameters` | Query parameters as a JSON string |

> Coming soon: `-cookies` and `-auth` support.

### Basic usage
```bash
./cursusx.py http \
  -method=get \
  -endpoint=http://127.0.0.1:5000 \
  -headers="{\"your\": \"headers\"}" \
  -parameters="{\"your\": \"parameters\"}"
```

### Pretty output

Prefix any command with `pretty` to get a formatted, human-readable response rendered in the terminal UI:
```bash
./cursusx.py pretty http \
  -method=get \
  -endpoint=http://127.0.0.1:5000 \
  -headers="{\"your\": \"headers\"}" \
  -parameters="{\"your\": \"parameters\"}"
```

---

## Roadmap

| Feature | Status |
|---|---|
| HTTP command | ✅ Available |
| Cookies support | 🔜 Planned |
| Authentication | 🔜 Planned |
| Packet sniffing | 🔜 Planned |

---

## Contributing

Cursusx is open source — contributions, issues, and feature requests are welcome.