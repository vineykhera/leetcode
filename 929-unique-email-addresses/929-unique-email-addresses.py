class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        outemails = set()
        for email in emails:
            validemail = ""
            eid = email.split("@")
            # print(eid)
            for ch in eid[0]:
                if ch == ".":
                    continue
                if ch == "+":
                    break
                validemail += ch
            validemail = validemail + "@" + eid[1]
            outemails.add(validemail)
            # print(outemails)
        return len(outemails)