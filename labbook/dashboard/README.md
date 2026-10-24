# Local dashboard

Serve this directory locally when a lightweight project overview is useful:

```bash
cd labbook/dashboard
python3 -m http.server 8765 --bind 127.0.0.1
```

Agents may update small JSON files in `status/`, but every entry must link back to an analysis `STATE.md`. Keep the dashboard read-only with respect to scientific state.
