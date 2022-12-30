class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        masterDict = collections.defaultdict(int)
        ret = []
        for i in cpdomains:
            rep, reversedDomainSplit = int(i.split()[0]), i.split()[1].split(".")[::-1]
            domainStr = ""
            for subD in reversedDomainSplit:
                domainStr = subD if not domainStr else "{}.{}".format(subD, domainStr)
                masterDict[domainStr] += rep
        for k,v in masterDict.items():
            ret.append("{} {}".format(v, k))
        return ret