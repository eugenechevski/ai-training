public class modelA {
  public static <T> void printElement(T element) {
    System.out.println("Element: " + element);
  }

  public static void main(String[] args) {
    String name = "Alice";
    int age = 30;

    printElement(name); // Output: Element: Alice
    printElement(age);   // Output: Element: 30
  }
}