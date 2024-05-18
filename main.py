
from tabulate import tabulate


# username: current plan, duration plan, referal_code
data = {
    "Anisatul" : ["Standard Plan", 13, "anisa-123"],
    "Andy" : ["Premium Plan", 10, "andy-123"],
    "Shandy" : ["Basic Plan", 12, "shandy-2134"],
    "Cahya" : ["Standard Plan", 24, "cahya-abcd"],
    "Ana" : ["Premium Plan", 5, "ana-f29g"],
    "Bagus" : ["Basic Plan", 11, "bagus-9f92"]
}

# create user class

class User:

    def __init__(self, username: str):
        self.username = username

    # method check plan
    def check_benefit(self):
        """Method uang digunakan untuk menampilkan all benefits dari PacFlix"""
        # init headers
        headers = [ "Benefits", "Basic Plan", "Standard Plan", "Premium Plan"]

        # init data
        table = [
        ['Can Stream', True, True, True],
        ["Can Download", True, True, True],
        ["Has SD", True, True, True],
        ["Has HD", False, True, True],
        ["Has UHD", False, False, True],
        ["Num of devices", 1, 2, 4],
        ["Content", "3rd party movie only", "Basic Plan Content + Sports(F1, Football, Basketball)", "Basic Plan + Standard Plan + PackFlix Original Series or Movie"],
        ["Price", 120_000, 160_000, 200_000]
        ]

        print("=====PacFlix Plan List=====")
        print(tabulate(table, headers, tablefmt="github"))

    # method check benefit based on username input
    def check_plan(self, username):
        """
        Method yang digunakan untuk mengambil data user PacFlix based on username
        Parameters
        ----------
        username (str): input username
        """
        # iterate keys and values based on data
        for keys, values in data.items():

            # create variable to store the value
            get_current_plan = values[0]
            get_duration_plan = values[1]

            # branching to filter username
            if username == keys:
                print(f"username: {username}")
                print(f"current plan: {get_current_plan}")
                print(f"duration plan: {get_duration_plan}")
            
    # method upgrade plan based on username
    def upgrade_plan(self, username:str, upgrade_plan:str) -> float:
        """
        Method untuk upgrade subscription PacFlix
        
        Parameters
        ----------
        ....
        
        Returns
        -------
        ....
        """
        DISCOUNT = 0.05

        # iterate keys and values based on data
        for keys, values in data.items():

            try:
                # create branching to filter username
                if username == keys:

                    # create variable to store the value
                    get_current_plan = values[0]
                    get_duration_plan = values[1]

                    if upgrade_plan != get_duration_plan:
                        # filter duration plan to get a discount 5%
                        if get_duration_plan > 12:
                            # logic discount
                            if upgrade_plan == "Basic Plan":
                                total_price = 120_000 - (120_000 * DISCOUNT)

                                return total_price
                        
                            elif upgrade_plan == "Standard Plan":
                                total_price = 160_000 - (160_000 * DISCOUNT)

                                return total_price
                        
                            elif upgrade_plan == "Premium Plan":
                                total_price = 200_000 - (200_000 * DISCOUNT)

                                return total_price
                        
                            else:
                                raise Exception ("Unknown Plan")

                        else:
                            # branching if not discount
                            if upgrade_plan == "Basic Plan":
                                total_price = 120_000

                                return total_price
                        
                            elif upgrade_plan == "Standard Plan":
                                total_price = 160_000

                                return total_price
                        
                            elif upgrade_plan == "Premium Plan":
                                total_price = 200_000

                                return total_price
                        
                            else:
                                raise Exception ("Unknown Plan") 
                        
                    else:
                        raise Exception("Plan tidak boleh sama!")

            except:
                raise Exception("Unknown Process")
            


# create New User OBJECT

class NewUser:

    referral_code = []

    def __init__ (self, username: str):
        self.username = username

    # method to extract referral code from dictionary
    def get_referreal_code (self, data):
        """
        Method untuk extract Referral Code pada dictionary data
        ...
        """
        # iterate to data
        for value in data.values():
            ref_code = value[2]

            # append to empty list
            self.referral_code.append(ref_code)

        return self.referral_code
    
    # method untuk new user pick plan
    def pick_plan(self, new_plan, referral_code):

        # initiate discount
        DISCOUNT = 0.04

        if referral_code in self.referral_code:
            # proses lanjut
            if new_plan == "Basic Plan":
                total_price = 120_000 - (120_000 * DISCOUNT)

                return total_price

            elif new_plan == "Standard Plan":
                total_price = 160_000 - (160_000 * DISCOUNT)

                return total_price
            
            elif new_plan == "Premium Plan":
                total_price = 200_000 - (200_000 * DISCOUNT)

                return total_price
            
            else:
                raise Exception ("Unknown Plan")

        else:
            raise Exception("Referral code tidak ada!!!")
        


dummy_user = User(username = "Shandy")
dummy_user.check_benefit()