

class AppError(Exception):
    description=""
    http_code=500
    details={}

    def __init__(self,**kwargs):
        super.__init__(self.description)
        self.set_details(kwargs)
        if 'http_code' in kwargs:
            self.http_code=kwargs.pop('http_code',self.http_code)
    def __str__(self) -> str:
        return  f"Description:{self.description},Details:{self.details},http_code:{self.http_code}"
    def set_details(self,kwargs):
        self.details=kwargs
    def to_dict(self):
        return{
            "description":self.description,
            "details":self.details,
            "http_code":self.http_code
        }
        
    

