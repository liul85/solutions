class Solution(object):
    def get_common_prefix(self, strs):
        if not strs: return ""
        min_str = min(strs, key=len)
        
        def has_common_prefix(strs, prefix):
            for s in strs:
                if not s.startswith(prefix):
                    return False
            return True

        for s in [ min_str[:len(min_str) - i] for i in range(len(min_str))]:
            if has_common_prefix(strs, s): return s
        return ""
