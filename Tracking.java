import java.util.Scanner;
import java.awt.Desktop;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
public class Tracking{

    public static void main(String [] args){
    Scanner input = new Scanner(System.in);
    input.useDelimiter("/n");

    String [] inputArray = new String[2];
    System.out.println("Enter tracking number, press enter, then enter carrier");
    for (int i = 0; i < 2; i++) {
        inputArray[i] = input.nextLine();
    }
    input.close();

    
    processor(Integer.parseInt(inputArray[0]), inputArray[1]);
    //input.close();
    }


    public static void processor(int trackingNumber, String carrier){
        String trackingLink = "";

        switch(carrier){
        case "USPS":
        case "usps":
            trackingLink = ("https://tools.usps.com/go/TrackConfirmAction_input?origTrackNum=" + trackingNumber);
            break;
        case "UPS":
        case "ups":
            trackingLink = ("https://www.ups.com/track?sort_by=status&tracknums_displayed=1&TypeOfInquiryNumber=T&loc=en_us&InquiryNumber1=" + trackingNumber + "&requester=ST");
            break;
        case "FedEx":
        case "Fedex":
        case "fedex":
            trackingLink = ("https://www.fedex.com/wtrk/track/?trknbr=" + trackingNumber);
            break;
        case "DHL":
        case "dhl":
            trackingLink = ("https://www.dhl.com/us-en/home/tracking.html?tracking-id=" + trackingNumber);
            break;
        case "Australia Post":
        case "australia post":
            trackingLink = ("https://auspost.com.au/mypost/track/details/" + trackingNumber);
            break;
            case "Canada Post":
        case "canada post":
            trackingLink = ("https://www.canadapost-postescanada.ca/track-reperage/en#/search?searchFor=" + trackingNumber);
            break;
            case "New Zealand Post":
        case "new zealand post":
            trackingLink = ("https://www.nzpost.co.nz/tools/tracking?trackid=" + trackingNumber);
            break;
            case "Royal Mail":
        case "royal mail":
            trackingLink = ("https://www.royalmail.com/track-your-item#/tracking-results/" + trackingNumber);
            break;
            case "4PX":
        case "4px":
        case "4 px":
            trackingLink = ("https://m-track.4px.com/#/details/" + trackingNumber);    
            break;
        case "YunExpress":
        case "yunexpress": 
        case "yun express":
            trackingLink = ("https://www.yuntrack.com/parcelTracking?id=" + trackingNumber);
            break;
        }


        if(trackingLink !="")
        {openURL(trackingLink);}
        else{System.out.println("Your package carrier may be incorrectly formatted or not supported");}
        }

    public static void openURL(String url){
        try{Desktop.getDesktop().browse(new URI(url));}
        catch(URISyntaxException badURI){System.err.println("Bad URL");}
        catch(IOException badIO){System.err.println("IO Error");}
        }

    
}
