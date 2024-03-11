class LoyaltyProgram:
    global points; 
    
    @staticmethod
    def loyalty_points(total_cost):
        loyalty_points = 0 
        if total_cost >= 1000:
            loyalty_points+= 5
        return loyalty_points