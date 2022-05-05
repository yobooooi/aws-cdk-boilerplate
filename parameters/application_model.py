from typing import List


class GeneralModel:
    def __init__(
        self,
        AppName,
        ProductOwner,
        NamePrefix,
        PrimaryOperatingRegion,
        EnabledRegions,
        MemberAccounts: List,
    ):

        self.AppName = AppName
        self.ProductOwner = ProductOwner
        self.NamePrefix = NamePrefix
        self.EnabledRegions = EnabledRegions
        self.PrimaryOperatingRegion = PrimaryOperatingRegion
        self.MemberAccounts = MemberAccounts
