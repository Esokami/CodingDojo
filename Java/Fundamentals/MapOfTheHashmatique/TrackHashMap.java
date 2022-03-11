import java.util.Set;
import java.util.HashMap;

public class TrackHashMap{
    public static void main (String[] args){
        HashMap<String, String> trackList = new HashMap<String, String>();
        trackList.put("Hometown", "I will let the wind go quietly");
        trackList.put("My Blood", "You don't need to run");
        trackList.put("Jumpsuit", "Pressures of a new place roll my way");
        trackList.put("The Outside", "I am a Megalodon, ocean's felling like a pond");

        System.out.println(trackList.get("Hometown"));
        String song = trackList.get("My Blood");
        System.out.println(song);

        Set<String> track = trackList.keySet();
        for (String single : track){
            System.out.printf("%s : %s \n", single, trackList.get(single));
        }
    }
}