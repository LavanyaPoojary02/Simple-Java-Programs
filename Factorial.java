public class Factorial {
    public static void main(String[] args) {
        int nums = 5;
        int facts = 1;

        for(int i = 1; i <= nums; i++) {
            facts = facts * i;
        }

        System.out.println("Factorial of " + nums + " is " + facts);
    }
}
