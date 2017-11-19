import junit.framework.Assert;
import org.junit.jupiter.api.Test;

public class TestFibonacci{

    @Test
    public void testCase1(){
        int input = 0;
        int expectedOutput = 0;
        int actualOutput = Fibonacci.findNthFibonacci(input);
        Assert.assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testCase2(){
        int input = 1;
        int expectedOutput = 1;
        int actualOutput = Fibonacci.findNthFibonacci(input);
        Assert.assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testCase3(){
        int input = 2;
        int expectedOutput = 1;
        int actualOutput = Fibonacci.findNthFibonacci(input);
        Assert.assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testCase4(){
        int input = 4;
        int expectedOutput = 2;
        int actualOutput = Fibonacci.findNthFibonacci(input);
        Assert.assertEquals(expectedOutput, actualOutput);
    }

}