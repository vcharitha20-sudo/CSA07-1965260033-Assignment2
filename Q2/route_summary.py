"""Route summarisation by common prefix."""
import ipaddress

def summarise(networks):
    nets=[ipaddress.ip_network(n, strict=False) for n in networks]
    first=min(int(n.network_address) for n in nets)
    last=max(int(n.broadcast_address) for n in nets)
    used=sum(n.num_addresses for n in nets)
    for length in range(32,-1,-1):
        shift=32-length
        if (first >> shift)==(last >> shift):
            base=(first >> shift)<<shift
            return f"{ipaddress.IPv4Address(base)}/{length}",2**shift,used

PLANS={
 "Four regional offices":["172.18.24.0/24","172.18.25.0/24","172.18.26.0/24","172.18.27.0/24"],
 "Fifth office added":["172.18.24.0/24","172.18.25.0/24","172.18.26.0/24","172.18.27.0/24","172.18.28.0/24"],
 "Gap in the numbering":["10.4.0.0/24","10.4.2.0/24","10.4.3.0/24"]}
for name,nets in PLANS.items():
    summary,covered,used=summarise(nets)
    print(f"{name:<22} {summary:<16} covers {covered:5d} owned {used:5d} extra {covered-used}")
