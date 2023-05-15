package AbstractShape;


public class Main {
    public static void main(String[] args) {
Dimensions square = new Square(2,4);
        int squareArea = square.CalArea();
        System.out.println("The area of Square is: "+squareArea);
        int squareperimeter = square.perimeter();
        System.out.println("The perimeter of Square is: "+squareperimeter);
        Dimensions cube = new Cube(3, 4);
        int cubeArea = cube.CalArea();
        System.out.println("The area of Cube is: "+cubeArea);
        int cubeperimeter = cube.perimeter();
        System.out.println("The perimeter of Cube is: "+cubeperimeter);
         
    }
}
