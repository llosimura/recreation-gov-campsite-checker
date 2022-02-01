import unittest

from utils.camping_argparser import CampingArgParser


class CampingArgParserTest(unittest.TestCase):

    def setUp(self):
        self.start_date = ["--start-date", "2022-01-01"]
        self.end_date = ["--end-date", "2022-01-02"]
        self.parks = ["--parks", "111"]
        self.default_args = []
        self.default_args.extend(self.start_date)
        self.default_args.extend(self.end_date)
        self.default_args.extend(self.parks)

    def testCampsiteIdsWithMoreThanOneCampgroundIdThrowsException(self):
        with self.assertRaises(CampingArgParser.ArgumentCombinationError):
            args = ["--campsite-id", "333", "--parks", "1", "2"]
            args.extend(self.start_date)
            args.extend(self.end_date)
            CampingArgParser().parse_args(args)

    def testAcceptsMultipleCampsiteIds(self):
        args = ["--campsite-id", "333", "444"]
        args.extend(self.default_args)
        CampingArgParser().parse_args(args)

    def testAcceptsMultipleCampgroundIds(self):
        args = ["--parks", "333", "444"]
        args.extend(self.start_date)
        args.extend(self.end_date)
        CampingArgParser().parse_args(args)
