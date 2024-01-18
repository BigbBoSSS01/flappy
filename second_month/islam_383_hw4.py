class SavingAccount:...



class CheckingAccount:...


class Stock:...
class Bond:...


class Security(Stock, Bond):...


class BankAccount(SavingAccount, CheckingAccount):...



class InterestBearingltem(BankAccount, Security):...



class RealEstate:...



class Asset(BankAccount,RealEstate,Security):...


class Insurableltem(RealEstate, BankAccount):...









