package akka_euler;

public class Range {

    private int low;
    private int high;

    public Range(int low, int high){
        this.low = low;
        this.high = high;
    }

    public int getLow(){
        return low;
    }

    public int getHigh(){
        return high;
    }
}