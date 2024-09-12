#Opens the tracking information for your package based on your carrier
#import needed packages and reset all vars
import webbrowser
trackingLink = 0
#Get tracking number and courrier from user
trackingNumber = input("What is your tracking number? ")
carrier = input("What is the package Carrier? ")
#Open tracking link
if carrier=="USPS":
    trackingLink = ("https://tools.usps.com/go/TrackConfirmAction_input?origTrackNum=" + trackingNumber)
if carrier=="usps":
    trackingLink = ("https://tools.usps.com/go/TrackConfirmAction_input?origTrackNum=" + trackingNumber)
if carrier=="UPS":
    trackingLink = ("https://www.ups.com/track?sort_by=status&tracknums_displayed=1&TypeOfInquiryNumber=T&loc=en_us&InquiryNumber1=" + trackingNumber + U"&requester=ST")
if carrier=="ups":
    trackingLink = ("https://www.ups.com/track?sort_by=status&tracknums_displayed=1&TypeOfInquiryNumber=T&loc=en_us&InquiryNumber1=" + trackingNumber + U"&requester=ST")
if carrier=="FedEx":
    trackingLink = ("https://www.fedex.com/wtrk/track/?trknbr=" + trackingNumber)
if carrier=="Fedex":
    trackingLink = ("https://www.fedex.com/wtrk/track/?trknbr=" + trackingNumber)
if carrier=="fedex":
    trackingLink = ("https://www.fedex.com/wtrk/track/?trknbr=" + trackingNumber)
if trackingLink == 0:
    print("Your package carrier may be incorrectly formatted or not supported")
else:
    webbrowser.open_new(trackingLink)