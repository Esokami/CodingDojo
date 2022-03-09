import java.util.Date; 
public class AlfredQuotes {
    public String basicGreeting(){
        return "Hello, lovely to see you. How are you?";
    }

    public String guestGreeting(String name){
        String guest = String.format("Hello, %s. Lovely to see you.", name);
        return guest;
    }

    public String dateAnnouncement(){
        Date date = new Date();
        return "It is currently " + date;
    }

    public String respondBeforeAlexis(String conversation){
        int alexis = conversation.indexOf("Alexis"); 
        int alfred = conversation.indexOf("Alfred"); 
        String response; 

        if (alexis >= 0){
            response = "Right away,sir. She certainly isn't sophisticated enough for that.";
        }
        else if (alfred >= 0){
            response = "At your service. As you wish, naturally.";
        }
        else{
            response = "Right. And with that I shall retire.";
        }
        return response;
    }

    // NINJA BONUS
    // See the specs to overload the guestGretting method

    public String guestGreeting(String dayPeriod, String name){
        
        String guestDay = String.format("Good %s, %s. Lovely to see you.", dayPeriod, name);

        return guestDay;
    }

    // SENSEI BONUS
    // Write your own AlfredQuote method using any of the String methods you have learned
}