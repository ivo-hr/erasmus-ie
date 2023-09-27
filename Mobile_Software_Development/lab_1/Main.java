package lab_1;

import lab_1.SportsPlayer;

public class Main {
    public static void main(String[] args){
        TennisPlayer player1 = new TennisPlayer(1990, 0, "Roger Federer", 1.85, "Switzerland", new String[]{"Basel", "Switzerland"}, "Ivan Ljubicic", 2, 110235682, 0);
        TennisPlayer player2 = new TennisPlayer(1969, 0, "Rogerto Federerto", 1.85, "Swislandia", new String[]{"based", "Gronrodón"}, "Ivan Turbao", 1000, 70, 3);
    
        System.out.println(player1.toString());
        System.out.println(player2.toString());

        System.out.println("Number of players: " + SportsPlayer.getNumPlayers());
        player1.showAge();
        player1.showNationality();

        player2.showAge();
        player2.showNationality();
    }
}
