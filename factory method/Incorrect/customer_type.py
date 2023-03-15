from enum import Enum


class CustomerType(Enum):
    PAY_AS_YOU_GO: 1
    UNLIMITED: 0
    

class Customer:
    def __init__(self, customer_type: CustomerType) -> None:
        self.customer_type = customer_type
        
class MonthlyUsage:
    def __init__(self, customer: Customer, call_minutes: int, sms_count: int) -> None:
        self.customer = customer
        self.call_minutes = call_minutes
        self.sms_count = sms_count

class MonthlyStatement:
    def __init__(self) -> None:
        self.call_cost: float
        self.sms_cost: float
        self.total_cost: float

    def generate(self, monthly_usage: MonthlyUsage):
        if (monthly_usage.customer.customer_type == CustomerType.PAY_AS_YOU_GO):
            self.call_cost = 0.12 * monthly_usage.call_minutes
            self.sms_cost = 0.12 * monthly_usage.sms_count
            self.total_cost = self.call_cost + self.sms_cost
        elif (monthly_usage.customer.customer_type == CustomerType.PAY_AS_YOU_GO):
            self.total_cost = 54.90
        else:
            raise Exception("The current customer type is not supported")
