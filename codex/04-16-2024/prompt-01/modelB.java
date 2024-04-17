public class modelB {
    public <T> void myGenericMethod(T argument) {
        // Method body
    }

    public <T> T addOne(T value) {
        if (value instanceof Integer) {
            return (T) (Integer) ((Integer) value + 1);
        } else if (value instanceof Double) {
            return (T) (Double) ((Double) value + 1.0);
        } else {
            // Handle other potential types or throw an exception
            return value;
        }
    }

    public static void main(String[] args) {
        modelB main = new modelB();
        main.myGenericMethod("Hello"); // T is inferred as String
        main.myGenericMethod(10);     // T is inferred as Integer
        main.myGenericMethod(3.14);

        System.out.println(main.addOne(10)); // Output: 11
        System.out.println(main.addOne(3.14)); // Output: 4.14
    }
}
