public class Counter {
    public void printNumbers() {
      try {
        for (int i = 1; i <= 10; i++) {
            System.out.println(i);
            Thread.sleep(1000);
        }
      } catch (Exception e) {
          System.err.println("exception");
      }
    }
    public static void main(String args[]) {
      new Counter().printNumbers();
    }
}
