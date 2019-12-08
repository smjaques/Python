import java.io.*;
import java.util.*;

public class LCS {
    public int[][] matchValue = new int[5][5];
    public String string1;
    public String string2;
    private int s1Len;
    private int s2Len;
    public int[][] LCS;


    public void readFile(String filename){
        try {
            BufferedReader reader = new BufferedReader(new FileReader(filename));
            string1 = reader.readLine();
            string2 = reader.readLine();
            s1Len = string1.length();
            s2Len = string2.length();
            reader.readLine();
            int i=0;
            String line = reader.readLine();
            while(line != null){
                String[] vals = line.split(" ");
                for(int j=1; j < vals.length; j++){
                    matchValue[i][j-1] = Integer.parseInt(vals[j]);
                }
                i++;
                line = reader.readLine();
            }

        } catch (Exception e){
            System.out.println(e);
        }
    }

    private int getMatchVal(int v1, int v2){
        int i = s1Len;
        int j = s2Len;
        if(v1 == 'A')
            i = 0;
        else if(v1 == 'C')
            i = 1;
        else if(v1 == 'G')
            i = 2;
        else if(v1 == 'T')
            i = 3;
        else if(v1 == '-')
            i = 4;
        if(v2 == 'A')
            j = 0;
        else if(v2 == 'C')
            j = 1;
        else if(v2 == 'G')
            j = 2;
        else if(v2 == 'T')
            j = 3;
        else if(v2 == '-')
            j = 4;

        return matchValue[i][j];
    }

    public void fillInZeroCases(){
        LCS[0][1] = matchValue[0][1];
        LCS[1][0] = matchValue[1][0];
        for (int j = 1; j < s1Len; j++) {
            LCS[0][j] = LCS[0][j - 1] + getMatchVal(string1.charAt(j), '-');
        }
        for(int k = 1; k < s2Len; k++){
            LCS[k][0] = LCS[k-1][0] + getMatchVal(string2.charAt(k), '-');
        }
    }

    public int fillInTable(){
        LCS = new int[s2Len+1][s1Len+1];
        string1 = " " + string1;
        string2 = " " + string2;
        s1Len+=1;
        s2Len+=1;
        fillInZeroCases();
        for(int i = 1; i < s2Len; i++) {
            for (int j = 1; j < s1Len; j++) {
                int v1 = string1.charAt(j);   //to find match value
                int v2 = string2.charAt(i);
                int matchVal = getMatchVal(v1, v2) + LCS[i-1][j-1];
                int top = LCS[i-1][j] + getMatchVal('-', string2.charAt(i));
                int left = LCS[i][j-1] + getMatchVal('-', string1.charAt(j));
                int bestOfSides = Integer.max(top, left);
                LCS[i][j] = Integer.max(bestOfSides,matchVal);
            }
        }

        return LCS[s2Len-1][s1Len-1];
    }

    public void retrace(){
        String finalSeq1 = "";
        String finalSeq2 = "";
        //start from bottom and retrace to find words!
        int i = s2Len-1;
        int j = s1Len-1;
        while((i != 0) && (j!=0)){
            //if value if from above
            if(LCS[i-1][j] == LCS[i][j]){
                finalSeq1 = " -" + finalSeq1;
                finalSeq2 = " " + string2.charAt(i) + finalSeq2;
                i--;
            }
            //if value is from the left
            else if(LCS[i][j-1] == LCS[i][j]){
                finalSeq2 = " -" + finalSeq2;
                finalSeq1 = " " + string1.charAt(j) + finalSeq1;
                j--;
            }
            //if value is from a match
            else{
                finalSeq1 = " " + string1.charAt(j) + finalSeq1;
                finalSeq2 = " " + string2.charAt(i) + finalSeq2;
                i--;
                j--;
            }

        }
        if((i==0) && (j!=0)){
            finalSeq1 = " " + string1.charAt(j) + finalSeq1;
            finalSeq2 = " -" + finalSeq2;
        } else if((j==0) & (i!=0)){
            finalSeq2 = " " + string2.charAt(i) + finalSeq2;
            finalSeq1 = " -" + finalSeq1;
        }

        System.out.println("x:" + finalSeq1);
        System.out.println("y:" + finalSeq2);
    }

}
