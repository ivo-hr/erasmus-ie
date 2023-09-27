package lab_1;
public class TennisPlayer extends SportsPlayer{
    private double _height;
    private String[] _placeOfBirth; //city/country
    private String _coachName;
    private int _rank;
    private int _prizeMoney; //USD
    private int _hand; //0 is right, 1 is left, 2 abidextrous

    public TennisPlayer(int year, int sex, String name, double height, String nationality, String[] cityCountry, 
                        String coach, int rank, int prize, int hand){
        super(year, sex, name, nationality);
        _height = height;
        _placeOfBirth = cityCountry;
        _coachName = coach;
        _rank = rank;
        _prizeMoney = prize;
        _hand = hand;
    }

    public String toString(){
        

        //convert hand to string
        String hand;
        if (_hand == 0)
            hand = "right";
            else if (_hand == 1)
            hand = "left";
        else hand = "ambidextrous";

        return super.toString() + 
                "- Height: " + _height + "\n" +
                "- Nationality: " + super.getCountry() + "\n" +
                "- Place of Birth: " + _placeOfBirth[0] + ", " + _placeOfBirth[1] + "\n" +
                "- Coach: " + _coachName + "\n" +
                "- Best Rank: " + _rank + "\n" +
                "- Hand: " + hand + "\n" +
                "- Prize Money: USD" + _prizeMoney + "\n";
    }

    public void showNationality(){
        System.out.println(_placeOfBirth[1]);
    }
}
