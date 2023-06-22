class Validator:
    
    @staticmethod
    def not_null(object,param_name:str):
        if object is None:
            raise Exception(f"{param_name} must not be null")
        else:
            return object
        
    
    @staticmethod
    def check_age(age,param_name:str):
        if age<0 or type(age) is not int:
            raise Exception(f"{param_name} must have a valid age")
        else:
            return age