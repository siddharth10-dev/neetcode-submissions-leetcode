class TimeMap:

    def __init__(self):
        self.db={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.db:
            self.db[key]=[]
        self.db[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.db:
            return ""


        values_list=self.db[key]


        l=0
        r=len(values_list)-1
        result=""
        while l<=r:
            m=(l+r)//2
            m_time,m_value=values_list[m]

            if m_time==timestamp:
                return m_value

            elif m_time<timestamp:
                result=m_value
                l=m+1
            else:
                r=m-1
            
        return result

        
