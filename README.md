# Write 365 Filler

Automatedly fill Write365 Entries.

# Notes

- The entries created currently reliable (>90%) pass WordSalad checks.
- When I took WR121H, an open challenge was issued whereupon one could automatedly fill out entries if they could find out how to. This is my response. Your situation may vary.

# Requirements

```bash
sudo apt install -y xdotool
pip install essential_generators --user
```

# Usage

- Open write365
- Start a new entry (I know, i didnt automate it -- you have Duo to blame for that).
- `python3 fill.py` or `./fill.py`
- Select text box that you want to fill
- Give it ~5 mins at most, don't click away

# Disclaimer

Use this program at your own risk - its not my fault if you get in trouble. 
