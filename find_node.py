import json

machine = "gh-runner-24227352594"

with open("status.json") as f:
    data = json.load(f)

node_id = ""

for peer in data.get("Peer", {}).values():
    if peer.get("HostName") == machine:
        node_id = peer.get("ID")
        break

with open("node.txt", "w") as f:
    f.write(node_id)
