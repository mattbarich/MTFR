import utils.gallatin
import utils.yellowstone

class Config:
    def __init__(self):
        self.gallatin_urls = {
            "bozeman fly supply": "https://www.bozemanflysupply.com/river-report/gallatin",
            "bfs": "https://www.bozemanflysupply.com/river-report/gallatin",
            "rivers edge": "https://theriversedge.com/pages/gallatin-river-fishing-report",
            "montana anglers": "https://www.montanaangler.com/montana-fishing-report/gallatin-river-fishing-report",
            "ma" : "https://www.montanaangler.com/montana-fishing-report/yellowstone-river-fishing-report",
            "yellowdog": "https://www.yellowdogflyfishing.com/pages/gallatin-river-fishing-report"
        }

        self.yellowstone_urls = {
            "bozeman fly supply": "https://www.bozemanflysupply.com/river-report/yellowstone",
            "bfs": "https://www.bozemanflysupply.com/river-report/yellowstone",
            "rivers edge": "https://theriversedge.com/pages/yellowstone-river-fishing-report",
            "montana anglers": "https://www.montanaangler.com/montana-fishing-report/yellowstone-river-fishing-report",
            "ma" : "https://www.montanaangler.com/montana-fishing-report/yellowstone-river-fishing-report",
            "yellowdog": "https://www.yellowdogflyfishing.com/pages/yellowstone-river-fishing-reports"
        }

        self.gallatin_report_functions = {
            "bozeman fly supply": utils.gallatin.bozemanFlySupplyReport,
            "bfs": utils.gallatin.bozemanFlySupplyReport,
            "rivers edge": utils.gallatin.riversEdgeReport,
            "montana anglers": utils.gallatin.montanaAnglersReport,
#            "ma" : utils.gallatin.montanaAnglersReport,
            "yellowdog": utils.gallatin.yellowDogReport
        }

        self.yellowstone_report_functions = {
            "bozeman fly supply": utils.yellowstone.bozemanFlySupplyReport,
            "bfs": utils.yellowstone.bozemanFlySupplyReport,
            "rivers edge": utils.yellowstone.riversEdgeReport,
            "montana anglers": utils.yellowstone.montanaAnglersReport,
 #           "ma" : utils.yellowstone.montanaAnglersReport,
            "yellowdog": utils.yellowstone.yellowDogReport
        }

# Dictionary for approved phone numbers.
        self.approved_phone_numbers = {
            "+11112223333" : "User1",
            "+12223334444" : "user2"
        }