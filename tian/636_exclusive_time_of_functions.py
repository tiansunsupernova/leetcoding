class Log:
    def __init__(self, log):
        items = log.split(':')
        self.id = int(items[0])
        self.status = items[1]
        self.time = int(items[2])
    
    def __lt__(self, other):
        return self.time < other.time 

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        st = []
        
        for cur in logs:
            log = Log(cur)
            if log.status == "start":
                st.append(log)
            else:
                last = st.pop()
                length = log.time - last.time + 1
                res[last.id] += length
                if st:
                    res[st[-1].id] -= length
        return res
            

