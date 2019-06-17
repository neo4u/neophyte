class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split("+")[0]
            unique.add(local.replace(".", "") + '@' + domain)
        return len(unique)

# 929. Unique Email Addresses
# https://leetcode.com/problems/unique-email-addresses/description/
