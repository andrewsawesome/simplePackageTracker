#Opens the tracking information for your package based on your carrier
#import needed packages and reset all vars
#Get tracking number and courrier from user
$trackingLink=0
$trackingNumber = Read-Host("What is your tracking number? ")
$carrier = Read-Host("What is the package Carrier? ")
#Create tracking link
echo($trackingNumber)
echo($carrier)

#if($carrier -eq "USPS" -or $_ -eq "usps"){$trackingLink = "https://tools.usps.com/go/TrackConfirmAction_input?origTrackNum=$trackingNumber"}

switch($carrier){
    {$_ -eq "USPS" -or $_ -eq "usps"}{$trackingLink = "https://tools.usps.com/go/TrackConfirmAction_input?origTrackNum=$trackingNumber"}
    {$_ -eq "UPS" -or $_ -eq "ups"}{$trackingLink = "https://www.ups.com/track?sort_by=status&tracknums_displayed=1&TypeOfInquiryNumber=T&loc=en_us&InquiryNumber1=$trackingNumberU&requester=ST"}
    {$_ -eq "FedEx" -or $_ -eq "Fedex" -or $_ -eq "fedex"}{$trackingLink ="https://www.fedex.com/wtrk/track/?trknbr=$trackingNumber"}
    {$_ -eq "DHL" -or $_ -eq "dhl"}{$trackingLink = "https://www.dhl.com/us-en/home/tracking.html?tracking-id=$trackingNumber"}
    {$_ -eq "Australia Post" -or $_ -eq "australia post"}{$trackingLink = "https://auspost.com.au/mypost/track/details/$trackingNumber"}
    {$_ -eq "Canada Post" -or $_ -eq "canada post"}{$trackingLink ="https://www.canadapost-postescanada.ca/track-reperage/en#/search?searchFor=$trackingNumber"}
    {$_ -eq "New Zealand Post" -or $_ -eq "new zealand post"}{$trackingLink ="https://www.nzpost.co.nz/tools/tracking?trackid=$trackingNumber"}
    {$_ -eq "Royal Mail" -or $_ -eq "royal mail"}{$trackingLink = "https://www.royalmail.com/track-your-item#/tracking-results/$trackingNumber"}
    {$_ -eq "4PX" -or $_ -eq "4px" -or $_ -eq "4 px"}{$trackingLink ="https://m-track.4px.com/#/details/$trackingNumber"}    
    {$_ -eq "YunExpress" -or $_ -eq "yunexpress" -or $_ -eq "yun express"}{$trackingLink ="https://www.yuntrack.com/parcelTracking?id=$trackingNumber"}
        }
#Open tracking link/display error
echo($trackingLink)
if ($trackingLink -eq 0){echo("Your package carrier may be incorrectly formatted or not supported")}
else{Start-Process $trackingLink}