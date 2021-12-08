class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        print(queryIP)
        if "." in queryIP and ":" in queryIP:
            return "Neither"
        elif "." in queryIP:
            return self.validIPv4(queryIP)
        elif ":" in queryIP:
            return self.validIPv6(queryIP)
        else:
            return "Neither"
    
    def validIPv4(self, queryIP):
        splitQuery = queryIP.split(".")
        if len(splitQuery) != 4:
            return "Neither"
        for n in splitQuery:
            if len(n) > 1 and len(n.lstrip("0")) != len(n):
                return "Neither"
            try:
                intOfN = int(n)
                if 0 > intOfN or intOfN > 255:
                    return "Neither"
            except ValueError:
                return "Neither"
        return "IPv4"
    
    def validIPv6(self, queryIP):
        splitQuery = queryIP.split(":")
        if len(splitQuery) != 8:
            return "Neither"
        for n in splitQuery:
            if len(n) > 4:
                return "Neither"
            try:
                int(n, 16)
            except ValueError:
                return "Neither"
        return "IPv6"
