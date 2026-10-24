# Local dashboard

To view a quick overview of the project:

```bash
cd labbook/dashboard
python3 -m http.server 8765 --bind 127.0.0.1
```

Agents can update the small JSON files in `status/`, but each entry must link to an analysis `STATE.md`. The dashboard only displays status; it never changes it.
