class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        retSet = set()
        for email in emails:
            local, domain = "".join(email.split("@")[:-1]), email.split("@")[-1]
            localIgnoredPlus = local.split("+")[0]
            localIgnoredDot = "".join(localIgnoredPlus.split("."))
            retSet.add("{}@{}".format(localIgnoredDot, domain))
        return len(retSet)
            