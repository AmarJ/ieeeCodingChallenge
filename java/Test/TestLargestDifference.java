import junit.framework.Assert;
import org.junit.jupiter.api.Test;

public class TestLargestDifference{

    @Test
    public void testCase1(){
        int[] inputArray = {1,5,9,16,28,35};
        int expectedAnswer = 34;
        int actualAnswer = LargestDifference.findLargestDifference(inputArray);
        Assert.assertEquals(expectedAnswer, actualAnswer);
    }

    @Test
    public void testCase2(){
        int[] inputArray = {7,19,15,13,3};
        int expectedAnswer = 12;
        int actualAnswer = LargestDifference.findLargestDifference(inputArray);
        Assert.assertEquals(expectedAnswer, actualAnswer);
    }

    @Test
    public void testCase3(){
        int[] inputArray = {1,1,1,1,1,1,1};
        int expectedAnswer = 0;
        int actualAnswer = LargestDifference.findLargestDifference(inputArray);
        Assert.assertEquals(expectedAnswer, actualAnswer);
    }

    @Test
    public void testCase4(){
        int[] inputArray = {5,4,3,2,1};
        int expectedAnswer = -1;
        int actualAnswer = LargestDifference.findLargestDifference(inputArray);
        Assert.assertEquals(expectedAnswer, actualAnswer);
    }
}