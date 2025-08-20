# EX-TOOLS-1
### Task Description:
Run a web server with just one page displaying your name and photo. In your project README.md, provide the link to the website. Describe how you set it up. No need for any fancy HTML. This serves as proof that you completed the setup tasks.

## Solution:
1. **Getting a VPS instance setup**
	- I chose hetzner as my provider, and started a debian instance at `49.13.203.98`
	- Made firewalls rules and exposed port `80`
	- Added a DNS A record to my domain which is managed by cloudflare to point `debbie.itsdhruv.in` to my server

2. **SSH'd into the server and setup my project files**
	- Made this `README.md` and a directory for the `webpage`
	- Created an `index.html` with my name and image
	- Wrote a bash script to take in a `PORT` value and run the server
```bash
PORT=${1:-8000}
python3 -m http.server "$PORT"
```
3. **Ran the server and verified my result**
	- The page was now being served to `49.13.203.98:80` and `debbie.itsdhruv.in` 
	- <img src="https://gcdnb.pbrd.co/images/pBZ5kFoxKmkn.png?o=1" alt="drawing" width="400"/>