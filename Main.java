import java.util.Scanner;

class MiscMethods{
    public void Clear_Term(){
        String ANSI_Clear_Term = "\033[2J\033[H";
        System.out.println(ANSI_Clear_Term);
    }
    String[][] BaseMap = {
        {"|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "},
        {"|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "},
        {"|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "},
        {"|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "},
        {"|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "},
        {"|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "},
        {"|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","_","_","_"," "," "," "," "," "," "," "," "," "," "},
        {"|"," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ","_","_","_","|"," "," "," ","|"," "," "," ","_","_","_"," "," ","|"},
        {"|"," "," "," "," "," ","_","_","_"," "," ","_","_","_","_","|"," "," "," "," "," "," "," ","|"," "," ","|","_","_","_","|"," "},
        {"|","_","_","_","_","|"," "," "," ","^","^"," "," "," "," "," "," "," "," "," "," "," "," ","|"," "," "," "," "," "," "," "," "},
        {" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "}
    };
    int PlayerX = 3;
    int PlayerY = 9;
    
    public void PrintArray(String[][]GivenArray){
        for (int i = 0; i<GivenArray.length;i++){
            for (int j = 0; j<GivenArray[i].length;j++){
                System.out.print(GivenArray[i][j]);
            }
            System.out.println();
        }
    }
    public void ChangeMapChar(int LocY, int LocX, String Replacement,String[][]GivenArray){
        for (int row = 0; row <= LocY; row++) { // Iterate through rows
            for (int col = 0; col <= LocX; col++) { // Iterate through columns in the current row
                if (row == LocY){ //Checks if specific location is coordinates, if so, it executes
                    if (col == LocX){
                        GivenArray[row][col] = Replacement;
                    }
                } 
            }
        }
    } 
    
    Boolean[] ColList = {false,false,false,false}; //Left, right, up, down
    public void UpdateColList(String[][]GivenArray){
        ColList[0] = GivenArray[PlayerY][PlayerX-1].equalsIgnoreCase("|"); //Left collision w/|
        ColList[1] = GivenArray[PlayerY][PlayerX+1].equalsIgnoreCase("|"); //BREAK Right collision w/|
        if (GivenArray[PlayerY][PlayerX].equalsIgnoreCase("_")){ //Down collision w/_ and |
            ColList[3] = true;
        }
        else ColList[3] = GivenArray[PlayerY+1][PlayerX].equalsIgnoreCase("|");
        if (GivenArray[PlayerY-1][PlayerX].equalsIgnoreCase("_")){ //Up collision w/_ and |
            ColList[2] = true;
        }
        else ColList[2] = GivenArray[PlayerY-1][PlayerX].equalsIgnoreCase("|");
    }
}

public class Main{ //Class where things actually get executed
    public static void main(String[] args) {
        MiscMethods Misc = new MiscMethods(); //Making Misc callable

        int jumpcooldown = 0; //Vars
        int VertMom = 0;
        int attackcooldown = 0;
        boolean running = true;
        Scanner ActionScanner = new Scanner(System.in);

        Scanner scannerClass = new Scanner(System.in);
        System.out.print("Choose a class\n   -Wizard\n   -Rogue\n   -Warrior\n   -Archer\nInput class here: ");
        String classInput = scannerClass.nextLine();
        //scannerClass.close();
        String Class = classInput;
        Misc.Clear_Term();

        while (running = true){ //Main loop
            String[][]CopyMap = new String[Misc.BaseMap.length][]; //Making copy map
            for (int i = 0; i<Misc.BaseMap.length; i++){
                CopyMap[i] = new String [Misc.BaseMap[i].length];
                for (int j = 0; j<Misc.BaseMap[i].length; j++){
                    CopyMap[i][j] = Misc.BaseMap[i][j];
                }
            } //Copy map made

            Misc.UpdateColList(Misc.BaseMap); //Updating list of left, right, down, up collision

            VertMom--;
            if (VertMom < 0){
                VertMom = -1;
            }
            if (Misc.ColList[3] == true){
                if (VertMom <= 0){
                    VertMom = 0;
                }
            }
            Misc.PlayerY -= VertMom;
            
            //Scanner ActionScanner = new Scanner(System.in);
            System.out.print("Choose an action\n   -a (left) \n   -d (right) \n   -w (jump) turns until ready: " + jumpcooldown + "\n   -e (attack) turns until ready: " + attackcooldown + "\nInput action here: ");
            String action = ActionScanner.nextLine();
            
            Misc.Clear_Term(); //Clear terminal

            if (action.equalsIgnoreCase("a")){
                if (Misc.ColList[0] == false){
                    Misc.PlayerX -= 1;
                }
            }
            if (action.equalsIgnoreCase("d")){
                if (Misc.ColList[1] == false){
                    Misc.PlayerX += 1; 
                }           
            }
            if (action.equalsIgnoreCase("w")){
                if (Misc.ColList[3] == true){
                    VertMom = +2;
                }
            }
            if (action.equalsIgnoreCase("e")){
                //Misc.PlayerX -= 1;
            }

            Misc.ChangeMapChar(Misc.PlayerY,Misc.PlayerX,"O",CopyMap);
            Misc.PrintArray(CopyMap); //Prints final map. Goes near end

            //try { //Time pause. GOES AT END!
            //    Thread.sleep(1000); //Pause in milliseconds, curently 1 second frames
            //} catch (InterruptedException e) {
            //    Thread.currentThread().interrupt();
            //    System.err.println("Thread was interupted during sleep: " + e.getMessage());
            //}
        }
    }
}

