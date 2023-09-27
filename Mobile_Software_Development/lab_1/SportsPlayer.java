package lab_1;


public class SportsPlayer implements PrintValues{
    private int _year;
    private int _sex; //0 is male, 1 female
    private String _name;
    protected String _country;

    private static int _numPlayers = 0;

    public SportsPlayer(int year, int sex, String name, String country){
        _year = year;
        _sex = sex;
        _name = name;
        _country = country;
        _numPlayers++;
    }

    public SportsPlayer(){
        _year = 0;
        _sex = 0;
        _name = "";
        _country = "";
        _numPlayers++;
    }

    protected String getCountry(){
        return _country;
    }

    //output all the information of the player
    public String toString(){
        return "Details of " + _name + "\n" +
                "- Born in " + _year + "\n";
    }

    public void showAge(){
        System.out.println("Age: " + (2023 - _year));
    }

    public void showNationality(){
        System.out.println(_country);
    }

    public static int getNumPlayers(){
        return _numPlayers;
    }
}
