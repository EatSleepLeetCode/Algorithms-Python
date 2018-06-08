class Solution(object):
    def maskPII(self, S):
        if '@' in S:
            first, after = S.split('@')
            return "{}*****{}@{}".format(first[0], first[-1], after).lower()

        digits = filter(unicode.isdigit, S)
        local = "***-***-{}".format(digits[-4:])
        if len(digits) == 10:
            return local
        else:
            return "+{}-{}".format("*" * (len(digits) - 10), local)