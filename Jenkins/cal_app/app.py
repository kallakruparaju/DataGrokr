def lambda_handler(event, context):
    class Calculator:
        def add(self, a, b):
            return a + b
        
        def subtract(self, a, b):
            return a - b
        
        def multiply(self, a, b):
            return a * b
    cal = Calculator()
    print(cal.add(1,2))