import junit.framework.Assert;
import org.junit.jupiter.api.Test;

public class TestNumberOfRepeats {

    @Test
    private void testCase1(){
        String a = "abcde";
        String b = "abcdabcdabcd";
        int expectedAnswer = -1;
        int actualAnswer = NumberOfRepeats.findNumberOfRepeats(a,b);
        Assert.assertEquals(expectedAnswer, actualAnswer);
    }

    @Test
    private void testCase2(){
        String a = "abcd";
        String b = "abcdabdcabcd";
        int expectedAnswer = -1;
        int actualAnswer = NumberOfRepeats.findNumberOfRepeats(a,b);
        Assert.assertEquals(expectedAnswer, actualAnswer);
    }

    @Test
    private void testCase3(){
        String a = "aaab";
        String b = "baaabaa";
        int expectedAnswer = 3;
        int actualAnswer = NumberOfRepeats.findNumberOfRepeats(a,b);
        Assert.assertEquals(expectedAnswer, actualAnswer);
    }

    @Test
    private void testCase4(){
        String a = "abcde";
        String b = "abcdabcdabcd";
        int expectedAnswer = -1;
        int actualAnswer = NumberOfRepeats.findNumberOfRepeats(a,b);
        Assert.assertEquals(expectedAnswer, actualAnswer);
    }

}