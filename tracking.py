#Opens the tracking information for your package based on your carrier
#import needed packages and reset all vars
import webbrowser
trackingLink = 0
#Get tracking number and courrier from user
trackingNumber = input("What is your tracking number? ")
carrier = input("What is the package Carrier? ")
#Create tracking link
match carrier:
    case "USPS" | "usps":
        trackingLink = ("https://tools.usps.com/go/TrackConfirmAction_input?origTrackNum=" + trackingNumber)
    case "UPS" | "ups":
        trackingLink = ("https://www.ups.com/track?sort_by=status&tracknums_displayed=1&TypeOfInquiryNumber=T&loc=en_us&InquiryNumber1=" + trackingNumber + U"&requester=ST")
    case "FedEx" | "Fedex" | "fedex":
        trackingLink = ("https://www.fedex.com/wtrk/track/?trknbr=" + trackingNumber)
    case "dhl" | "DHL":
        trackingLink = ("https://www.dhl.com/us-en/home/tracking.html?tracking-id=" + trackingNumber)
    case "canada post" | "Canada Post":
        trackingLink = ("https://www.canadapost-postescanada.ca/track-reperage/en#/search?searchFor=" + trackingNumber)
    case "royal mail" | "Royal Mail":
        trackingLink = ("https://www.royalmail.com/track-your-item#/tracking-results/" + trackingNumber)
    case "YunExpress" | "yunexpress" | "yun express":
        trackingLink = ("https://www.yuntrack.com/parcelTracking?id=" + trackingNumber)
    case "4PX" | "4px" | "4 px":
        trackingLink = ("https://m-track.4px.com/#/details/" + trackingNumber)
#Open tracking link/display error
if trackingLink == 0:
    print("Your package carrier may be incorrectly formatted or not supported")
else:
    webbrowser.open_new(trackingLink)
